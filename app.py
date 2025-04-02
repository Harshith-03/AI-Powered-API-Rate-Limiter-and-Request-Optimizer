# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 17:04:23 2025

@author: harsh
"""

import json
import os
from fastapi import FastAPI, Request
from datetime import datetime

app = FastAPI()
LOG_FILE = "api_logs.json"

def log_request(ip: str, timestamp: str):
    print(f"Logging request: {ip} at {timestamp}")  # Debugging output

    try:
        with open(LOG_FILE, "r") as file:
            logs = json.load(file)  # Read existing logs
    except (FileNotFoundError, json.JSONDecodeError):
        logs = []

    logs.append({"ip": ip, "timestamp": timestamp})

    with open(LOG_FILE, "w") as file:
        json.dump(logs, file, indent=4)  # Write updated logs

@app.get("/api")
async def rate_limited_endpoint(request: Request):
    client_ip = request.client.host
    log_request(client_ip, datetime.now().isoformat())  # Call logging function
    return {"message": "Request logged"}
