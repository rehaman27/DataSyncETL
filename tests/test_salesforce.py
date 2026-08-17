import pytest

from extract.salesforce import SalesforceExtractor


def test_salesforce_extractor_creation():

    extractor = SalesforceExtractor()

    assert extractor.access_token is None
    assert extractor.instance_url is None


def test_salesforce_requires_login_url(monkeypatch):

    monkeypatch.setattr(
        "extract.salesforce.settings.SALESFORCE_LOGIN_URL",
        None
    )

    extractor = SalesforceExtractor()

    with pytest.raises(ValueError):
        extractor.authenticate()