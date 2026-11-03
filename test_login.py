import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

URL = "https://demowebshop.tricentis.com/"


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(URL)
    yield driver
    driver.quit()


class TestLogin:

    def test_successful_login(self, driver):
        login_link = driver.find_element(By.LINK_TEXT, "Log in")
        login_link.click()

        email_field = driver.find_element(By.ID, "Email")
        email_field.send_keys(os.getenv("TEST_EMAIL"))

        password_field = driver.find_element(By.ID, "Password")
        password_field.send_keys(os.getenv("TEST_PASSWORD"))

        login_button = driver.find_element(
            By.CSS_SELECTOR, "input.login-button"
        )
        login_button.click()

        assert driver.find_element(
            By.LINK_TEXT, "Log out"
        ).is_displayed()
