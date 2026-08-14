from datetime import datetime

from extract.stripe import StripeExtractor
from storage.raw_storage import save_json
from utils.logger import logger
from utils.health_check import check_configuration


def main():

    logger.info("DataSync ETL Pipeline Started")

    # Configuration health check
    checks = check_configuration()

    logger.info("Configuration Health Check:")

    for name, status in checks.items():
        logger.info(
            f"{name}: {'OK' if status else 'NOT CONFIGURED'}"
        )

    try:

        extractor = StripeExtractor()

        customers = extractor.get_all_customers()

        filename = (
            f"customers_"
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        )

        file_path = save_json(
            customers,
            filename
        )

        logger.info(
            f"Total customers extracted: "
            f"{len(customers)}"
        )

        logger.info(
            f"Raw data saved to: {file_path}"
        )

    except Exception as error:

        logger.error(
            f"ETL pipeline failed: {error}"
        )

        raise


if __name__ == "__main__":
    main()