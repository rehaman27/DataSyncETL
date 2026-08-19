import requests

from config.settings import settings
from utils.logger import logger


class SalesforceExtractor:

    API_VERSION = "v61.0"

    def __init__(self):
        self.access_token = None
        self.instance_url = None

    def authenticate(self):
        """
        Authenticate with Salesforce using OAuth
        username-password flow.
        """

        if not settings.SALESFORCE_LOGIN_URL:
            raise ValueError(
                "SALESFORCE_LOGIN_URL is not configured"
            )

        if not settings.SALESFORCE_CLIENT_ID:
            raise ValueError(
                "SALESFORCE_CLIENT_ID is not configured"
            )

        if not settings.SALESFORCE_CLIENT_SECRET:
            raise ValueError(
                "SALESFORCE_CLIENT_SECRET is not configured"
            )

        if not settings.SALESFORCE_USERNAME:
            raise ValueError(
                "SALESFORCE_USERNAME is not configured"
            )

        if not settings.SALESFORCE_PASSWORD:
            raise ValueError(
                "SALESFORCE_PASSWORD is not configured"
            )

        if not settings.SALESFORCE_SECURITY_TOKEN:
            raise ValueError(
                "SALESFORCE_SECURITY_TOKEN is not configured"
            )

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
            "Authenticating with Salesforce"
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