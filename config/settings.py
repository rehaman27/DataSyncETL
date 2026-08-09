import os

from dotenv import load_dotenv


# Load variables from .env file
load_dotenv()


class Settings:
    # Stripe
    STRIPE_API_KEY = os.getenv("STRIPE_API_KEY")

    # Salesforce
    SALESFORCE_USERNAME = os.getenv("SALESFORCE_USERNAME")
    SALESFORCE_PASSWORD = os.getenv("SALESFORCE_PASSWORD")
    SALESFORCE_SECURITY_TOKEN = os.getenv("SALESFORCE_SECURITY_TOKEN")

    # Zendesk
    ZENDESK_API_TOKEN = os.getenv("ZENDESK_API_TOKEN")

    # PostgreSQL
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")

    # AWS S3
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_REGION = os.getenv("AWS_REGION")
    S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")


# Create settings object
settings = Settings()