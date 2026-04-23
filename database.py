import sqlite3
import pandas as pd

DB_NAME = "weather.db"


# 🔹 Connection
def get_connection():
    return sqlite3.connect(DB_NAME)


# 🔹 Create tables (run once)
def setup_database():
    conn = get_connection()
    cursor = conn.cursor()

    # Weather table (USING city)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS weather (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT,
        temperature REAL,
        humidity INTEGER,
        weather_condition TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # API logs table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS api_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT,
        status TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


# 🔹 Insert weather data
def insert_weather(city, temperature, humidity, condition):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO weather (city, temperature, humidity, weather_condition)
        VALUES (?, ?, ?, ?)
    """, (city, temperature, humidity, condition))

    conn.commit()
    conn.close()


# 🔹 Insert API logs
def insert_api_log(city, status):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO api_logs (city, status)
        VALUES (?, ?)
    """, (city, status))

    conn.commit()
    conn.close()


# 🔹 Fetch data
def get_weather_data():
    conn = get_connection()

    try:
        df = pd.read_sql("SELECT * FROM weather", conn)
    except Exception as e:
        print("❌ Error reading DB:", e)
        df = None

    conn.close()
    return df


# 🔹 Test run
if __name__ == "__main__":
    setup_database()

    df = get_weather_data()

    if df is None or df.empty:
        print("⚠️ No data available")
    else:
        print(df.head())