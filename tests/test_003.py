import allure
from playwright.sync_api import expect
from utils.tools import take_screenshot


class TestLoginUserIncorrectEmailPassword:

    def test_login_user_with_incorrect_credentials(
        self,
        page,
        home_page,
        login_page
    ):
        home_page.open()

        expect(
            home_page.home_page_heading
        ).to_be_visible()

        home_page.click_signup_login()

        expect(
            login_page.login_account_heading
        ).to_be_visible()

        with allure.step("Login with incorrect email and password"):
            login_page.login(
            "incorrect@example.com",
            "WrongPassword123!"
        )

        with allure.step("Verify error message is present"):
            expect(
            login_page.login_error_message
        ).to_be_visible()
            take_screenshot(page, "Error message is present")