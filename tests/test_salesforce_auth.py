from unittest.mock import patch

from extract.salesforce import SalesforceExtractor


def test_salesforce_authentication():

    mock_response = {
        "access_token": "test_access_token",
        "instance_url": "https://example.salesforce.com"
    }

    with patch(
        "extract.salesforce.settings.SALESFORCE_LOGIN_URL",
        "https://login.salesforce.com"
    ), patch(
        "extract.salesforce.settings.SALESFORCE_CLIENT_ID",
        "test_client_id"
    ), patch(
        "extract.salesforce.settings.SALESFORCE_CLIENT_SECRET",
        "test_client_secret"
    ), patch(
        "extract.salesforce.settings.SALESFORCE_USERNAME",
        "test@example.com"
    ), patch(
        "extract.salesforce.settings.SALESFORCE_PASSWORD",
        "test_password"
    ), patch(
        "extract.salesforce.settings.SALESFORCE_SECURITY_TOKEN",
        "test_security_token"
    ), patch(
        "extract.salesforce.requests.post"
    ) as mock_post:

        mock_post.return_value.json.return_value = mock_response

        mock_post.return_value.raise_for_status.return_value = None

        extractor = SalesforceExtractor()

        token = extractor.authenticate()

        assert token == "test_access_token"

        assert extractor.access_token == (
            "test_access_token"
        )

        assert extractor.instance_url == (
            "https://example.salesforce.com"
        )