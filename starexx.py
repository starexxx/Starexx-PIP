import json
import random
import requests
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Remaining API request count
remain_count = 20  

# API Configuration
TOPUP_API_URL = "https://topup.pk/api/auth/player_id_login"
HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36"
}

# Bot Credits
STAREXX = {
    "Developer": "Starexx"
    "Telegram": "https://t.me/starexx7"
}


@app.get("/like")
def fetch_player_info(uid: str):
    """Fetch Free Fire player info using UID."""
    global remain_count

    if not uid.isdigit():
        raise HTTPException(status_code=400, detail="Invalid UID format. Please enter a numeric UID.")

    if remain_count <= 0:
        raise HTTPException(status_code=403, detail="Request limit exceeded. Try again later.")

    data = {"app_id": 100067, "login_id": uid}
    response = requests.post(TOPUP_API_URL, headers=HEADERS, data=json.dumps(data))

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail=f"Failed to fetch player data. Status Code: {response.status_code}")

    data_json = response.json()
    nickname = data_json.get("nickname", "Not Found")
    region = data_json.get("region", "Not Found")

    if nickname == "Not Found" or region == "Not Found":
        raise HTTPException(status_code=500, detail="Player data not found. Please check the UID.")

    remain_count -= 1
    return {
        "UID": uid,
        "Nickname": nickname,
        "Region": region,
        "LIKES_RECEIVED_TODAY": "N/A",
        "LIKES_PREDICTED_NEXT_DAYS": random.randint(10, 40),
        "Credit": STAREXX
    }


@app.get("/visit")
def check_visit_status(region: str, uid: str):
    """Verify visit status for a Free Fire account."""
    global remain_count

    if remain_count <= 0:
        raise HTTPException(status_code=403, detail="Request limit exceeded. Try again later.")

    api_url = f"https://ariiflexlabs.vercel.app/send_visit?uid={uid}&region={region}"
    response = requests.get(api_url)

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Visit verification failed. Try again later.")

    data = response.json()
    visit_status = data.get("Success", "UNKNOWN").upper()

    remain_count -= 1
    return {
        "PLAYER_UID": uid,
        "VISIT_STATUS": visit_status,
        "MESSAGE": "Join our community: https://t.me/Freefirevisit1000",
        "CREDITS": STAREXX
    }


@app.get("/remain")
def get_remaining_requests():
    """Retrieve the remaining request limit."""
    return {
        "remaining_requests": remain_count,
        "message": "Requests left before reset."
    }


@app.post("/setremain")
def update_remaining_requests(new_count: int):
    """Manually update the remaining request count."""
    global remain_count
    remain_count = new_count
    return {
        "message": f"Request limit successfully updated to {remain_count}.",
        "CREDITS": STAREXX
    }


@app.get("/")
def get_credits():
    """Display API credits and developer information."""
    return STAREXX
