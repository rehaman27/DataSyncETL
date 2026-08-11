import pytest
from unittest.mock import patch

from extract.stripe import StripeExtractor


class MockResponse:

    def __init__(self, data, status_code=200):
        self._data = data
        self.status_code = status_code
        self.headers = {}

    def json(self):
        return self._data

    def raise_for_status(self):
        if self.status_code >= 400:
            raise Exception("API request failed")


def test_get_customers():

    mock_data = {
        "data": [
            {
                "id": "cus_001",
                "name": "Rehaman"
            },
            {
                "id": "cus_002",
                "name": "Suraksha"
            }
        ],
        "has_more": False
    }

    with patch(
        "extract.stripe.make_request",
        return_value=MockResponse(mock_data)
    ):

        extractor = StripeExtractor()

        customers = extractor.get_all_customers()

        assert len(customers) == 2
        assert customers[0]["id"] == "cus_001"


def test_empty_customers():

    mock_data = {
        "data": [],
        "has_more": False
    }

    with patch(
        "extract.stripe.make_request",
        return_value=MockResponse(mock_data)
    ):

        extractor = StripeExtractor()

        customers = extractor.get_all_customers()

        assert customers == []


def test_pagination():

    first_page = {
        "data": [
            {
                "id": "cus_001",
                "name": "Customer 1"
            }
        ],
        "has_more": True
    }

    second_page = {
        "data": [
            {
                "id": "cus_002",
                "name": "Customer 2"
            }
        ],
        "has_more": False
    }

    with patch(
        "extract.stripe.make_request",
        side_effect=[
            MockResponse(first_page),
            MockResponse(second_page)
        ]
    ):

        extractor = StripeExtractor()

        customers = extractor.get_all_customers()

        assert len(customers) == 2
        assert customers[0]["id"] == "cus_001"
        assert customers[1]["id"] == "cus_002"


def test_api_failure():

    with patch(
        "extract.stripe.make_request",
        side_effect=Exception("Stripe API failed")
    ):

        extractor = StripeExtractor()

        with pytest.raises(Exception):
            extractor.get_all_customers()