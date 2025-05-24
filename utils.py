# core/utils.py

from core.api import post_flag
from core.logger import log_result
from core.notifier import notify

def submit_flag(flag):
    response = post_flag(flag)
    status = "UNKNOWN"

    if response is None:
        status = "API_ERROR"
        print(f"❗ Error submitting flag: {flag}")
    elif response.status_code == 200:
        data = response.json()
        if data.get("data") and data["data"].get("status") == "correct":
            status = "CORRECT"
            print(f"✅ Correct: {flag}")
        else:
            status = "INCORRECT"
            print(f"❌ Incorrect/Duplicate: {flag}")
    else:
        status = f"HTTP_{response.status_code}"
        print(f"⚠️ HTTP Error {response.status_code}: {response.text}")

    log_result(flag, status)
    notify(flag, status)
