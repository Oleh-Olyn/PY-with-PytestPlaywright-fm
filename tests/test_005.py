import allure
from playwright.sync_api import expect
from utils.tools import take_screenshot


class TestRegisterUserExistingEmail:

    def test_register_user_existing_email(
        self,
        page,
        home_page,
        login_page,
        registered_user
    ):
        home_page.open()

        expect(
            home_page.home_page_heading
        ).to_be_visible()

        home_page.click_signup_login()

        expect(
            login_page.new_user_signup_heading
        ).to_be_visible()

        with allure.step("Register User with existing email"):
            login_page.enter_signup_details(
            registered_user["name"],
            registered_user["email"]
        )

        login_page.click_signup()

        with allure.step("Verify error message"):
            expect(
            login_page.signup_error_message
        ).to_be_visible()
            take_screenshot(page, "Error message is present")