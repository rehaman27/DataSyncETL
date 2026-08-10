from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
)
import requests


@retry(
    retry=retry_if_exception_type(
        requests.exceptions.RequestException
    ),
    wait=wait_exponential(
        multiplier=1,
        min=2,
        max=10
    ),
    stop=stop_after_attempt(3),
    reraise=True
)
def make_request(method, url, **kwargs):

    response = requests.request(
        method,
        url,
        **kwargs
    )

    if response.status_code == 429:
        raise requests.exceptions.HTTPError(
            "Stripe rate limit exceeded",
            response=response
        )

    response.raise_for_status()

    return response