from datetime import datetime

from extract.stripe import StripeExtractor
from storage.raw_storage import save_json


def main():

    print("DataSync ETL Pipeline Started")

    extractor = StripeExtractor()

    customers = extractor.get_all_customers()

    filename = (
        f"customers_"
        f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    )

    file_path = save_json(customers, filename)

    print(f"Total customers extracted: {len(customers)}")
    print(f"Raw data saved to: {file_path}")


if __name__ == "__main__":
    main()