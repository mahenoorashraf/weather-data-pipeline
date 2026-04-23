from database import get_connection
from logger import app_logger, error_logger


# ==============================
# 📄 REPORT GENERATOR
# ==============================
def generate_report():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # ✅ ONLY WEATHER TABLE (NO cities anywhere)
        cursor.execute("""
            SELECT city, temperature, humidity, weather_condition, timestamp
            FROM weather
            ORDER BY timestamp DESC
            LIMIT 10
        """)

        rows = cursor.fetchall()
        conn.close()

        print("\n📄 WEATHER REPORT")
        print("========================================")

        if not rows:
            print("⚠️ No data available")
            return

        for row in rows:
            city, temp, humidity, condition, timestamp = row

            print(f"🌍 City: {city}")
            print(f"🌡️ Temp: {temp}°C")
            print(f"💧 Humidity: {humidity}%")
            print(f"🌤️ Condition: {condition}")
            print(f"⏰ Time: {timestamp}")
            print("----------------------------------------")

        app_logger.info("Report generated successfully")

    except Exception as e:
        error_logger.error(f"❌ Report Error: {e}")
        print(f"❌ Report Error: {e}")


# ==============================
# ▶️ RUN DIRECTLY
# ==============================
if __name__ == "__main__":
    generate_report()