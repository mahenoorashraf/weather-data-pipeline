# ==============================
# 🔹 Validate API Response
# ==============================
def validate_weather_data(data):
    """
    Validates OpenWeather API response
    Returns True if valid else False
    """

    if not data:
        print("❌ Error: Empty API response")
        return False

    # Required keys
    required_keys = ["main", "weather", "name"]

    for key in required_keys:
        if key not in data:
            print(f"❌ Missing key: {key}")
            return False

    main = data.get("main", {})
    weather = data.get("weather", [])

    if "temp" not in main or "humidity" not in main:
        print("❌ Missing temperature or humidity")
        return False

    if not weather or "description" not in weather[0]:
        print("❌ Missing weather description")
        return False

    return True


# ==============================
# 🔹 Extract Clean Values
# ==============================
def extract_weather_values(data):
    """
    Extracts required fields safely
    """

    try:
        city = data["name"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]

        return city, temperature, humidity, condition

    except Exception as e:
        print("❌ Extraction Error:", e)
        return None


# ==============================
# 🔹 Threshold Alerts
# ==============================
def validate_thresholds(temp, humidity, temp_limit, humidity_limit):
    """
    Returns alerts if thresholds exceeded
    """

    alerts = []

    if temp > temp_limit:
        alerts.append(f"🔥 High Temp: {temp}°C")

    if humidity > humidity_limit:
        alerts.append(f"💧 High Humidity: {humidity}%")

    return alerts


# ==============================
# ▶️ TEST BLOCK (IMPORTANT)
# ==============================
if __name__ == "__main__":

    sample_data = {
        "name": "Delhi",
        "main": {
            "temp": 32,
            "humidity": 70
        },
        "weather": [
            {"description": "clear sky"}
        ]
    }

    print("Validator Test Running...\n")

    valid = validate_weather_data(sample_data)
    print("Valid Data:", valid)

    if valid:
        result = extract_weather_values(sample_data)
        print("Extracted Values:", result)

        alerts = validate_thresholds(32, 70, 30, 60)
        print("Alerts:", alerts)