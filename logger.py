# core/logger.py

from datetime import datetime
from config import LOG_FILE

def log_result(flag, status):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now()}] Flag: {flag} | Status: {status}\n")
