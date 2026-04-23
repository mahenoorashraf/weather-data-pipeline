from api_client import fetch_weather
from database import insert_weather
from logger import etl_logger, error_logger

CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore"]


def validate(data):
    if data is None:
        return False

    if data["temperature"] < -50 or data["temperature"] > 60:
        return False

    if data["humidity"] < 0 or data["humidity"] > 100:
        return False

    return True


def run_etl():
    etl_logger.info("🚀 ETL Pipeline Started")

    try:
        for city in CITIES:
            etl_logger.info(f"📡 Processing: {city}")

            data = fetch_weather(city)

            if not validate(data):
                etl_logger.warning(f"❌ Invalid data for {city}")
                print(f"❌ Invalid data for {city}")
                continue

            try:
                # ✅ INSERT USING CITY (NOT city_id)
                insert_weather(
                    data["city"],
                    data["temperature"],
                    data["humidity"],
                    data["condition"]
                )

                etl_logger.info(f"✅ Inserted data for {city}")
                print(f"✅ Inserted data for {city}")

            except Exception as db_error:
                error_logger.error(f"❌ DB Error for {city}: {db_error}")
                print(f"❌ DB Error for {city}: {db_error}")

        etl_logger.info("🏁 ETL Pipeline Completed")
        print("🏁 ETL Pipeline Completed")

    except Exception as e:
        error_logger.error(f"❌ ETL Failed: {e}")
        print(f"❌ ETL Failed: {e}")


if __name__ == "__main__":
    run_etl()