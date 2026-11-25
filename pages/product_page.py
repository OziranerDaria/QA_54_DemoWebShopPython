from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class ProductPage:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#add-to-cart-button-13")
    CART_QUANTITY = (By.CSS_SELECTOR, "span.cart-qty")

    def __init__(self, driver):
        self.driver = driver

    def click_add_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART_BUTTON).click()

    def open_product_page(self):
        self.driver.get("https://demowebshop.tricentis.com/computing-and-internet")

    def get_cart_quantity(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*self.CART_QUANTITY).text == "(1)"
        )
        return self.driver.find_element(*self.CART_QUANTITY).text