import requests

from config.settings import settings


class SalesforceExtractor:

    def __init__(self):
        self.access_token = None

    def authenticate(self):
        """
        Authenticate with Salesforce
        and obtain an access token.
        """
        pass

    def get_customers(self):
        """
        Fetch customer data from Salesforce.
        """
        pass