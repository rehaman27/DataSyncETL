import requests

from config.settings import settings


class SalesforceExtractor:

    def __init__(self):
        self.access_token = None
        self.instance_url = None

    def authenticate(self):
        """
        Authenticate with Salesforce.

        Authentication details depend on the
        Salesforce OAuth configuration provided
        by the organization.
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

        raise NotImplementedError(
            "Configure the Salesforce OAuth flow "
            "provided by Zaalima before implementing authentication."
        )