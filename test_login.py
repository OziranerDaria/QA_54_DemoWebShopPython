
from pages.login_page import LoginPage
import os

class TestLogin:

    def test_successful_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.fill_email_field(os.getenv("TEST_EMAIL"))
        login_page.fill_password_field(os.getenv("TEST_PASSWORD"))
        login_page.click_on_login_button()

        assert login_page.is_logout_displayed()

    def test_login_with_wrong_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.fill_email_field(os.getenv("TEST_EMAIL"))
        login_page.fill_password_field(os.getenv("INVALID_PASSWORD"))
        login_page.click_on_login_button()

        assert "The credentials provided are incorrect" in login_page.get_error_message()

    def test_login_with_empty_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.fill_email_field(os.getenv("TEST_EMAIL"))
        login_page.fill_password_field("")
        login_page.click_on_login_button()

        assert "The credentials provided are incorrect" in login_page.get_error_message()

    def test_login_with_invalid_email(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.fill_email_field(os.getenv("INVALID_EMAIL"))
        login_page.fill_password_field(os.getenv("TEST_PASSWORD"))
        login_page.click_on_login_button()

        assert "Please enter a valid email address." in login_page.get_invalid_email_error()








