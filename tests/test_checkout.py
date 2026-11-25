from base_test import BaseTest
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

class TestCheckout(BaseTest):

    def test_successful_checkout(self):
        product_page = ProductPage(self.driver)
        product_page.open_product_page()
        product_page.click_add_to_cart()

        assert product_page.get_cart_quantity() == "(1)", "Product was not added to cart"

        cart_page = CartPage(self.driver)
        cart_page.click_cart_link()
        cart_page.accept_terms()
        cart_page.click_checkout()

        checkout_page = CheckoutPage(self.driver)
        checkout_page.prepare_billing_address("Test Test1, Street Test 1, Ashdod 3344556, Israel")
        checkout_page.click_billing_continue()

        checkout_page.click_shipping_continue()
        checkout_page.select_ground_shipping()
        checkout_page.click_shipping_method_continue()
        checkout_page.select_cash_on_delivery()
        checkout_page.click_payment_method_continue()
        checkout_page.click_payment_info_continue()

        assert checkout_page.get_order_product_name() == "Computing and Internet", "Wrong product in order"
        assert checkout_page.get_order_total() == "17.00", "Incorrect order total"

        checkout_page.click_confirm_order()

        assert checkout_page.get_order_success_message() == "Your order has been successfully processed!", "Order was not completed successfully"