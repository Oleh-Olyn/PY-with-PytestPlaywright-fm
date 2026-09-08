from playwright.sync_api import Page


class ProductsPage:

    def __init__(self, page: Page):
        self.page = page

        self.all_products_heading = page.get_by_text(
            "All Products"
        )

        self.products_list = page.locator(
            ".features_items .product-image-wrapper"
        )

        self.first_product = self.products_list.first

        self.first_view_product = self.first_product.get_by_text(
            "View Product"
        )

        self.product_name = page.locator(
            ".product-information h2"
        )

        self.product_category = page.get_by_text(
            "Category:"
        )

        self.product_price = page.get_by_text(
            "Rs."
        )

        self.product_availability = page.get_by_text(
            "Availability:"
        )

        self.product_condition = page.get_by_text(
            "Condition:"
        )

        self.product_brand = page.get_by_text(
            "Brand:"
        )

        self.search_input = page.locator(
            "#search_product"
        )

        self.search_button = page.locator(
            "#submit_search"
        )

        self.searched_products_heading = page.get_by_text(
            "Searched Products"
        )

        self.searched_products = page.locator(
            ".features_items .product-image-wrapper"
        )

        self.products = page.locator(
            ".features_items .product-image-wrapper"
        )

        self.first_product = self.products.nth(0)
        self.second_product = self.products.nth(1)

        self.first_add_to_cart = self.first_product.get_by_text(
            "Add to cart"
        ).first

        self.second_add_to_cart = self.second_product.get_by_text(
            "Add to cart"
        ).nth(1)

        self.continue_shopping_button = page.get_by_text(
            "Continue Shopping"
        )

        self.view_cart_button = page.get_by_text(
            "View Cart"
        )

    def click_first_view_product(self):
        self.first_view_product.click()

    def search_product(self, product_name):
        self.search_input.fill(product_name)
        self.search_button.click()

    def add_first_product_to_cart(self):
        self.first_product.hover()
        self.first_add_to_cart.click()

    def add_second_product_to_cart(self):
        self.second_product.hover()
        self.second_add_to_cart.click()

    def click_continue_shopping(self):
        self.continue_shopping_button.click()

    def click_view_cart(self):
        self.view_cart_button.click()