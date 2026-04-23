import logging
import os
import sys

os.makedirs("logs", exist_ok=True)


def setup_logger(name, file_name, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        # 📁 File handler (UTF-8 FIX)
        file_handler = logging.FileHandler(
            f"logs/{file_name}",
            encoding="utf-8"
        )
        file_handler.setFormatter(formatter)

        # 🖥 Console handler (SAFE encoding)
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger


# 🔹 Loggers
app_logger = setup_logger("app_logger", "app.log")
etl_logger = setup_logger("etl_logger", "etl.log")
error_logger = setup_logger("error_logger", "error.log", logging.ERROR)