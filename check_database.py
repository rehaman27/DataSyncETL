import sqlite3


DATABASE_PATH = "data/datasync_etl.db"


def main():

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            customer_id,
            name,
            email,
            currency,
            created_at
        FROM customers
    """)

    rows = cursor.fetchall()

    print("\nCustomers in SQLite database:")
    print("-" * 80)

    for row in rows:
        print(row)

    print("-" * 80)
    print(f"Total customers: {len(rows)}")

    connection.close()


if __name__ == "__main__":
    main()