import pytest

from test_data.user_data import generate_user

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.contact_us_page import ContactUsPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


@pytest.fixture
def home_page(page):
    return HomePage(page)


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def signup_page(page):
    return (SignupPage(page))

@pytest.fixture
def registered_user(page, home_page, login_page, signup_page):
    user = generate_user()
    home_page.open()
    home_page.click_signup_login()
    login_page.enter_signup_details(
        user["name"],
        user["email"]
    )
    login_page.click_signup()
    signup_page.register_new_user(user)
    home_page.click_logout_button()
    return user

@pytest.fixture
def contact_us_page(page):
    return ContactUsPage(page)

@pytest.fixture
def products_page(page):
    return ProductsPage(page)

@pytest.fixture
def cart_page(page):
    return CartPage(page)