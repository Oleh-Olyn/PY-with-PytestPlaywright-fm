from playwright.sync_api import Page, expect


class ContactUsPage:

    def __init__(self, page: Page):
        self.page = page

        self.get_in_touch_heading = page.get_by_text(
            "Get In Touch"
        )

        self.name = page.locator(
            '[data-qa="name"]'
        )

        self.email = page.locator(
            '[data-qa="email"]'
        )

        self.subject = page.locator(
            '[data-qa="subject"]'
        )

        self.message = page.locator(
            '[data-qa="message"]'
        )

        self.file_input = page.locator(
            'input[type="file"]'
        )

        self.submit_button = page.locator(
            '[data-qa="submit-button"]'
        )

        self.success_message = page.locator(
            "#contact-page"
        ).get_by_text(
            "Success! Your details have been submitted successfully."
        )

        self.home_button = page.locator(
            "#contact-page"
        ).get_by_role(
            "link",
            name="Home"
        )

    def fill_contact_form(
        self,
        name,
        email,
        subject,
        message,
    ):
        self.name.fill(name)
        expect(self.name).to_have_value(name)
        self.email.fill(email)
        expect(self.email).to_have_value(email)
        self.subject.fill(subject)
        expect(self.subject).to_have_value(subject)
        self.message.fill(message)
        expect(self.message).to_have_value(message)

    def upload_file(self, file_path):
        self.file_input.set_input_files(file_path)

    def click_submit(self):
        self.submit_button.click()

    def click_home(self):
        self.home_button.click()