#importing dependices
from openai import OpenAI
import requests
import os
import time
from tools2 import tools
from flask import Flask, request, Response, session
from functions2 import *
import json
import secrets
import base64
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError('OPENAI_API_KEY environment variable not set')

client = OpenAI(api_key=api_key)
ASTRO_API_KEY = os.getenv('ASTRO_API_KEY', 'dfa2b8e6-d4f5-584a-b08c-e0a1e0150047')


tools = tools

function_dispatch_table = {
    "get_mangal_dosh_api": get_mangal_dosh_api,
    "get_kaalsarp_dosh_api": get_kaalsarp_dosh_api,
    "get_manglik_dosh_api": get_manglik_dosh_api,
    "get_pitra_dosh_api" :get_pitra_dosh_api,
    "get_papasamaya_api" :get_papasamaya_api,
    "get_mahadasha_api"  :get_mahadasha_api,
    "get_mahadasha_predictions_api":get_mahadasha_predictions_api,
    "get_antardasha_api":get_antardasha_api,
    "get_char_dasha_current":get_char_dasha_current,
    "get_char_dasha_main" :get_char_dasha_main,
    "get_current_mahadasha": get_current_mahadasha,
    "get_yogini_dasha_main": get_yogini_dasha_main,
    "get_char_dasha_sub":get_char_dasha_sub,
    "get_current_mahadasha_full":get_current_mahadasha_full,
    "get_paryantar_dasha":get_paryantar_dasha,
    "find_moon_sign":find_moon_sign,
    "find_sun_sign":find_sun_sign,
    "find_ascendant":find_ascendant,
    "get_specific_dasha":get_specific_dasha,
    "current_sade_sati":current_sade_sati,
    "extended_kundli_details":extended_kundli_details,
    "sade_sati_table":sade_sati_table,
    "friendship_table":friendship_table,
    "kp_houses":kp_houses,
    "kp_planets":kp_planets,
    "gem_suggestion":gem_suggestion,
    "rudraksh_suggestion":rudraksh_suggestion,
    "varshapal_details":varshapal_details,
    "varshapal_month_chart":varshapal_month_chart,
    "varshapal_year_chart":varshapal_year_chart,
    "get_planet_details":get_planet_details,
    "get_ascendant_report":get_ascendant_report,
    "get_planet_report":get_planet_report,
    "get_ashtakoot_match":get_ashtakoot_match,
    "get_ashtakoot_with_astro_details":get_ashtakoot_with_astro_details,
    "get_dashakoot_match":get_dashakoot_match,
    "get_dashakoot_with_astro_details":get_dashakoot_with_astro_details,
    "get_aggregate_match":get_aggregate_match,
    "get_rajju_vedha_details":get_rajju_vedha_details,
    "get_papasamaya_match":get_papasamaya_match,
    "get_nakshatra_match":get_nakshatra_match,
    "get_panchang":get_panchang,
    "get_monthly_panchang":get_monthly_panchang,
    "get_choghadiya_muhurta":get_choghadiya_muhurta,
    "get_hora_muhurta":get_hora_muhurta,
    "get_moon_calendar":get_moon_calendar,
    "get_moon_phase":get_moon_phase,
    "get_moon_rise":get_moon_rise,
    "get_moon_set":get_moon_set,
    "get_solar_noon":get_solar_noon,
    "get_sun_rise":get_sun_rise,
    "get_sun_set":get_sun_set,
    "get_retrogrades":get_retrogrades,
    "get_personal_characteristics":get_personal_characteristics,
    "get_daily_sun":get_daily_sun,
    "get_daily_moon":get_daily_moon,
    "get_daily_nakshatra":get_daily_nakshatra,
    "get_weekly_moon":get_weekly_moon,
    "get_weekly_sun":get_weekly_sun,
    "get_yearly":get_yearly,
    "get_biorythm":get_biorythm,
    "get_gem_details":get_gem_details,
    "get_nakshatra_vastu_details":get_nakshatra_vastu_details,
    "get_current_date_time":get_current_date_time
    # Add other functions here as needed
}

assistant_id = "asst_kcijOKWplEtKqVuk1QMgSpX0"  # Use your actual assistant ID
my_updated_assistant = client.beta.assistants.update(
   assistant_id,
   tools=tools
)

app = Flask(__name__)
app.secret_key = secrets.token_hex(16) 
# Setting a secret key for session management  store secret keys in environment variables or secure configuration files that are not included in the source code repository.

def create_new_thread():
    thread = client.beta.threads.create()
    return thread.id

def your_main_function(user_query, thread_id):
    client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=user_query
    )

    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id
    )

    while True:
        run_status = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run.id
        )

        if run_status.status == 'completed':
            messages = client.beta.threads.messages.list(thread_id=thread_id)
            latest_message = messages.data[0]
            text = latest_message.content[0].text.value
            return text

        elif run_status.status == 'requires_action':
            required_actions = run_status.required_action.submit_tool_outputs.model_dump()
            tools_output = []

            for action in required_actions["tool_calls"]:
                func_name = action["function"]["name"]
                arguments = json.loads(action["function"]["arguments"])

                func = function_dispatch_table.get(func_name)
                if func:
                    result = func(**arguments)
                    output = json.dumps(result) if not isinstance(result, str) else result
                    tools_output.append({
                        "tool_call_id": action["id"],
                        "output": output
                    })
                else:
                    print(f"Function {func_name} not found")

            client.beta.threads.runs.submit_tool_outputs(
                thread_id=thread_id,
                run_id=run.id,
                tool_outputs=tools_output
            )

        else:
            time.sleep(1)

@app.route('/', methods=['POST'])
def handle_query():
    data = request.json
    user_query = data.get('query')
    if user_query:
        if 'thread_id' not in session:
            session['thread_id'] = create_new_thread()

        response = your_main_function(user_query, session['thread_id'])
        response_data = json.dumps({'response': response})
        return Response(response_data, mimetype='application/json')
    else:
        error_response_data = json.dumps({'error': 'No query provided'})
        return Response(error_response_data, mimetype='application/json', status=400)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
    from gunicorn.app.wsgiapp import WSGIApplication
    WSGIApplication("%(application)s").run()
