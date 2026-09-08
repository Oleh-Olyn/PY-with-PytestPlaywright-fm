from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        self.new_user_signup_heading = page.get_by_text(
            "New User Signup!"
        )

        self.login_account_heading = page.get_by_text(
            "Login to your account"
        )

        self.signup_name = page.locator(
            '[data-qa="signup-name"]'
        )

        self.signup_email = page.locator(
            '[data-qa="signup-email"]'
        )

        self.signup_button = page.locator(
            '[data-qa="signup-button"]'
        )

        self.login_email = page.locator(
            '[data-qa="login-email"]'
        )

        self.login_password = page.locator(
            '[data-qa="login-password"]'
        )

        self.login_button = page.locator(
            '[data-qa="login-button"]'
        )

        self.login_error_message = page.get_by_text(
            "Your email or password is incorrect!"
        )

        self.signup_error_message = page.get_by_text(
            "Email Address already exist!"
        )

    def enter_signup_details(self, name, email):
        self.signup_name.fill(name)
        self.signup_email.fill(email)

    def click_signup(self):
        self.signup_button.click()

    def login(self, email, password):
        self.login_email.fill(email)
        self.login_password.fill(password)
        self.click_login()

    def click_login(self):
        self.login_button.click()