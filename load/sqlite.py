from database.connection import get_connection


def create_customers_table():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            customer_id TEXT PRIMARY KEY,
            name TEXT,
            email TEXT,
            currency TEXT,
            created_at TEXT
        )
    """)

    connection.commit()
    connection.close()


def load_customers(customers):

    connection = get_connection()

    cursor = connection.cursor()

    for customer in customers:

        cursor.execute("""
            INSERT OR REPLACE INTO customers (
                customer_id,
                name,
                email,
                currency,
                created_at
            )
            VALUES (?, ?, ?, ?, ?)
        """, (
            customer.get("id"),
            customer.get("name"),
            customer.get("email"),
            customer.get("currency"),
            None
        ))

    connection.commit()
    connection.close()

    print(
        f"Loaded {len(customers)} customers into SQLite"
    )