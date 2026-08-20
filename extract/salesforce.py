import requests

from config.settings import settings
from utils.logger import logger


class SalesforceExtractor:

    API_VERSION = "v61.0"

    def __init__(self):
        self.access_token = None
        self.instance_url = None

    def validate_configuration(self):
        """
        Validate required Salesforce configuration.
        """

        required_settings = {
            "SALESFORCE_LOGIN_URL": settings.SALESFORCE_LOGIN_URL,
            "SALESFORCE_CLIENT_ID": settings.SALESFORCE_CLIENT_ID,
            "SALESFORCE_CLIENT_SECRET": settings.SALESFORCE_CLIENT_SECRET,
            "SALESFORCE_USERNAME": settings.SALESFORCE_USERNAME,
            "SALESFORCE_PASSWORD": settings.SALESFORCE_PASSWORD,
            "SALESFORCE_SECURITY_TOKEN": (
                settings.SALESFORCE_SECURITY_TOKEN
            ),
        }

        missing = [
            name
            for name, value in required_settings.items()
            if not value
        ]

        if missing:
            raise ValueError(
                "Missing Salesforce configuration: "
                + ", ".join(missing)
            )

    def authenticate(self):
        """
        Authenticate with Salesforce using
        OAuth username-password flow.
        """

        self.validate_configuration()

        token_url = (
            f"{settings.SALESFORCE_LOGIN_URL}"
            "/services/oauth2/token"
        )

        password = (
            f"{settings.SALESFORCE_PASSWORD}"
            f"{settings.SALESFORCE_SECURITY_TOKEN}"
        )

        payload = {
            "grant_type": "password",
            "client_id": settings.SALESFORCE_CLIENT_ID,
            "client_secret": settings.SALESFORCE_CLIENT_SECRET,
            "username": settings.SALESFORCE_USERNAME,
            "password": password,
        }

        logger.info(
            "Starting Salesforce authentication"
        )

        response = requests.post(
            token_url,
            data=payload,
            timeout=30
        )

        response.raise_for_status()

        result = response.json()

        self.access_token = result["access_token"]
        self.instance_url = result["instance_url"]

        logger.info(
            "Salesforce authentication successful"
        )

        return self.access_token