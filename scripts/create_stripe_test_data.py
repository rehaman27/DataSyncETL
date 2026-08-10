import requests

from config.settings import settings


def create_customer(name, email):
    url = "https://api.stripe.com/v1/customers"

    headers = {
        "Authorization": f"Bearer {settings.STRIPE_API_KEY}"
    }

    data = {
        "name": name,
        "email": email
    }

    response = requests.post(
        url,
        headers=headers,
        data=data,
        timeout=30
    )

    response.raise_for_status()

    customer = response.json()

    print(
        f"Created customer: "
        f"{customer['id']} - "
        f"{customer['name']}"
    )


def main():

    customers = [
        ("Rehaman", "rehaman@test.com"),
        ("Suraksha", "suraksha@test.com"),
        ("Lohit", "lohit@test.com"),
        ("Jay", "jay@test.com"),
    ]

    for name, email in customers:
        create_customer(name, email)


if __name__ == "__main__":
    main()