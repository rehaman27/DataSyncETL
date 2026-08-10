import time

from requests import Response

from config.settings import settings
from utils.retry import make_request


class StripeExtractor:

    BASE_URL = "https://api.stripe.com/v1"

    def __init__(self):
        if not settings.STRIPE_API_KEY:
            raise ValueError(
                "STRIPE_API_KEY is not configured in .env"
            )

        self.headers = {
            "Authorization": (
                f"Bearer {settings.STRIPE_API_KEY}"
            )
        }

    def _request(self, params):
        """
        Send request to Stripe with retry
        and rate-limit handling.
        """

        url = f"{self.BASE_URL}/customers"

        response: Response = make_request(
            "GET",
            url,
            headers=self.headers,
            params=params,
            timeout=30
        )

        return response

    def get_all_customers(self, limit=100):

        all_customers = []

        starting_after = None

        while True:

            params = {
                "limit": limit
            }

            if starting_after:
                params["starting_after"] = starting_after

            response = self._request(params)

            # Rate limit
            if response.status_code == 429:

                retry_after = response.headers.get(
                    "Retry-After",
                    "2"
                )

                wait_time = int(retry_after)

                print(
                    f"Rate limit reached. "
                    f"Waiting {wait_time} seconds..."
                )

                time.sleep(wait_time)

                continue

            result = response.json()

            customers = result.get(
                "data",
                []
            )

            all_customers.extend(customers)

            print(
                f"Fetched {len(customers)} customers | "
                f"Total: {len(all_customers)}"
            )

            # No more pages
            if not result.get("has_more"):
                break

            # Safety check
            if not customers:
                break

            starting_after = customers[-1]["id"]

        return all_customers