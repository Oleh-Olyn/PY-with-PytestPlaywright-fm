import allure
from playwright.sync_api import expect
from utils.tools import take_screenshot


class TestSearchProduct:

    def test_search_product(
        self,
        page,
        home_page,
        products_page,
    ):
        home_page.open()

        expect(
            home_page.home_page_heading
        ).to_be_visible()

        home_page.click_products()

        expect(
            products_page.all_products_heading
        ).to_be_visible()

        with allure.step("Search product"):
            products_page.search_product(
            "Blue Top"
        )

        with allure.step("Verify searching product"):
            expect(
            products_page.searched_products_heading
        ).to_be_visible()
            take_screenshot(page, "Searched products heading is present")

        expect(
            products_page.searched_products.first
        ).to_be_visible()
        take_screenshot(page, "Product is searched")

