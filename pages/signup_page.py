from playwright.sync_api import Page


class SignupPage:

    def __init__(self, page: Page):
        self.page = page

        self.account_information_heading = page.get_by_text(
            "Enter Account Information"
        )

        self.title_mr = page.locator("#id_gender1")
        self.title_mrs = page.locator("#id_gender2")

        self.password = page.locator(
            '[data-qa="password"]'
        )

        self.day = page.locator(
            '[data-qa="days"]'
        )

        self.month = page.locator(
            '[data-qa="months"]'
        )

        self.year = page.locator(
            '[data-qa="years"]'
        )

        self.newsletter = page.locator(
            "#newsletter"
        )

        self.special_offers = page.locator(
            "#optin"
        )

        self.first_name = page.locator(
            '[data-qa="first_name"]'
        )

        self.last_name = page.locator(
            '[data-qa="last_name"]'
        )

        self.company = page.locator(
            '[data-qa="company"]'
        )

        self.address = page.locator(
            '[data-qa="address"]'
        )

        self.address2 = page.locator(
            '[data-qa="address2"]'
        )

        self.country = page.locator(
            '[data-qa="country"]'
        )

        self.state = page.locator(
            '[data-qa="state"]'
        )

        self.city = page.locator(
            '[data-qa="city"]'
        )

        self.zipcode = page.locator(
            '[data-qa="zipcode"]'
        )

        self.mobile_number = page.locator(
            '[data-qa="mobile_number"]'
        )

        self.create_account_button = page.locator(
            '[data-qa="create-account"]'
        )

        self.account_created_heading = page.get_by_text(
            "Account Created!"
        )

        self.continue_button = page.get_by_text(
            "Continue"
        )

        # Account deletion
        self.account_deleted_heading = page.get_by_text(
            "Account Deleted!"
        )

    def select_title(self):
        self.title_mr.check()

    def enter_password(self, password):
        self.password.fill(password)

    def select_date_of_birth(self, day, month, year):
        self.day.select_option(label=day)
        self.month.select_option(label=month)
        self.year.select_option(label=year)

    def select_newsletter(self):
        self.newsletter.check()

    def select_special_offers(self):
        self.special_offers.check()

    def fill_personal_information(
        self,
        first_name,
        last_name,
        company,
        address,
        address2,
        country,
        state,
        city,
        zipcode,
        mobile_number,
    ):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.company.fill(company)
        self.address.fill(address)
        self.address2.fill(address2)

        self.country.select_option(
            label=country
        )

        self.state.fill(state)
        self.city.fill(city)
        self.zipcode.fill(zipcode)
        self.mobile_number.fill(mobile_number)

    def click_create_account(self):
        self.create_account_button.click()

    def click_continue(self):
        self.continue_button.click()

    def register_new_user(self, user):
        self.select_title()

        self.enter_password(user["password"])

        self.fill_personal_information(
            user["first_name"],
            user["last_name"],
            user["company"],
            user["address"],
            user["address2"],
            user["country"],
            user["state"],
            user["city"],
            user["zipcode"],
            user["mobile_number"],
        )

        self.click_create_account()
        self.click_continue()

