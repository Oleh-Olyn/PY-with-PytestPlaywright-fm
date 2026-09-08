from playwright.sync_api import Page


class CartPage:

    def __init__(self, page: Page):
        self.page = page

        self.cart_products = page.locator(
            "#cart_info_table tbody tr"
        )

    def get_product(self, index):
        return self.cart_products.nth(index)

    def get_product_price(self, index):
        return self.get_product(index).locator(
            ".cart_price p"
        )

    def get_product_quantity(self, index):
        return self.get_product(index).locator(
            ".cart_quantity button"
        )

    def get_product_total(self, index):
        return self.get_product(index).locator(".cart_total_price")


