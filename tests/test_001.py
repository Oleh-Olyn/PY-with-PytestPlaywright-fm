import allure
from playwright.sync_api import expect
from test_data.user_data import generate_user
from utils.tools import take_screenshot

class TestRegisterUser:

    def test_register_user(
        self,
        page,
        home_page,
        login_page,
        signup_page,
    ):
        user = generate_user()

        home_page.open()
        expect(
            home_page.home_page_heading
        ).to_be_visible()


        home_page.click_signup_login()
        expect(
            login_page.new_user_signup_heading
        ).to_be_visible()

        login_page.enter_signup_details(
            user["name"],
            user["email"],
        )

        login_page.click_signup()
        expect(
            signup_page.account_information_heading
        ).to_be_visible()

        signup_page.select_title()
        signup_page.enter_password(
            user["password"]
        )
        signup_page.select_date_of_birth(
            user["day"],
            user["month"],
            user["year"],
        )

        signup_page.select_newsletter()

        signup_page.select_special_offers()

        signup_page.fill_personal_information(
            first_name=user["first_name"],
            last_name=user["last_name"],
            company=user["company"],
            address=user["address"],
            address2=user["address2"],
            country=user["country"],
            state=user["state"],
            city=user["city"],
            zipcode=user["zipcode"],
            mobile_number=user["mobile_number"],
        )
        with allure.step("Create account"):
            signup_page.click_create_account()

        with allure.step("Verify account created"):
            expect(
            signup_page.account_created_heading
        ).to_be_visible()

            take_screenshot(page, "Account created")

        signup_page.click_continue()
        expect(
            home_page.logged_in_as
        ).to_contain_text(user["name"])

        with allure.step("Delete account"):
            home_page.click_delete_account()
        with allure.step("Verify account deleted"):
            expect(
            signup_page.account_deleted_heading
        ).to_be_visible()

            take_screenshot(page, "Account deleted")