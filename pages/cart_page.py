from selenium.webdriver.common.by import By


class CartPage:
    CART_LINK = (By.CSS_SELECTOR, "#topcartlink a")
    TERMS_CHECKBOX = (By.CSS_SELECTOR, "#termsofservice")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "#checkout")

    def __init__(self, driver):
        self.driver = driver

    def click_cart_link(self):
        self.driver.find_element(*self.CART_LINK).click()

    def accept_terms(self):
        self.driver.find_element(*self.TERMS_CHECKBOX).click()

    def click_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()