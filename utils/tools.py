import allure


def take_screenshot(page, name):
    allure.attach(
        page.screenshot(),
        name=name,
        attachment_type=allure.attachment_type.PNG,
    )

