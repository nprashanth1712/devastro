from flask import Flask, request, jsonify, Response
from openai import OpenAI
import requests
import os
import time
from dotenv import load_dotenv
#from newtools_v1 import tools
#from functions2_v1 import *
from werkzeug.exceptions import BadRequest, InternalServerError
import json
import base64
import logging

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_mangal_dosh_api",
            "description": "Fetches Mangal Dosh details based on birth information.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dob": {
                        "type": "string",
                        "description": "Date of Birth - DD/MM/YYYY"
                    },
                    "tob": {
                        "type": "string",
                        "description": "Time of Birth - HH:MM"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude with decimals"
                    }
                },
                "required": ["dob", "tob", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_kaalsarp_dosh_api",
            "description": "Retrieves Kaalsarp Dosh information based on birth details.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dob": {
                        "type": "string",
                        "description": "Date of Birth - DD/MM/YYYY"
                    },
                    "tob": {
                        "type": "string",
                        "description": "Time of Birth - HH:MM"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude with decimals"
                    }
                },
                "required": ["dob", "tob", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_manglik_dosh_api",
            "description": "Fetches Manglik Dosh details based on birth information.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dob": {
                        "type": "string",
                        "description": "Date of Birth - DD/MM/YYYY"
                    },
                    "tob": {
                        "type": "string",
                        "description": "Time of Birth - HH:MM"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude with decimals"
                    }
                },
                "required": ["dob", "tob", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_pitra_dosh_api",
            "description": "Retrieves Pitra Dosh information based on birth details.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dob": {
                        "type": "string",
                        "description": "Date of Birth - DD/MM/YYYY"
                    },
                    "tob": {
                        "type": "string",
                        "description": "Time of Birth - HH:MM"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude with decimals"
                    }
                },
                "required": ["dob", "tob", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_papasamaya_api",
            "description": "Fetches Papasamaya details based on birth information.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dob": {
                        "type": "string",
                        "description": "Date of Birth - DD/MM/YYYY"
                    },
                    "tob": {
                        "type": "string",
                        "description": "Time of Birth - HH:MM"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude with decimals"
                    }
                },
                "required": ["dob", "tob", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_mahadasha_api",
            "description": "Retrieves Mahadasha information based on birth details.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dob": {
                        "type": "string",
                        "description": "Date of Birth - DD/MM/YYYY"
                    },
                    "tob": {
                        "type": "string",
                        "description": "Time of Birth - HH:MM"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude with decimals"
                    }
                },
                "required": ["dob", "tob", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_mahadasha_predictions_api",
            "description": "Provides Mahadasha predictions based on birth details.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dob": {
                        "type": "string",
                        "description": "Date of Birth - DD/MM/YYYY"
                    },
                    "tob": {
                        "type": "string",
                        "description": "Time of Birth - HH:MM"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude with decimals"
                    }
                },
                "required": ["dob", "tob", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_antardasha_api",
            "description": "Fetches Antardasha details based on birth details.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dob": {
                        "type": "string",
                        "description": "Date of Birth - DD/MM/YYYY"
                    },
                    "tob": {
                        "type": "string",
                        "description": "Time of Birth - HH:MM"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude with decimals"
                    }
                },
                "required": ["dob", "tob", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_char_dasha_current",
            "description": "Fetches current Char Dasha data based on birth details.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dob": {
                        "type": "string",
                        "description": "Date of Birth - DD/MM/YYYY"
                    },
                    "tob": {
                        "type": "string",
                        "description": "Time of Birth - HH:MM"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude with decimals"
                    }
                },
                "required": ["dob", "tob", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_char_dasha_main",
            "description": "Fetches main periods of Char Dasha based on birth details.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dob": {
                        "type": "string",
                        "description": "Date of Birth - DD/MM/YYYY"
                    },
                    "tob": {
                        "type": "string",
                        "description": "Time of Birth - HH:MM"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude with decimals"
                    }
                },
                "required": ["dob", "tob", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_current_mahadasha",
            "description": "Fetches details of the current Mahadasha based on birth details.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dob": {
                        "type": "string",
                        "description": "Date of Birth - DD/MM/YYYY"
                    },
                    "tob": {
                        "type": "string",
                        "description": "Time of Birth - HH:MM"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude with decimals"
                    }
                },
                "required": ["dob", "tob", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_yogini_dasha_main",
            "description": "Fetches main periods of Yogini Dasha based on birth details.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dob": {
                        "type": "string",
                        "description": "Date of Birth - DD/MM/YYYY"
                    },
                    "tob": {
                        "type": "string",
                        "description": "Time of Birth - HH:MM"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude with decimals"
                    }
                },
                "required": ["dob", "tob", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_char_dasha_sub",
            "description": "Fetches sub-periods of Char Dasha based on birth details.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dob": {
                        "type": "string",
                        "description": "Date of Birth - DD/MM/YYYY"
                    },
                    "tob": {
                        "type": "string",
                        "description": "Time of Birth - HH:MM"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude with decimals"
                    }
                },
                "required": ["dob", "tob", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_current_mahadasha_full",
            "description": "Fetches comprehensive details of the current Mahadasha, including sub-periods, based on birth details.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dob": {
                        "type": "string",
                        "description": "Date of Birth - DD/MM/YYYY"
                    },
                    "tob": {
                        "type": "string",
                        "description": "Time of Birth - HH:MM"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude with decimals"
                    }
                },
                "required": ["dob", "tob", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_paryantar_dasha",
            "description": "Fetches Paryantar Dasha details, offering precise predictions within a specific phase of an individual's life.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dob": {
                        "type": "string",
                        "description": "Date of Birth - DD/MM/YYYY"
                    },
                    "tob": {
                        "type": "string",
                        "description": "Time of Birth - HH:MM"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude with decimals"
                    }
                },
                "required": ["dob", "tob", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_specific_dasha",
            "description": "Fetches detailed predictions for a specific Dasha period based on the combination of major, minor, sub-minor, and sub-sub-minor periods.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dob": {
                        "type": "string",
                        "description": "Date of Birth - DD/MM/YYYY"
                    },
                    "tob": {
                        "type": "string",
                        "description": "Time of Birth - HH:MM"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude with decimals"
                    },
                    "md": {
                        "type": "string",
                        "description": "Main Dasha planet"
                    },
                    "ad": {
                        "type": "string",
                        "description": "Antardasha planet"
                    },
                    "pd": {
                        "type": "string",
                        "description": "Pratyantardasha planet"
                    },
                    "sd": {
                        "type": "string",
                        "description": "Sookshmadasha planet"
                    }
                },
                "required": ["dob", "tob", "lat", "lon", "md", "ad", "pd", "sd"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "find_moon_sign",
            "description": "Fetches the Moon sign based on birth details.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dob": {
                        "type": "string",
                        "description": "Date of Birth - DD/MM/YYYY"
                    },
                    "tob": {
                        "type": "string",
                        "description": "Time of Birth - HH:MM"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude with decimals"
                    }
                },
                "required": ["dob", "tob", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "find_sun_sign",
            "description": "Fetches the Sun sign based on birth details.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dob": {
                        "type": "string",
                        "description": "Date of Birth - DD/MM/YYYY"
                    },
                    "tob": {
                        "type": "string",
                        "description": "Time of Birth - HH:MM"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude with decimals"
                    }
                },
                "required": ["dob", "tob", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "find_ascendant",
            "description": "Fetches the Ascendant sign based on birth details.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dob": {
                        "type": "string",
                        "description": "Date of Birth - DD/MM/YYYY"
                    },
                    "tob": {
                        "type": "string",
                        "description": "Time of Birth - HH:MM"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude with decimals"
                    }
                },
                "required": ["dob", "tob", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "current_sade_sati",
            "description": "Fetches the current Sade Sati period based on birth details.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dob": {
                        "type": "string",
                        "description": "Date of Birth - DD/MM/YYYY"
                    },
                    "tob": {
                        "type": "string",
                        "description": "Time of Birth - HH:MM"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude with decimals"
                    }
                },
                "required": ["dob", "tob", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "extended_kundli_details",
            "description": "Fetches extended Kundli details based on birth details.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dob": {
                        "type": "string",
                        "description": "Date of Birth - DD/MM/YYYY"
                    },
                    "tob": {
                        "type": "string",
                        "description": "Time of Birth - HH:MM"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude with decimals"
                    }
                },
                "required": ["dob", "tob", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "sade_sati_table",
            "description": "Fetches the Sade Sati table based on birth details.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dob": {
                        "type": "string",
                        "description": "Date of Birth - DD/MM/YYYY"
                    },
                    "tob": {
                        "type": "string",
                        "description": "Time of Birth - HH:MM"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude with decimals"
                    }
                },
                "required": ["dob", "tob", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "friendship_table",
            "description": "Fetches the Friendship table based on birth details.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dob": {
                        "type": "string",
                        "description": "Date of Birth - DD/MM/YYYY"
                    },
                    "tob": {
                        "type": "string",
                        "description": "Time of Birth - HH:MM"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude with decimals"
                    }
                },
                "required": ["dob", "tob", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "kp_houses",
            "description": "Fetches KP-Houses based on birth details.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dob": {
                        "type": "string",
                        "description": "Date of Birth - DD/MM/YYYY"
                    },
                    "tob": {
                        "type": "string",
                        "description": "Time of Birth - HH:MM"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude with decimals"
                    }
                },
                "required": ["dob", "tob", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "kp_planets",
            "description": "Fetches KP-Planets based on birth details.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dob": {
                        "type": "string",
                        "description": "Date of Birth - DD/MM/YYYY"
                    },
                    "tob": {
                        "type": "string",
                        "description": "Time of Birth - HH:MM"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude with decimals"
                    }
                },
                "required": ["dob", "tob", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "gem_suggestion",
            "description": "Fetches Gemstone suggestions based on birth details.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dob": {
                        "type": "string",
                        "description": "Date of Birth - DD/MM/YYYY"
                    },
                    "tob": {
                        "type": "string",
                        "description": "Time of Birth - HH:MM"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude with decimals"
                    }
                },
                "required": ["dob", "tob", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "rudraksh_suggestion",
            "description": "Fetches Rudraksh suggestions based on birth details.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dob": {
                        "type": "string",
                        "description": "Date of Birth - DD/MM/YYYY"
                    },
                    "tob": {
                        "type": "string",
                        "description": "Time of Birth - HH:MM"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude with decimals"
                    }
                },
                "required": ["dob", "tob", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "varshapal_details",
            "description": "Fetches Varshapal details for the year based on birth details.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dob": {
                        "type": "string",
                        "description": "Date of Birth - DD/MM/YYYY"
                    },
                    "tob": {
                        "type": "string",
                        "description": "Time of Birth - HH:MM"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude with decimals"
                    }
                },
                "required": ["dob", "tob", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "varshapal_month_chart",
            "description": "Fetches Varshapal month chart based on birth details.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dob": {
                        "type": "string",
                        "description": "Date of Birth - DD/MM/YYYY"
                    },
                    "tob": {
                        "type": "string",
                        "description": "Time of Birth - HH:MM"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude with decimals"
                    }
                },
                "required": ["dob", "tob", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "varshapal_year_chart",
            "description": "Fetches Varshapal year chart based on birth details.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dob": {
                        "type": "string",
                        "description": "Date of Birth - DD/MM/YYYY"
                    },
                    "tob": {
                        "type": "string",
                        "description": "Time of Birth - HH:MM"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude with decimals"
                    }
                },
                "required": ["dob", "tob", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_planet_details",
            "description": "Fetches details of planets based on birth details.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dob": {
                        "type": "string",
                        "description": "Date of Birth - DD/MM/YYYY"
                    },
                    "tob": {
                        "type": "string",
                        "description": "Time of Birth - HH:MM"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude with decimals"
                    }
                },
                "required": ["dob", "tob", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_ascendant_report",
            "description": "Provides insights into personality, appearance, and life approach based on the ascendant sign.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dob": {
                        "type": "string",
                        "description": "Date of Birth - DD/MM/YYYY"
                    },
                    "tob": {
                        "type": "string",
                        "description": "Time of Birth - HH:MM"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude with decimals"
                    }
                },
                "required": ["dob", "tob", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_planet_report",
            "description": "Detailed analysis of positions and influences of planets in a birth chart.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dob": {
                        "type": "string",
                        "description": "Date of Birth - DD/MM/YYYY"
                    },
                    "tob": {
                        "type": "string",
                        "description": "Time of Birth - HH:MM"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude with decimals"
                    },
                    "planet": {
                        "type": "string",
                        "description": "Planet for report",
                        "enum": [
                            "Sun",
                            "Moon",
                            "Mercury",
                            "Venus",
                            "Mars",
                            "Saturn",
                            "Jupiter",
                            "Rahu",
                            "Ketu"
                        ]
                    }
                },
                "required": ["dob", "tob", "lat", "lon", "planet"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_personal_characteristics",
            "description": "Determines traits and qualities from a birth chart.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dob": {
                        "type": "string",
                        "description": "Date of Birth - DD/MM/YYYY"
                    },
                    "tob": {
                        "type": "string",
                        "description": "Time of Birth - HH:MM"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude with decimals"
                    }
                },
                "required": ["dob", "tob", "lat", "lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_ashtakoot_match",
            "description": "Calculates compatibility based on the Ashtakoot system for a boy and girl.",
            "parameters": {
                "type": "object",
                "properties": {
                    "boy_dob": {
                        "type": "string",
                        "description": "Boy's Date of Birth - DD/MM/YYYY"
                    },
                    "boy_tob": {
                        "type": "string",
                        "description": "Boy's Time of Birth - HH:MM"
                    },
                    "boy_lat": {
                        "type": "number",
                        "description": "Boy's Latitude with decimals"
                    },
                    "boy_lon": {
                        "type": "number",
                        "description": "Boy's Longitude with decimals"
                    },
                    "girl_dob": {
                        "type": "string",
                        "description": "Girl's Date of Birth - DD/MM/YYYY"
                    },
                    "girl_tob": {
                        "type": "string",
                        "description": "Girl's Time of Birth - HH:MM"
                    },
                    "girl_lat": {
                        "type": "number",
                        "description": "Girl's Latitude with decimals"
                    },
                    "girl_lon": {
                        "type": "number",
                        "description": "Girl's Longitude with decimals"
                    }
                },
                "required": ["boy_dob", "boy_tob", "boy_lat", "boy_lon", "girl_dob", "girl_tob", "girl_lat", "girl_lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_ashtakoot_with_astro_details",
            "description": "Calculates Ashtakoot match score with detailed astrological information for both boy and girl.",
            "parameters": {
                "type": "object",
                "properties": {
                    "boy_dob": {
                        "type": "string",
                        "description": "Boy's Date of Birth - DD/MM/YYYY"
                    },
                    "boy_tob": {
                        "type": "string",
                        "description": "Boy's Time of Birth - HH:MM"
                    },
                    "boy_lat": {
                        "type": "number",
                        "description": "Boy's Latitude with decimals"
                    },
                    "boy_lon": {
                        "type": "number",
                        "description": "Boy's Longitude with decimals"
                    },
                    "girl_dob": {
                        "type": "string",
                        "description": "Girl's Date of Birth - DD/MM/YYYY"
                    },
                    "girl_tob": {
                        "type": "string",
                        "description": "Girl's Time of Birth - HH:MM"
                    },
                    "girl_lat": {
                        "type": "number",
                        "description": "Girl's Latitude with decimals"
                    },
                    "girl_lon": {
                        "type": "number",
                        "description": "Girl's Longitude with decimals"
                    }
                },
                "required": ["boy_dob", "boy_tob", "boy_lat", "boy_lon", "girl_dob", "girl_tob", "girl_lat", "girl_lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_dashakoot_match",
            "description": "Calculates compatibility based on the Dashakoot system for a boy and girl.",
            "parameters": {
                "type": "object",
                "properties": {
                    "boy_dob": {
                        "type": "string",
                        "description": "Boy's Date of Birth - DD/MM/YYYY"
                    },
                    "boy_tob": {
                        "type": "string",
                        "description": "Boy's Time of Birth - HH:MM"
                    },
                    "boy_lat": {
                        "type": "number",
                        "description": "Boy's Latitude with decimals"
                    },
                    "boy_lon": {
                        "type": "number",
                        "description": "Boy's Longitude with decimals"
                    },
                    "girl_dob": {
                        "type": "string",
                        "description": "Girl's Date of Birth - DD/MM/YYYY"
                    },
                    "girl_tob": {
                        "type": "string",
                        "description": "Girl's Time of Birth - HH:MM"
                    },
                    "girl_lat": {
                        "type": "number",
                        "description": "Girl's Latitude with decimals"
                    },
                    "girl_lon": {
                        "type": "number",
                        "description": "Girl's Longitude with decimals"
                    }
                },
                "required": ["boy_dob", "boy_tob", "boy_lat", "boy_lon", "girl_dob", "girl_tob", "girl_lat", "girl_lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_dashakoot_with_astro_details",
            "description": "Calculates Dashakoot match score including detailed astrological insights for both individuals.",
            "parameters": {
                "type": "object",
                "properties": {
                    "boy_dob": {
                        "type": "string",
                        "description": "Boy's Date of Birth - DD/MM/YYYY"
                    },
                    "boy_tob": {
                        "type": "string",
                        "description": "Boy's Time of Birth - HH:MM"
                    },
                    "boy_lat": {
                        "type": "number",
                        "description": "Boy's Latitude with decimals"
                    },
                    "boy_lon": {
                        "type": "number",
                        "description": "Boy's Longitude with decimals"
                    },
                    "girl_dob": {
                        "type": "string",
                        "description": "Girl's Date of Birth - DD/MM/YYYY"
                    },
                    "girl_tob": {
                        "type": "string",
                        "description": "Girl's Time of Birth - HH:MM"
                    },
                    "girl_lat": {
                        "type": "number",
                        "description": "Girl's Latitude with decimals"
                    },
                    "girl_lon": {
                        "type": "number",
                        "description": "Girl's Longitude with decimals"
                    }
                },
                "required": ["boy_dob", "boy_tob", "boy_lat", "boy_lon", "girl_dob", "girl_tob", "girl_lat", "girl_lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_aggregate_match",
            "description": "Provides an aggregate compatibility score combining various astrological factors.",
            "parameters": {
                "type": "object",
                "properties": {
                    "boy_dob": {
                        "type": "string",
                        "description": "Boy's Date of Birth - DD/MM/YYYY"
                    },
                    "boy_tob": {
                        "type": "string",
                        "description": "Boy's Time of Birth - HH:MM"
                    },
                    "boy_lat": {
                        "type": "number",
                        "description": "Boy's Latitude with decimals"
                    },
                    "boy_lon": {
                        "type": "number",
                        "description": "Boy's Longitude with decimals"
                    },
                    "girl_dob": {
                        "type": "string",
                        "description": "Girl's Date of Birth - DD/MM/YYYY"
                    },
                    "girl_tob": {
                        "type": "string",
                        "description": "Girl's Time of Birth - HH:MM"
                    },
                    "girl_lat": {
                        "type": "number",
                        "description": "Girl's Latitude with decimals"
                    },
                    "girl_lon": {
                        "type": "number",
                        "description": "Girl's Longitude with decimals"
                    }
                },
                "required": ["boy_dob", "boy_tob", "boy_lat", "boy_lon", "girl_dob", "girl_tob", "girl_lat", "girl_lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_rajju_vedha_details",
            "description": "Analyzes the presence of Rajju and Vedha doshas in the match, crucial for assessing marital harmony.",
            "parameters": {
                "type": "object",
                "properties": {
                    "boy_dob": {
                        "type": "string",
                        "description": "Boy's Date of Birth - DD/MM/YYYY"
                    },
                    "boy_tob": {
                        "type": "string",
                        "description": "Boy's Time of Birth - HH:MM"
                    },
                    "boy_lat": {
                        "type": "number",
                        "description": "Boy's Latitude with decimals"
                    },
                    "boy_lon": {
                        "type": "number",
                        "description": "Boy's Longitude with decimals"
                    },
                    "girl_dob": {
                        "type": "string",
                        "description": "Girl's Date of Birth - DD/MM/YYYY"
                    },
                    "girl_tob": {
                        "type": "string",
                        "description": "Girl's Time of Birth - HH:MM"
                    },
                    "girl_lat": {
                        "type": "number",
                        "description": "Girl's Latitude with decimals"
                    },
                    "girl_lon": {
                        "type": "number",
                        "description": "Girl's Longitude with decimals"
                    }
                },
                "required": ["boy_dob", "boy_tob", "boy_lat", "boy_lon", "girl_dob", "girl_tob", "girl_lat", "girl_lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_papasamaya_match",
            "description": "Evaluates the compatibility by comparing the malefic impacts (Papasamya) in both charts.",
            "parameters": {
                "type": "object",
                "properties": {
                    "boy_dob": {
                        "type": "string",
                        "description": "Boy's Date of Birth - DD/MM/YYYY"
                    },
                    "boy_tob": {
                        "type": "string",
                        "description": "Boy's Time of Birth - HH:MM"
                    },
                    "boy_lat": {
                        "type": "number",
                        "description": "Boy's Latitude with decimals"
                    },
                    "boy_lon": {
                        "type": "number",
                        "description": "Boy's Longitude with decimals"
                    },
                    "girl_dob": {
                        "type": "string",
                        "description": "Girl's Date of Birth - DD/MM/YYYY"
                    },
                    "girl_tob": {
                        "type": "string",
                        "description": "Girl's Time of Birth - HH:MM"
                    },
                    "girl_lat": {
                        "type": "number",
                        "description": "Girl's Latitude with decimals"
                    },
                    "girl_lon": {
                        "type": "number",
                        "description": "Girl's Longitude with decimals"
                    }
                },
                "required": ["boy_dob", "boy_tob", "boy_lat", "boy_lon", "girl_dob", "girl_tob", "girl_lat", "girl_lon"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_nakshatra_match",
            "description": "Calculates compatibility based on the Nakshatra (Star) match system.",
            "parameters": {
                "type": "object",
                "properties": {
                    "boy_star": {
                        "type": "number",
                        "description": "Boy's Nakshatra number, 1 for Ashvini to 27 for Revati"
                    },
                    "girl_star": {
                        "type": "number",
                        "description": "Girl's Nakshatra number, 1 for Ashvini to 27 for Revati"
                    }
                },
                "required": ["boy_star", "girl_star"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_panchang",
            "description": "Retrieves Panchang details for a specific date, time, and location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "date": {
                        "type": "string",
                        "description": "Date in DD/MM/YYYY format"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude in decimals"
                    },
                    "time": {
                        "type": "string",
                        "description": "Time in HH:MM format"
                    }
                },
                "required": ["date", "lat", "lon", "time"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_monthly_panchang",
            "description": "Retrieves monthly Panchang details for a specific date, time, and location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "date": {
                        "type": "string",
                        "description": "Start date in DD/MM/YYYY format"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude in decimals"
                    },
                    "time": {
                        "type": "string",
                        "description": "Time in HH:MM format"
                    }
                },
                "required": ["date", "lat", "lon", "time"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_choghadiya_muhurta",
            "description": "Retrieves Choghadiya Muhurta details for a specific date, time, and location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "date": {
                        "type": "string",
                        "description": "Date in DD/MM/YYYY format"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude in decimals"
                    },
                    "time": {
                        "type": "string",
                        "description": "Time in HH:MM format"
                    }
                },
                "required": ["date", "lat", "lon", "time"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_hora_muhurta",
            "description": "Retrieves Hora Muhurta details for a specific date, time, and location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "date": {
                        "type": "string",
                        "description": "Date in DD/MM/YYYY format"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude in decimals"
                    },
                    "time": {
                        "type": "string",
                        "description": "Time in HH:MM format"
                    }
                },
                "required": ["date", "lat", "lon", "time"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_moon_calendar",
            "description": "Retrieves Moon Calendar details for a specific date and time zone.",
            "parameters": {
                "type": "object",
                "properties": {
                    "date": {
                        "type": "string",
                        "description": "Date in DD/MM/YYYY format"
                    }
                },
                "required": ["date"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_moon_phase",
            "description": "Retrieves Moon Phase details for a specific date and time zone.",
            "parameters": {
                "type": "object",
                "properties": {
                    "date": {
                        "type": "string",
                        "description": "Date in DD/MM/YYYY format"
                    }
                },
                "required": ["date"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_moon_rise",
            "description": "Retrieves Moon Rise details for a specific date, time, and location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "date": {
                        "type": "string",
                        "description": "Date in DD/MM/YYYY format"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude in decimals"
                    },
                    "time": {
                        "type": "string",
                        "description": "Time in HH:MM format"
                    }
                },
                "required": ["date", "lat", "lon", "time"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_moon_set",
            "description": "Retrieves Moon Set details for a specific date, time, and location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "date": {
                        "type": "string",
                        "description": "Date in DD/MM/YYYY format"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude in decimals"
                    },
                    "time": {
                        "type": "string",
                        "description": "Time in HH:MM format"
                    }
                },
                "required": ["date", "lat", "lon", "time"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_solar_noon",
            "description": "Retrieves Solar Noon details for a specific date, time, and location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "date": {
                        "type": "string",
                        "description": "Date in DD/MM/YYYY format"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude in decimals"
                    },
                    "time": {
                        "type": "string",
                        "description": "Time in HH:MM format"
                    }
                },
                "required": ["date", "lat", "lon", "time"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_sun_rise",
            "description": "Retrieves Sun Rise details for a specific date, time, and location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "date": {
                        "type": "string",
                        "description": "Date in DD/MM/YYYY format"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude in decimals"
                    },
                    "time": {
                        "type": "string",
                        "description": "Time in HH:MM format"
                    }
                },
                "required": ["date", "lat", "lon", "time"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_sun_set",
            "description": "Retrieves Sun Set details for a specific date, time, and location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "date": {
                        "type": "string",
                        "description": "Date in DD/MM/YYYY format"
                    },
                    "lat": {
                        "type": "number",
                        "description": "Latitude with decimals"
                    },
                    "lon": {
                        "type": "number",
                        "description": "Longitude in decimals"
                    },
                    "time": {
                        "type": "string",
                        "description": "Time in HH:MM format"
                    }
                },
                "required": ["date", "lat", "lon", "time"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_retrogrades",
            "description": "Retrieves Retrograde details for a specific year and planet.",
            "parameters": {
                "type": "object",
                "properties": {
                    "year": {
                        "type": "number",
                        "description": "Year till 2799"
                    },
                    "planet": {
                        "type": "string",
                        "description": "Planet name (Sun, Moon, Mercury, Venus, Mars, Saturn, Jupiter, Rahu, Ketu)"
                    }
                },
                "required": ["year", "planet"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_daily_sun",
            "description": "Retrieves daily sun predictions for a specific zodiac sign and date.",
            "parameters": {
                "type": "object",
                "properties": {
                    "zodiac": {
                        "type": "number",
                        "description": "Zodiac sign number (1-12)"
                    },
                    "date": {
                        "type": "string",
                        "description": "Date in DD/MM/YYYY format"
                    },
                    "split": {
                        "type": "boolean",
                        "description": "If true, splits the response"
                    }
                },
                "required": ["zodiac", "date"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_daily_moon",
            "description": "Retrieves daily moon predictions for a specific zodiac sign and date.",
            "parameters": {
                "type": "object",
                "properties": {
                    "zodiac": {
                        "type": "number",
                        "description": "Zodiac sign number (1-12)"
                    },
                    "date": {
                        "type": "string",
                        "description": "Date in DD/MM/YYYY format"
                    },
                    "type": {
                        "type": "string",
                        "description": "Type of prediction (big/small)",
                        "enum": ["big", "small"],
                        "default": "small"
                    }
                },
                "required": ["zodiac", "date"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_daily_nakshatra",
            "description": "Retrieves daily nakshatra predictions for a specific nakshatra and date.",
            "parameters": {
                "type": "object",
                "properties": {
                    "nakshatra": {
                        "type": "number",
                        "description": "Nakshatra number (1-27)"
                    },
                    "date": {
                        "type": "string",
                        "description": "Date in DD/MM/YYYY format"
                    }
                },
                "required": ["nakshatra", "date"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_weekly_moon",
            "description": "Retrieves weekly moon predictions for a specific zodiac sign and week.",
            "parameters": {
                "type": "object",
                "properties": {
                    "zodiac": {
                        "type": "number",
                        "description": "Zodiac sign number (1-12)"
                    },
                    "week": {
                        "type": "string",
                        "description": "Week in DD/MM/YYYY format"
                    }
                },
                "required": ["zodiac", "week"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_weekly_sun",
            "description": "Retrieves weekly sun predictions for a specific zodiac sign and week.",
            "parameters": {
                "type": "object",
                "properties": {
                    "zodiac": {
                        "type": "number",
                        "description": "Zodiac sign number (1-12)"
                    },
                    "week": {
                        "type": "string",
                        "description": "Week in DD/MM/YYYY format"
                    }
                },
                "required": ["zodiac", "week"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_yearly",
            "description": "Retrieves yearly predictions for a specific zodiac sign.",
            "parameters": {
                "type": "object",
                "properties": {
                    "zodiac": {
                        "type": "number",
                        "description": "Zodiac sign number (1-12)"
                    },
                    "year": {
                        "type": "string",
                        "description": "Year in YYYY format"
                    }
                },
                "required": ["zodiac", "year"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_biorythm",
            "description": "Retrieves biorythm details for a specific date of birth and target date.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dob": {
                        "type": "string",
                        "description": "Date of birth in DD/MM/YYYY format"
                    },
                    "target_date": {
                        "type": "string",
                        "description": "Target date in DD/MM/YYYY format"
                    }
                },
                "required": ["dob", "target_date"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_gem_details",
            "description": "Retrieves details about a specific gem.",
            "parameters": {
                "type": "object",
                "properties": {
                    "gem": {
                        "type": "string",
                        "description": "Name of the gem (e.g., coral, diamond, ruby)"
                    }
                },
                "required": ["gem"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_nakshatra_vastu_details",
            "description": "Retrieves vastu details for a specific nakshatra.",
            "parameters": {
                "type": "object",
                "properties": {
                    "nakshatra": {
                        "type": "number",
                        "description": "Nakshatra number (1-27)"
                    }
                },
                "required": ["nakshatra"]
            }
        }
    }
]



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
def get_daily_sun(zodiac,date):
    base_url = f"https://api.vedicastroapi.com/v3-json/prediction/daily-sun"
    params = {
        "zodiac": zodiac,
        "date": date,
        "api_key": ASTRO_API_KEY,
        "lang": "en",
        "split": "true",
        "type":"big",
        "show_same":"true"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises HTTPError for 4xx and 5xx responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error calling API: {e}")
        return None
def get_daily_moon(zodiac,date):
    base_url = f"https://api.vedicastroapi.com/v3-json/prediction/daily-moon"
    params = {
        "zodiac": zodiac,
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


def get_week(typ1,zodiac,week):
    base_url = f"https://api.vedicastroapi.com/v3-json/prediction/{typ1}"
    params = {
        "zodiac": zodiac,
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
def get_weekly_sun(zodiac,week):
    return get_week('weekly-sun',zodiac,week)
def get_weekly_moon(zodiac,week):
    return get_week('weekly-moon',zodiac,week)
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






load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError('OPENAI_API_KEY environment variable not set')

client = OpenAI(api_key=api_key)
ASTRO_API_KEY = os.getenv('ASTRO_API_KEY', 'dfa2b8e6-d4f5-584a-b08c-e0a1e0150047')

logging.basicConfig(level=logging.INFO)

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


@app.route('/', methods=['POST'])

app = Flask(__name__)

def handle_query():
    try:
        data = request.json
        # Validate input data
        if not data or 'query' not in data:
            raise BadRequest('No query provided')
        user_query = data['query']
        response = your_main_function(user_query)
        return Response(json.dumps(response), mimetype='application/json')
    except BadRequest as e:
        logging.error(f"BadRequest error: {e}")
        return Response(json.dumps({'error': str(e)}), mimetype='application/json'), 400
    except Exception as e:
        logging.error(f"Internal server error: {e}")
        return Response(json.dumps({'error': 'Internal server error'}), mimetype='application/json'), 500

@app.errorhandler(400)
def bad_request_error(e):
    return Response(json.dumps({'error': 'Bad request', 'message': str(e)}), mimetype='application/json'), 400

@app.errorhandler(500)
def internal_server_error(e):
    return Response(json.dumps({'error': 'Internal server error', 'message': 'An unexpected error occurred'}), mimetype='application/json'), 500



if __name__ == '__main__':
    from gunicorn.app.wsgiapp import WSGIApplication
    WSGIApplication("%(application)s").run()
