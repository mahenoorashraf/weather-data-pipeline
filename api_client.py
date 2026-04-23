import requests
import os
from dotenv import load_dotenv
from pathlib import Path
from database import insert_api_log

# ==============================
# 🔐 LOAD .env SAFELY
# ==============================
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv("OPENWEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


# ==============================
# 🔹 Fetch Weather Data
# ==============================
def fetch_weather(city):
    try:
        # ❌ If API key missing
        if not API_KEY:
            print("❌ API Key not found. Set OPENWEATHER_API_KEY in .env file")
            return None

        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(BASE_URL, params=params)
        data = response.json()

        # ==========================
        # ✅ SUCCESS RESPONSE
        # ==========================
        if response.status_code == 200:
            insert_api_log(city, "Success")

            return {
                "city": city,
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "condition": data["weather"][0]["description"]
            }

        # ==========================
        # ❌ API ERROR RESPONSE
        # ==========================
        else:
            insert_api_log(city, "Failed")
            print(f"❌ API Error for {city}: {data}")
            return None

    except Exception as e:
        insert_api_log(city, "Error")
        print(f"❌ Exception for {city}: {e}")
        return None


# ==============================
# 🔹 TEST RUN
# ==============================
if __name__ == "__main__":
    cities = ["Delhi", "Mumbai", "Chennai", "Bangalore"]

    for city in cities:
        print(f"\n📡 Fetching data for {city}...")
        result = fetch_weather(city)

        if result:
            print("✅ Data:", result)
        else:
            print("❌ Failed")