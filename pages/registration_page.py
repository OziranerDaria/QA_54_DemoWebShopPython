from selenium.webdriver.common.by import By

class RegistrationPage:
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "#FirstName")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "#LastName")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#Email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#Password")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "#ConfirmPassword")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register-button")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".result")

    def __init__(self, driver):
        self.driver = driver

    def open_registration_page(self):
        self.driver.get("https://demowebshop.tricentis.com/register")

    def fill_first_name_field(self, first_name):
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)

    def fill_last_name_field(self, last_name):
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)

    def fill_email_field(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def fill_password_field(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def fill_confirm_password_field(self, password):
        self.driver.find_element(*self.CONFIRM_PASSWORD_INPUT).send_keys(password)

    def click_on_register_button(self):
        self.driver.find_element(*self.REGISTER_BUTTON).click()

    def get_success_message(self):
        return self.driver.find_element(*self.SUCCESS_MESSAGE).text