from flask import Flask, request, jsonify
from openai import OpenAI
import requests
import os
import time
from dotenv import load_dotenv
from newtools_v1 import tools
from functions2_v1 import *
#from functions2 import call_antardasha_api,call_kaalsarp_dosh_api,call_mahadasha_api,call_mahadasha_predictions_api,call_mangal_dosh_api,call_manglik_dosh_api,call_papasamaya_api,call_pitra_dosh_api,current_sade_sati,get_ex_horo,gem_suggestion,get_ascendant_report,get_astro_dashas,get_astro_dosh,get_char_dasha_current,get_char_dasha_main,get_char_dasha_sub,get_current_mahadasha,get_current_mahadasha_full,get_horo,get_paryantar_dasha,get_planet_details,get_planet_report,get_yogini_dasha_main,friendship_table,sade_sati_table,find_ascendant,find_moon_sign,find_sun_sign,kp_houses,kp_planets,extended_kundli_details,rudraksh_suggestion,varshapal_details,varshapal_month_chart,varshapal_year_chart,get_specific_dasha,get_aggregate_match,get_ashtakoot_with_astro_details,get_choghadiya_muhurta,get_dashakoot_match,get_dashakoot_with_astro_details,get_monthly_panchang,get_moon_calendar,get_moon_phase,get_moon_rise,get_moon_set,get_nakshatra_match,get_panchang,get_papasamaya_match,get_rajju_vedha_details,get_retrogrades,get_solar_noon,get_sun_rise,get_sun_set,get_ashtakoot_match,get_hora_muhurta,get_personal_characteristics
import json
import base64

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
    "get_nakshatra_vastu_details":get_nakshatra_vastu_details

}

assistant_id = "asst_Rr5fZne22yP1TWUIoUzp2OKn" 
"""my_updated_assistant = client.beta.assistants.update(
   assistant_id,
   tools=tools
)"""

def your_main_function(user_query):

    query = user_query
    thread = client.beta.threads.create()
    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=query
    )

    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id
    )

    while True:
        run_status = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )

        if run_status.status == 'completed':
            messages = client.beta.threads.messages.list(thread_id=thread.id)
            latest_message = messages.data[0]
            text = latest_message.content[0].text.value
            return text
            '''
            user_input = input()
            if user_input.lower() == "stop":
                break
            client.beta.threads.messages.create(
                thread_id=thread.id,
                role="user",
                content=user_input
            )

            run = client.beta.threads.runs.create(
                thread_id=thread.id,
                assistant_id=assistant_id
            )'''

        elif run_status.status == 'requires_action':
            #print("Requires action")
            required_actions = run_status.required_action.submit_tool_outputs.model_dump()
            #print(required_actions)
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
                thread_id=thread.id,
                run_id=run.id,
                tool_outputs=tools_output
            )

        else:
            #print("Waiting for the Assistant to process...")
            time.sleep(1)




app = Flask(__name__)


@app.route('/api/query', methods=['POST'])
def handle_query():
    try:
        data = request.json
        user_query = data.get('query')
        if user_query:
            response = your_main_function(user_query)
            return jsonify({'response': response})
        else:
            return jsonify({'error': 'No query provided'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    from gunicorn.app.wsgiapp import WSGIApplication
    WSGIApplication("%(application)s").run()