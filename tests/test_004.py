import allure
from playwright.sync_api import expect
from utils.tools import take_screenshot


class TestLogoutUser:

    def test_logout_user(
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
            login_page.login_account_heading
        ).to_be_visible()

        login_page.login(
            registered_user["email"],
            registered_user["password"]
        )

        expect(
            home_page.logged_in_as
        ).to_be_visible()

        with allure.step("Logout"):
            home_page.click_logout_button()

        with allure.step("Verify logout"):
            expect(
            login_page.login_account_heading
        ).to_be_visible()
            take_screenshot(page, "User is logout")