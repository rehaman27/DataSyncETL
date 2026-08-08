from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, EmailStr, Field


class Customer(BaseModel):
    customer_id: str
    name: str
    email: EmailStr
    phone: str | None = None
    currency: str | None = None
    created_at: datetime


class Transaction(BaseModel):
    transaction_id: str
    customer_id: str
    amount: Decimal = Field(ge=0)
    currency: str
    status: str
    transaction_date: datetime


class Ticket(BaseModel):
    ticket_id: str
    customer_id: str | None = None
    subject: str
    status: str
    priority: str | None = None
    created_at: datetime