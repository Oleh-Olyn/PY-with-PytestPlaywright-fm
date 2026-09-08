import allure
from playwright.sync_api import expect
from utils.tools import take_screenshot


class TestAllProductsAndProductDetail:

    def test_all_products_and_product_detail(
        self,
        page,
        home_page,
        products_page,
    ):
        home_page.open()

        expect(
            home_page.home_page_heading
        ).to_be_visible()

        with allure.step("Open Products Page"):
            home_page.click_products()

        with allure.step("Verify open Products Page"):
            expect(
            products_page.all_products_heading
        ).to_be_visible()
            take_screenshot(page, "Products Page is opened")

        expect(
            products_page.products_list.first
        ).to_be_visible()
        take_screenshot(page, "Products list is present")

        products_page.click_first_view_product()

        expect(
            products_page.product_name
        ).to_be_visible()
        take_screenshot(page, "Product name is present")

        expect(
            products_page.product_category
        ).to_be_visible()
        take_screenshot(page, "Product category is present")

        expect(
            products_page.product_price
        ).to_be_visible()
        take_screenshot(page, "Product price is present")

        expect(
            products_page.product_availability
        ).to_be_visible()
        take_screenshot(page, "Product availability is present")

        expect(
            products_page.product_condition
        ).to_be_visible()
        take_screenshot(page, "Product condition is present")

        expect(products_page.product_brand).to_be_visible()
        take_screenshot(page, "Product brand is present")