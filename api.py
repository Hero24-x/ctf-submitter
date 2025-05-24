# core/api.py

import requests
from config import API_URL, HEADERS

def post_flag(flag):
    endpoint = f"{API_URL}/flags"
    payload = {"submission": flag}

    try:
        response = requests.post(endpoint, headers=HEADERS, json=payload)
        return response
    except Exception as e:
        print(f"🔥 API Error: {e}")
        return None
