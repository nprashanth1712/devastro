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
        "name": "get_current_date_time",
         "description": "Fetches the current date and current time."
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
    {"type": "function",
        "function": {
            "name": "get_ashtakvarga",
            "description": "Retrieve Ashtakvarga information from a birth chart.",
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
           "name": "get_binnashtakvarga",
           "description": "Retrieve Binnashtakvarga information from a birth chart.",
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
                        "description": "Planet for Binnashtakvarga report",
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
            "name": "get_western_planets",
            "description": "Retrieve information on the positions of planets in the Western astrological system from a birth chart.",
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
