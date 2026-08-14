from config.settings import settings


def check_configuration():
    checks = {
        "Stripe API Key": bool(settings.STRIPE_API_KEY),
        "Database Host": bool(settings.DB_HOST),
        "AWS Region": bool(settings.AWS_REGION),
    }

    return checks