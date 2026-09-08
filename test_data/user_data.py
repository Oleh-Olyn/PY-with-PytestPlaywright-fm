from faker import Faker
import random


fake = Faker()

COUNTRIES = [
    "India",
    "United States",
    "Canada",
    "Australia",
    "Israel",
    "New Zealand",
    "Singapore"
]


def generate_user():
    return {
        "name": fake.first_name(),
        "email": fake.unique.email(),
        "password": fake.password(
            length=12,
            special_chars=True,
            digits=True,
            upper_case=True,
            lower_case=True
        ),
        "day": str(fake.random_int(min=1, max=28)),
        "month": fake.month_name(),
        "year": str(fake.random_int(min=1950, max=2000)),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "company": fake.company(),
        "address": fake.street_address(),
        "address2": fake.secondary_address(),
        "country": random.choice(COUNTRIES),
        "state": fake.state(),
        "city": fake.city(),
        "zipcode": fake.postcode(),
        "mobile_number": fake.msisdn()[:10]
    }