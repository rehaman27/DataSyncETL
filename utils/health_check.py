from config.settings import settings


def check_configuration():

    checks = {
        "Stripe API Key": bool(settings.STRIPE_API_KEY),

        "Salesforce Username": bool(
            settings.SALESFORCE_USERNAME
        ),

        "Salesforce Password": bool(
            settings.SALESFORCE_PASSWORD
        ),

        "Salesforce Security Token": bool(
            settings.SALESFORCE_SECURITY_TOKEN
        ),

        "Database Host": bool(settings.DB_HOST),

        "AWS Region": bool(settings.AWS_REGION),
    }

    return checks