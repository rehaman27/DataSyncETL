from datetime import datetime

from extract.stripe import StripeExtractor
from storage.raw_storage import save_json
from load.sqlite import (
    create_customers_table,
    load_customers
)
from utils.logger import logger


def main():

    logger.info(
        "DataSync ETL Pipeline Started"
    )

    try:

        # =========================
        # EXTRACT
        # =========================

        extractor = StripeExtractor()

        customers = (
            extractor.get_all_customers()
        )

        logger.info(
            f"Extracted {len(customers)} customers"
        )

        # =========================
        # RAW STORAGE
        # =========================

        filename = (
            f"customers_"
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        )

        file_path = save_json(
            customers,
            filename
        )

        logger.info(
            f"Raw data saved to: {file_path}"
        )

        # =========================
        # DATABASE
        # =========================

        create_customers_table()

        load_customers(customers)

        logger.info(
            "ETL pipeline completed successfully"
        )

    except Exception as error:

        logger.error(
            f"ETL pipeline failed: {error}"
        )

        raise


if __name__ == "__main__":
    main()