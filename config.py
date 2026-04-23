# ==============================
# 🌤️ WEATHER PROJECT CONFIG FILE
# ==============================

# 🔑 API Configuration
API_KEY = "7e2899c04460683b44abbe812d77cb62"

# 🌍 API URL
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# 🏙 Cities to track
CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore"]

# 🗄 Database
DB_NAME = "weather.db"

# ⏰ Scheduler (in seconds)
SCHEDULE_INTERVAL = 10   # for testing (change to 3600 for 1 hour)

# 📊 Alert Thresholds
TEMP_THRESHOLD = 30       # alert if temperature > 30°C
HUMIDITY_THRESHOLD = 75   # alert if humidity > 75%

# 📁 Logs & Reports (for future use)
LOG_FILE = "logs/pipeline.log"
REPORT_FILE = "reports/weather_report.txt"
