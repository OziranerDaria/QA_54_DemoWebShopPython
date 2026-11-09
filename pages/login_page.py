
from selenium.webdriver.common.by import By


class LoginPage:
    LOGIN_LINK = (By.CSS_SELECTOR, "a[href='/login']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='Email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='Password']")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "input.login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div.validation-summary-errors")
    LOGOUT_LINK = (By.LINK_TEXT, "Log out")
    INVALID_EMAIL_ERROR = (By.CSS_SELECTOR, 'span[for="Email"]')

    def is_logout_displayed(self):
        return self.driver.find_element(*self.LOGOUT_LINK).is_displayed()

    def __init__(self, driver):
        self.driver = driver

    def open_login_page(self):
        self.driver.find_element(*self.LOGIN_LINK).click()

    def fill_email_field(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def fill_password_field(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_on_login_button(self):
        self.driver.find_element(*self.BUTTON_LOGIN).click()

    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text

    def get_invalid_email_error(self):
        return self.driver.find_element(*self.INVALID_EMAIL_ERROR).text










