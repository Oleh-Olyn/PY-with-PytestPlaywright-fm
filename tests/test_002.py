from playwright.sync_api import expect


class TestLoginUserCorrectEmailPassword:

    def test_login_user(
        self,
        page,
        home_page,
        login_page,
        signup_page,
        registered_user
    ):
        home_page.open()

        expect(
            home_page.home_page_heading
        ).to_be_visible()

        home_page.click_signup_login()

        expect(
            login_page.login_account_heading
        ).to_be_visible()

        login_page.login(
            registered_user["email"],
            registered_user["password"]
        )

        expect(
            home_page.logged_in_as
        ).to_be_visible()

        home_page.click_delete_account()

        expect(
            signup_page.account_deleted_heading
        ).to_be_visible()