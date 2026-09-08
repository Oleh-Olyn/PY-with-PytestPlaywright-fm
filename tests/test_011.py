import allure
from playwright.sync_api import expect
from test_data.user_data import fake
from utils.tools import take_screenshot


class TestSubscriptionInCart:

    def test_subscription_in_cart(
        self,
        page,
        home_page,
    ):
        home_page.open()

        expect(
            home_page.home_page_heading
        ).to_be_visible()

        home_page.click_cart()

        expect(
            home_page.subscription_heading
        ).to_be_visible()

        with allure.step("Subscribe in cart page"):
            home_page.subscribe(
            fake.unique.email()
        )

        with allure.step("Verify subscribe in cart page"):
            expect(
            home_page.subscription_success_message
        ).to_be_visible()
            take_screenshot(page, "User is subscribed in cart page")

