from logger import app_logger, error_logger

app_logger.info("TEST: App logger working")
error_logger.error("TEST: Error logger working")

print("Logs should be written now")