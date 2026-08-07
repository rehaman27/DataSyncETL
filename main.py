from config.settings import settings
from utils.logger import logger
print("Database Host:", settings.DB_HOST)
print("Log Level:", settings.LOG_LEVEL)


logger.info("Application started successfully.")
print("Check logs/app.log")