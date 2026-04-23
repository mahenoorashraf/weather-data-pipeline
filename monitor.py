from database import get_connection
from logger import app_logger, error_logger


# ==============================
# 📊 SYSTEM HEALTH CHECK
# ==============================
def check_system_health():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # 🔹 Total records in weather table
        cursor.execute("SELECT COUNT(*) FROM weather")
        total_records = cursor.fetchone()[0]

        # 🔹 Latest timestamp
        cursor.execute("SELECT MAX(timestamp) FROM weather")
        last_update = cursor.fetchone()[0]

        conn.close()

        # ==========================
        # 📊 OUTPUT
        # ==========================
        print("\n📊 SYSTEM MONITOR")
        print("========================")
        print(f"📦 Total Records: {total_records}")
        print(f"⏰ Last Update: {last_update}")

        # ==========================
        # 🔍 STATUS
        # ==========================
        if total_records > 0:
            print("✅ Data is fresh and available")
        else:
            print("⚠️ No data found")

        app_logger.info("System health check completed")

    except Exception as e:
        error_logger.error(f"❌ Monitoring Error: {e}")
        print(f"❌ Monitoring Error: {e}")


# ==============================
# ▶️ RUN DIRECTLY
# ==============================
if __name__ == "__main__":
    check_system_health()