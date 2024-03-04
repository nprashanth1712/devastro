import requests
import json
import base64

ASTRO_API_KEY = "dfa2b8e6-d4f5-584a-b08c-e0a1e0150047"

def get_astro_dosh(dosh_type, dob, tob, lat, lon):
    base_url = f"https://api.vedicastroapi.com/v3-json/dosha/{dosh_type}"
    
    params = {
        "dob": dob,
        "tob": tob,
        "lat": lat,
        "lon": lon,
        "tz": 5.5,
        "api_key": ASTRO_API_KEY,
        "lang": "en"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises HTTPError for 4xx and 5xx responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error calling {dosh_type.replace('-', ' ').capitalize()} API: {e}")
        return None

def get_mangal_dosh_api(dob, tob, lat, lon):
    return get_astro_dosh("mangal-dosh", dob, tob, lat, lon)

def get_kaalsarp_dosh_api(dob, tob, lat, lon):
    return get_astro_dosh("kaalsarp-dosh", dob, tob, lat, lon)

def get_manglik_dosh_api(dob, tob, lat, lon):
    return get_astro_dosh("manglik-dosh", dob, tob, lat, lon)
def get_pitra_dosh_api(dob, tob, lat, lon):
    return get_astro_dosh("pitra-dosh", dob, tob, lat, lon)
def get_papasamaya_api(dob, tob, lat, lon):
    return get_astro_dosh("papasamaya", dob, tob, lat, lon)


def get_astro_dashas(dashas_type,dob, tob, lat, lon):
    base_url = f"https://api.vedicastroapi.com/v3-json/dashas/{dashas_type}"
    params = {
        "dob": dob,
        "tob": tob,
        "lat": lat,
        "lon": lon,
        "tz": 5.5,
        "api_key": ASTRO_API_KEY,
        "lang": "en"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises HTTPError for 4xx and 5xx responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error calling {dashas_type.replace('-', ' ').capitalize()} API: {e}")
        return None

def get_mahadasha_api(dob, tob, lat, lon):
    return get_astro_dashas("maha-dasha", dob, tob, lat, lon)
def get_mahadasha_predictions_api(dob, tob, lat, lon):
    return get_astro_dashas("maha-dasha-predictions", dob, tob, lat, lon)
def get_antardasha_api(dob, tob, lat, lon):
    return get_astro_dashas("antar-dasha", dob, tob, lat, lon)
def get_char_dasha_current(dob, tob, lat, lon):
    return get_astro_dashas("char-dasha-current", dob, tob, lat, lon)
def get_char_dasha_main(dob, tob, lat, lon):
    return get_astro_dashas("char-dasha-main", dob, tob, lat, lon)
def get_current_mahadasha(dob,tob,lat,lon):
    return get_astro_dashas("current-mahadasha", dob, tob, lat, lon)
def get_yogini_dasha_main(dob, tob, lat, lon):
    return get_astro_dashas("yogini-dasha-main", dob, tob, lat, lon)
def get_char_dasha_sub(dob,tob,lat,lon):
    return get_astro_dashas("char-dasha-sub", dob, tob, lat, lon)
def get_current_mahadasha_full(dob,tob,lat,lon):
    return get_astro_dashas("current-mahadasha-full", dob, tob, lat, lon)
def get_paryantar_dasha(dob,tob,lat,lon):
    return get_astro_dashas("paryantar-dasha", dob, tob, lat, lon)
def get_specific_dasha(dob, tob, lat, lon,md,ad,pd,sd):
    base_url = f"https://api.vedicastroapi.com/v3-json/dashas/specific-sub-dasha"
    params = {
       "dob": dob,  # Date of birth
       "tob": tob,       # Time of birth
       "lat": lat,            # Latitude
       "lon": lon,            # Longitude
       "tz": 5.5,            # Timezone
       "md": md,       # Mahadasha planet
       "ad": ad,          # Antardasha planet
       "pd": pd,      # Pratyantardasha planet
       "sd": sd,         # Sookshmadasha planet
       "lang": "en",         # Language
       "api_key": ASTRO_API_KEY  # Your API key
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises HTTPError for 4xx and 5xx responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error calling API: {e}")
        return None


def get_ex_horo(ex_type,dob,tob,lat,lon):
    base_url = f"https://api.vedicastroapi.com/v3-json/extended-horoscope/{ex_type}"
    params = {
        "dob": dob,
        "tob": tob,
        "lat": lat,
        "lon": lon,
        "tz": 5.5,
        "api_key": ASTRO_API_KEY,
        "lang": "en"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises HTTPError for 4xx and 5xx responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error calling {ex_type.replace('-', ' ').capitalize()} API: {e}")
        return None

def find_moon_sign(dob,tob,lat,lon):
    return get_ex_horo("find-moon-sign", dob, tob, lat, lon)
def find_sun_sign(dob,tob,lat,lon):
    return get_ex_horo("find-sun-sign", dob, tob, lat, lon)
def find_ascendant(dob,tob,lat,lon):
    return get_ex_horo("find-ascendant", dob, tob, lat, lon)
def current_sade_sati(dob,tob,lat,lon):
    return get_ex_horo("current-sade-sati", dob, tob, lat, lon)
def extended_kundli_details(dob,tob,lat,lon):
    return get_ex_horo("extended-kundli-details", dob, tob, lat, lon)
def sade_sati_table(dob,tob,lat,lon):
    return get_ex_horo("sade-sati-table", dob, tob, lat, lon)
def friendship_table(dob,tob,lat,lon):
    return get_ex_horo("friendship", dob, tob, lat, lon)
def kp_houses(dob,tob,lat,lon):
    return get_ex_horo("kp-houses", dob, tob, lat, lon)
def kp_planets(dob,tob,lat,lon):
    return get_ex_horo("kp-planets", dob, tob, lat, lon)
def gem_suggestion(dob,tob,lat,lon):
    return get_ex_horo("gem-suggestion", dob, tob, lat, lon)
def rudraksh_suggestion(dob,tob,lat,lon):
    return get_ex_horo("rudraksh-suggestion", dob, tob, lat, lon)
def varshapal_details(dob,tob,lat,lon):
    return get_ex_horo("varshapal-details", dob, tob, lat, lon)
def varshapal_month_chart(dob,tob,lat,lon):
    return get_ex_horo("varshapal-month-chart", dob, tob, lat, lon)
def varshapal_year_chart(dob,tob,lat,lon):
    return get_ex_horo("varshapal-year-chart", dob, tob, lat, lon)
def varshapal_year_chart(dob,tob,lat,lon):
    return get_ex_horo("varshapal-year-chart", dob, tob, lat, lon)

def get_horo(horo_type,dob,tob,lat,lon):
    base_url = f"https://api.vedicastroapi.com/v3-json/horoscope/{horo_type}"
    params = {
        "dob": dob,
        "tob": tob,
        "lat": lat,
        "lon": lon,
        "tz": 5.5,
        "api_key": ASTRO_API_KEY,
        "lang": "en"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises HTTPError for 4xx and 5xx responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error calling {horo_type.replace('-', ' ').capitalize()} API: {e}")
        return None
    
def get_planet_details(dob,tob,lat,lon):
    return get_horo("planet-details", dob, tob, lat, lon)
def get_ascendant_report(dob,tob,lat,lon):
    return get_horo("ascendant-report", dob, tob, lat, lon)
def get_planet_report(dob,tob,lat,lon,planet):
    base_url = f"https://api.vedicastroapi.com/v3-json/horoscope/planet-report"
    params = {
        "dob": dob,
        "tob": tob,
        "lat": lat,
        "lon": lon,
        "planet": planet,
        "tz": 5.5,
        "api_key": ASTRO_API_KEY,
        "lang": "en"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises HTTPError for 4xx and 5xx responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error calling API: {e}")
        return None

def get_personal_characteristics(dob,tob,lat,lon):
    return get_horo("personal-characteristics", dob, tob, lat, lon)

#add 4 here

def astro_match(match_type,boy_dob,boy_tob,boy_lat,boy_lon,girl_dob,girl_tob,girl_lat,girl_lon):
    base_url = f"https://api.vedicastroapi.com/v3-json/matching/{match_type}"
    params = {
        "boy_dob": boy_dob,
        "boy_tob": boy_tob,
        "boy_lat": boy_lat,
        "boy_lon": boy_lon,
        "boy_tz": 5.5,
        "girl_dob": girl_dob,
        "girl_tob": girl_tob,
        "girl_lat": girl_lat,
        "girl_lon": girl_lon,
        "girl_tz": 5.5,
        "api_key": ASTRO_API_KEY,
        "lang": "en"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises HTTPError for 4xx and 5xx responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error calling {match_type.replace('-', ' ').capitalize()} API: {e}")
        return None
    
def get_ashtakoot_match(boy_dob,boy_tob,boy_lat,boy_lon,girl_dob,girl_tob,girl_lat,girl_lon):
    return  astro_match("ashtakoot",boy_dob,boy_tob,boy_lat,boy_lon,girl_dob,girl_tob,girl_lat,girl_lon)
def get_dashakoot_match(boy_dob,boy_tob,boy_lat,boy_lon,girl_dob,girl_tob,girl_lat,girl_lon):
    return astro_match("dashakoot",boy_dob,boy_tob,boy_lat,boy_lon,girl_dob,girl_tob,girl_lat,girl_lon)
def get_dashakoot_with_astro_details(boy_dob,boy_tob,boy_lat,boy_lon,girl_dob,girl_tob,girl_lat,girl_lon):
    return astro_match("dashakoot-with-astro-details",boy_dob,boy_tob,boy_lat,boy_lon,girl_dob,girl_tob,girl_lat,girl_lon)
def get_ashtakoot_with_astro_details(boy_dob,boy_tob,boy_lat,boy_lon,girl_dob,girl_tob,girl_lat,girl_lon):
    return astro_match("ashtakoot-with-astro-details",boy_dob,boy_tob,boy_lat,boy_lon,girl_dob,girl_tob,girl_lat,girl_lon)
def get_aggregate_match(boy_dob,boy_tob,boy_lat,boy_lon,girl_dob,girl_tob,girl_lat,girl_lon):
    return astro_match("aggregate-match",boy_dob,boy_tob,boy_lat,boy_lon,girl_dob,girl_tob,girl_lat,girl_lon)
def get_rajju_vedha_details(boy_dob,boy_tob,boy_lat,boy_lon,girl_dob,girl_tob,girl_lat,girl_lon):
    return astro_match("rajju-vedha-details",boy_dob,boy_tob,boy_lat,boy_lon,girl_dob,girl_tob,girl_lat,girl_lon)
def get_papasamaya_match(boy_dob,boy_tob,boy_lat,boy_lon,girl_dob,girl_tob,girl_lat,girl_lon):
    return astro_match("papasamaya-match",boy_dob,boy_tob,boy_lat,boy_lon,girl_dob,girl_tob,girl_lat,girl_lon)
def get_nakshatra_match(boy_dob,boy_tob,boy_lat,boy_lon,girl_dob,girl_tob,girl_lat,girl_lon):
    return astro_match("nakshatra-match",boy_dob,boy_tob,boy_lat,boy_lon,girl_dob,girl_tob,girl_lat,girl_lon)

def panchang(panch_type,date,time,lat,lon):
    base_url = f"https://api.vedicastroapi.com/v3-json/panchang/{panch_type}"
    params = {
        "date": date,
        "tob": time,
        "lat": lat,
        "lon": lon,
        "tz": 5.5,
        "api_key": ASTRO_API_KEY,
        "lang": "en"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises HTTPError for 4xx and 5xx responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error calling {panch_type.replace('-', ' ').capitalize()} API: {e}")
        return None
def get_panchang(date,time,lat,lon):
    return panchang("panchang",date,time,lat,lon)
def get_monthly_panchang(date,time,lat,lon):
    return panchang("monthly-panchang",date,time,lat,lon)
def get_choghadiya_muhurta(date,time,lat,lon):
    return panchang("choghadiya-muhurta",date,time,lat,lon)
def get_moon_calendar(date):
    base_url = f"https://api.vedicastroapi.com/v3-json/panchang/moon-calendar"
    params = {
        "date": date,
        "tz": 5.5,
        "api_key": ASTRO_API_KEY,
        "lang": "en"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises HTTPError for 4xx and 5xx responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error calling API: {e}")
        return None
def get_moon_phase(date):
    base_url = f"https://api.vedicastroapi.com/v3-json/panchang/moon-phase"
    params = {
        "date": date,
        "tz": 5.5,
        "api_key": ASTRO_API_KEY,
        "lang": "en"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises HTTPError for 4xx and 5xx responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error calling API: {e}")
        return None
   
def get_moon_rise(date,time,lat,lon):
    return panchang("moonrise",date,time,lat,lon)
def get_hora_muhurta(date,time,lat,lon):
    return panchang("hora-muhurta",date,time,lat,lon)
def get_moon_set(date,time,lat,lon):
    return panchang("moonset",date,time,lat,lon)
def get_solar_noon(date,time,lat,lon):
    return panchang("solarnoon",date,time,lat,lon)
def get_sun_rise(date,time,lat,lon):
    return panchang("sunrise",date,time,lat,lon)
def get_sun_set(date,time,lat,lon):
    return panchang("sunset",date,time,lat,lon)
def get_retrogrades(year,planet):
    base_url = f"https://api.vedicastroapi.com/v3-json/panchang/retrogrades"
    params = {
        "year": year,
        "planet": planet,
        "api_key": ASTRO_API_KEY,
        "lang": "en"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises HTTPError for 4xx and 5xx responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error calling API: {e}")
        return None
    
#predictions
def get_daily(typ,zodic,date):
    base_url = f"https://api.vedicastroapi.com/v3-json/prediction/{typ}"
    params = {
        "zodic": zodic,
        "date": date,
        "api_key": ASTRO_API_KEY,
        "lang": "en",
        "show_same":"true"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises HTTPError for 4xx and 5xx responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error calling API: {e}")
        return None
    
def get_daily_sun(zodic,date):
    return get_daily('daily-sun',zodic,date,split='true',type='big')
def get_daily_moon(zodic,date):
    return get_daily('daily-moon',zodic,date)
def get_week(typ1,zodic,week):
    base_url = f"https://api.vedicastroapi.com/v3-json/prediction/{typ1}"
    params = {
        "zodic": zodic,
        "week": week,
        "api_key": ASTRO_API_KEY,
        "lang": "en",
        "show_same":"true"

    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises HTTPError for 4xx and 5xx responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error calling API: {e}")
        return None
def get_weekly_sun(zodic,week):
    return get_week('weekly-sun',zodic,week)
def get_weekly_moon(zodic,week):
    return get_week('weekly-moon',zodic,week)
def get_daily_nakshatra(nakshatra,date):
    base_url = f"https://api.vedicastroapi.com/v3-json/prediction/daily-nakshatra"
    params = {
        "nakshatra": nakshatra,
        "date": date,
        "api_key": ASTRO_API_KEY,
        "lang": "en",
        "show_same":"true"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises HTTPError for 4xx and 5xx responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error calling API: {e}")
        return None
def get_yearly(year,zodiac):
    base_url = f"https://api.vedicastroapi.com/v3-json/prediction/yearly"
    params = {
        "year": year,
        "zodiac": zodiac,
        "api_key": ASTRO_API_KEY,
        "lang": "en"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises HTTPError for 4xx and 5xx responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error calling API: {e}")
        return None
def get_biorythm(dob):
    base_url = f"https://api.vedicastroapi.com/v3-json/prediction/biorhythm"
    params = {
        "dob": dob,
        "api_key": ASTRO_API_KEY,
        "lang": "en",
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises HTTPError for 4xx and 5xx responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error calling API: {e}")
        return None
    
def get_gem_details(gem):
    base_url = f"https://api.vedicastroapi.com/v3-json/utilities/gem-details"
    params = {
        "gem": gem,
        "api_key": ASTRO_API_KEY,
        "lang": "en",
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises HTTPError for 4xx and 5xx responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error calling API: {e}")
        return None
def get_nakshatra_vastu_details(nakshatra):
    base_url = f"https://api.vedicastroapi.com/v3-json/utilities/nakshatra-vastu-details"
    params = {
        "nakshatra": nakshatra,
        "api_key": ASTRO_API_KEY,
        "lang": "en",
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises HTTPError for 4xx and 5xx responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error calling API: {e}")
        return None
