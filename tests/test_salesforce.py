from extract.salesforce import SalesforceExtractor


def test_salesforce_extractor_creation():

    extractor = SalesforceExtractor()

    assert extractor is not None
    assert extractor.access_token is None