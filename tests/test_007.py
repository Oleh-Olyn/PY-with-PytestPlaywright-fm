import allure
from playwright.sync_api import expect
from utils.tools import take_screenshot


class TestVerifyTestCasesPage:

    def test_verify_test_cases_page(
        self,
        page,
        home_page,
    ):
        home_page.open()

        expect(
            home_page.home_page_heading
        ).to_be_visible()

        with allure.step("Open Test Cases Page"):
            home_page.click_test_cases()

        with allure.step("Verify Test Cases Page is opened"):
            expect(page).to_have_url(
            "https://www.automationexercise.com/test_cases"
        )
            take_screenshot(page, "Test Cases Page is opened")