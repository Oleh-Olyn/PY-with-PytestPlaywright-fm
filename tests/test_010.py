import allure
from playwright.sync_api import expect
from test_data.user_data import fake
from utils.tools import take_screenshot


class TestSubscriptionInHome:

    def test_subscription_in_home(
        self,
        page,
        home_page,
    ):
        home_page.open()

        expect(
            home_page.home_page_heading
        ).to_be_visible()

        expect(
            home_page.subscription_heading
        ).to_be_visible()

        with allure.step("Subscribe in home page"):
            home_page.subscribe(
            fake.unique.email()
        )

        with allure.step("Verify subscribe in home page"):
            expect(
            home_page.subscription_success_message
        ).to_be_visible()
            take_screenshot(page, "User is subscribed in home page")

