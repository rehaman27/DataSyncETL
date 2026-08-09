import requests

from config.settings import settings


class StripeExtractor:

    BASE_URL = "https://api.stripe.com/v1"

    def __init__(self):
        if not settings.STRIPE_API_KEY:
            raise ValueError("STRIPE_API_KEY is not configured in .env")

        self.headers = {
            "Authorization": f"Bearer {settings.STRIPE_API_KEY}"
        }

    def get_customers(self, limit=100):
        """
        Fetch a single page of customers from Stripe.
        """

        url = f"{self.BASE_URL}/customers"

        params = {
            "limit": limit
        }

        response = requests.get(
            url,
            headers=self.headers,
            params=params,
            timeout=30
        )

        response.raise_for_status()

        return response.json()

    def get_all_customers(self, limit=100):
        """
        Fetch all customers using Stripe cursor-based pagination.
        """

        url = f"{self.BASE_URL}/customers"

        all_customers = []
        starting_after = None

        while True:

            params = {
                "limit": limit
            }

            if starting_after:
                params["starting_after"] = starting_after

            response = requests.get(
                url,
                headers=self.headers,
                params=params,
                timeout=30
            )

            response.raise_for_status()

            result = response.json()

            customers = result.get("data", [])

            all_customers.extend(customers)

            print(f"Fetched {len(customers)} customers")

            # Stop when Stripe says there are no more records
            if not result.get("has_more"):
                break

            # Use the last customer's ID as the cursor
            if not customers:
                break

            starting_after = customers[-1]["id"]

        return all_customers