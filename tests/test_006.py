import allure
from playwright.sync_api import expect

from utils.tools import take_screenshot


class TestContactUsForm:

    def test_contact_us_form(
        self,
        page,
        home_page,
        contact_us_page,
    ):
        home_page.open()

        expect(
            home_page.home_page_heading
        ).to_be_visible()

        home_page.click_contact_us()

        expect(
            contact_us_page.get_in_touch_heading
        ).to_be_visible()

        contact_us_page.fill_contact_form(
            name="John Doe",
            email="john@example.com",
            subject="Test Subject",
            message="This is a test message."
        )

        contact_us_page.upload_file(
            "test_data/test_file.txt"
        )

        page.on(
            "dialog",
            lambda dialog: dialog.accept()
        )

        with allure.step("Submit contact form"):
            contact_us_page.click_submit()

        with allure.step("Verify success message"):
            expect(
                contact_us_page.success_message
            ).to_be_visible()

            take_screenshot(
                page,
                "Success message is present"
            )

        contact_us_page.click_home()

        expect(
            home_page.home_page_heading
        ).to_be_visible()