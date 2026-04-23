from logger import app_logger, error_logger
from monitor import check_system_health
from reporter import generate_report
from etl_pipeline import run_etl
import time


# ==============================
# 🚀 SYSTEM START FUNCTION
# ==============================
def start_system():
    try:
        print("🚀 MAIN.PY STARTED")

        app_logger.info("🚀 Weather Pipeline System Starting...")

        print("\n==============================")
        print("🌤️ WEATHER DATA PIPELINE SYSTEM")
        print("==============================\n")

        # ==========================
        # 📊 SYSTEM HEALTH CHECK
        # ==========================
        print("📊 Running System Health Check...\n")
        check_system_health()

        # ==========================
        # 📄 INITIAL REPORT
        # ==========================
        print("\n📄 Generating Initial Report...\n")
        generate_report()

        # ==========================
        # 🔄 INITIAL ETL RUN
        # ==========================
        print("\n🚀 Running Initial ETL...\n")
        run_etl()

        app_logger.info("✅ System initialized successfully")
        print("✅ SYSTEM STARTED SUCCESSFULLY")

    except Exception as e:
        error_logger.error(f"❌ System Startup Failed: {e}")
        print(f"❌ SYSTEM ERROR: {e}")


# ==============================
# 🔄 CONTINUOUS PIPELINE
# ==============================
def run_continuous_pipeline(interval=10):
    print(f"\n⏰ Scheduler started (Every {interval} seconds)\n")

    try:
        while True:
            run_etl()
            time.sleep(interval)

    except KeyboardInterrupt:
        app_logger.warning("🛑 System stopped manually")
        print("\n🛑 Pipeline Stopped Safely")


# ==============================
# ▶️ MAIN ENTRY POINT
# ==============================
if __name__ == "__main__":
    start_system()

    # ⚠️ Enable only if needed
    # run_continuous_pipeline(interval=10)