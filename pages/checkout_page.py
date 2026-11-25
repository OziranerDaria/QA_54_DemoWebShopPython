from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class CheckoutPage:
    COUNTRY_DROPDOWN = (By.CSS_SELECTOR, "#BillingNewAddress_CountryId")
    CITY_INPUT = (By.CSS_SELECTOR, "#BillingNewAddress_City")
    ADDRESS_INPUT = (By.CSS_SELECTOR, "#BillingNewAddress_Address1")
    ZIP_CODE_INPUT = (By.CSS_SELECTOR, "#BillingNewAddress_ZipPostalCode")
    PHONE_INPUT = (By.CSS_SELECTOR, "#BillingNewAddress_PhoneNumber")
    BILLING_CONTINUE_BUTTON = (By.CSS_SELECTOR, 'input[onclick="Billing.save()"]')
    SHIPPING_CONTINUE_BUTTON = (By.CSS_SELECTOR, 'input[onclick="Shipping.save()"]')
    GROUND_SHIPPING_RADIO = (By.CSS_SELECTOR, "#shippingoption_0")
    SHIPPING_METHOD_CONTINUE_BUTTON = (By.CSS_SELECTOR, 'input[onclick="ShippingMethod.save()"]')
    CASH_ON_DELIVERY_RADIO = (By.CSS_SELECTOR, "#paymentmethod_0")
    PAYMENT_METHOD_CONTINUE_BUTTON = (By.CSS_SELECTOR, 'input[onclick="PaymentMethod.save()"]')
    PAYMENT_INFO_CONTINUE_BUTTON = (By.CSS_SELECTOR, 'input[onclick="PaymentInfo.save()"]')
    CONFIRM_ORDER_BUTTON = (By.CSS_SELECTOR, 'input[onclick="ConfirmOrder.save()"]')
    ORDER_PRODUCT_NAME = (By.CSS_SELECTOR, ".product-name")
    ORDER_TOTAL = (By.CSS_SELECTOR, "span.product-price.order-total strong")
    ORDER_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.order-completed div.title strong")
    BILLING_ADDRESS_SELECT = (By.ID, "billing-address-select")

    def __init__(self, driver):
        self.driver = driver

    def select_country(self, country):
        dropdown = Select(self.driver.find_element(*self.COUNTRY_DROPDOWN))
        dropdown.select_by_visible_text(country)

    def fill_city(self, city):
        self.driver.find_element(*self.CITY_INPUT).send_keys(city)

    def fill_address(self, address):
        self.driver.find_element(*self.ADDRESS_INPUT).send_keys(address)

    def fill_zip_code(self, zip_code):
        self.driver.find_element(*self.ZIP_CODE_INPUT).send_keys(zip_code)

    def fill_phone(self, phone):
        self.driver.find_element(*self.PHONE_INPUT).send_keys(phone)

    def click_billing_continue(self):
        self.driver.find_element(*self.BILLING_CONTINUE_BUTTON).click()

    def click_shipping_continue(self):
        self.driver.find_element(*self.SHIPPING_CONTINUE_BUTTON).click()

    def select_ground_shipping(self):
        self.driver.find_element(*self.GROUND_SHIPPING_RADIO).click()

    def click_shipping_method_continue(self):
        self.driver.find_element(*self.SHIPPING_METHOD_CONTINUE_BUTTON).click()

    def select_cash_on_delivery(self):
        self.driver.find_element(*self.CASH_ON_DELIVERY_RADIO).click()

    def click_payment_method_continue(self):
        self.driver.find_element(*self.PAYMENT_METHOD_CONTINUE_BUTTON).click()

    def click_payment_info_continue(self):
        self.driver.find_element(*self.PAYMENT_INFO_CONTINUE_BUTTON).click()

    def click_confirm_order(self):
        self.driver.find_element(*self.CONFIRM_ORDER_BUTTON).click()

    def get_order_product_name(self):
        return self.driver.find_element(*self.ORDER_PRODUCT_NAME).text

    def get_order_total(self):
        return self.driver.find_element(*self.ORDER_TOTAL).text

    def get_order_success_message(self):
        return self.driver.find_element(*self.ORDER_SUCCESS_MESSAGE).text

    def select_saved_address(self, address):
        Select(self.driver.find_element(*self.BILLING_ADDRESS_SELECT)).select_by_visible_text(address)

    def is_saved_address_available(self, address):
        address_list = Select(self.driver.find_element(*self.BILLING_ADDRESS_SELECT))
        return any(option.text == address for option in address_list.options)

    def is_billing_address_select_present(self):
        return bool(self.driver.find_elements(*self.BILLING_ADDRESS_SELECT))

    def prepare_billing_address(self, address):
        if self.is_billing_address_select_present():
            if self.is_saved_address_available(address):
                self.select_saved_address(address)
                return

            self.select_saved_address("New Address")

        self.select_country("Israel")
        self.fill_city("Ashdod")
        self.fill_address("Street Test 1")
        self.fill_zip_code("3344556")
        self.fill_phone("0501234567")