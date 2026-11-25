import os
import pytest
from pages.login_page import LoginPage

class BaseTest:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.login_page = LoginPage(self.driver)
        self.email = os.getenv("TEST_EMAIL")
        self.password = os.getenv("TEST_PASSWORD")

        self.login_page.open_login_page()
        self.login_page.fill_email_field(self.email)
        self.login_page.fill_password_field(self.password)
        self.login_page.click_on_login_button()

        assert self.login_page.is_logout_displayed(), "Login failed"