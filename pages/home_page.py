from playwright.sync_api import Page


class HomePage:

    def __init__(self, page: Page):
        self.page = page

        self.home_page_heading = page.get_by_role(
            "heading",
            name="Full-Fledged practice website for Automation Engineers"
        )

        self.signup_login_button = page.get_by_role(
            "link",
            name="Signup / Login"
        )

        self.logged_in_as = page.get_by_text(
            "Logged in as"
        )

        self.logout_button = page.get_by_role(
            "link",
            name="Logout"
        )

        self.delete_account_button = page.get_by_role(
            "link",
            name="Delete Account"
        )

        self.contact_us_button = page.get_by_role(
            "link",
            name="Contact us"
        )

        self.test_cases_button = page.get_by_role(
            "link",
            name="Test Cases"
        ).first

        self.products_button = page.get_by_role(
            "link",
            name="Products"
        )

        self.subscription_heading = page.get_by_text(
            "Subscription"
        )

        self.subscription_email = page.locator(
            "#susbscribe_email"
        )

        self.subscription_button = page.locator(
            "#subscribe"
        )

        self.subscription_success_message = page.get_by_text(
            "You have been successfully subscribed!"
        )

        self.cart_button = page.get_by_role(
            "link",
            name="Cart"
        )


    def open(self):
        self.page.goto("https://www.automationexercise.com")

    def click_signup_login(self):
        self.signup_login_button.click()

    def click_delete_account(self):
        self.delete_account_button.click()

    def click_logout_button(self):
        self.logout_button.click()

    def click_contact_us(self):
        self.contact_us_button.click()

    def click_test_cases(self):
        self.test_cases_button.click()

    def click_products(self):
        self.products_button.click()

    def subscribe(self, email):
        self.subscription_email.fill(email)
        self.subscription_button.click()

    def click_cart(self):
        self.cart_button.click()