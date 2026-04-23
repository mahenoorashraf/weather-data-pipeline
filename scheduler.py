import schedule
import time
from etl_pipeline import run_etl
from logger import app_logger


# ==============================
# 🔄 JOB FUNCTION
# ==============================
def job():
    print("\n⏰ Running Scheduled ETL Job...\n")

    try:
        run_etl()
        print("\n✅ Job Completed!\n")

    except Exception as e:
        print(f"❌ Job Failed: {e}")
        app_logger.error(f"Scheduler Error: {e}")


# ==============================
# 🚀 STARTUP LOGS
# ==============================
app_logger.info("Application started")
app_logger.info("Scheduler initialized")

# Schedule job (every 10 seconds)
schedule.every(10).seconds.do(job)

print("🚀 Scheduler started... (every 10 seconds)")

# ==============================
# 🔁 LOOP
# ==============================
while True:
    schedule.run_pending()
    time.sleep(1)