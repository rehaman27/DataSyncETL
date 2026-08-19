from extract.salesforce import SalesforceExtractor


extractor = SalesforceExtractor()

token = extractor.authenticate()

print("Authentication successful")
print("Token received:", token[:10])
print("Instance URL:", extractor.instance_url)