from models.schemas import Customer


def test_valid_customer():
    customer = Customer(
        customer_id="C001",
        name="Rahul",
        email="rahul@gmail.com",
        phone="9876543210",
        currency="USD",
        created_at="2026-08-08T10:00:00"
    )

    assert customer.customer_id == "C001"
    assert customer.email == "rahul@gmail.com"