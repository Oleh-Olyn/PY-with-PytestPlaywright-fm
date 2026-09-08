import allure
from playwright.sync_api import expect
from utils.tools import take_screenshot


class TestAddProductsInCart:

    def test_add_products_in_cart(
        self,
        page,
        home_page,
        products_page,
        cart_page,
    ):
        home_page.open()

        expect(
            home_page.home_page_heading
        ).to_be_visible()

        home_page.click_products()

        expect(
            products_page.all_products_heading
        ).to_be_visible()

        with allure.step("Add first product to cart"):
            products_page.add_first_product_to_cart()

        products_page.click_continue_shopping()

        with allure.step("Add second product to cart"):
            products_page.add_second_product_to_cart()

        products_page.click_view_cart()

        with allure.step("Verify products in cart"):
            expect(
            cart_page.cart_products.nth(0)
        ).to_be_visible()
            take_screenshot(page, "Products in cart page")

        with allure.step("Verify products in cart"):
            expect(
            cart_page.cart_products.nth(1)
        ).to_be_visible()
            take_screenshot(page, "Products in cart page")

        expect(
            cart_page.get_product_price(0)
        ).to_be_visible()
        take_screenshot(page, "Product price is present")

        expect(
            cart_page.get_product_quantity(0)
        ).to_have_text("1")
        take_screenshot(page, "Product quantity is present")

        expect(
            cart_page.get_product_total(0)
        ).to_be_visible()
        take_screenshot(page, "Product total is present")

        expect(
            cart_page.get_product_price(1)
        ).to_be_visible()
        take_screenshot(page, "Product price is present")

        expect(
            cart_page.get_product_quantity(1)
        ).to_have_text("1")
        take_screenshot(page, "Product quantity is present")

        expect(
            cart_page.get_product_total(1)
        ).to_be_visible()
        take_screenshot(page, "Product total is present")

