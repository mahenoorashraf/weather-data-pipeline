import requests
from database import insert_api_log

# 🔑 Replace with your OpenWeatherMap API key
API_KEY = "7e2899c04460683b44abbe812d77cb62"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


# ==============================
# 🔹 Fetch Weather Data
# ==============================
def fetch_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        # ✅ Success
        if response.status_code == 200:
            insert_api_log(city, "Success")

            weather_data = {
                "city": city,
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "condition": data["weather"][0]["description"]
            }

            return weather_data

        # ❌ API error
        else:
            insert_api_log(city, "Failed")
            print(f"❌ API Error for {city}: {data}")
            return None

    # ❌ Exception handling
    except Exception as e:
        insert_api_log(city, "Error")
        print(f"❌ Exception for {city}: {e}")
        return None


# ==============================
# 🔹 Test Run (Optional)
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