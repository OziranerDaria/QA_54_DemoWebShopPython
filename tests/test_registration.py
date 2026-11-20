from pages.registration_page import RegistrationPage
import uuid

class TestRegistration:
    def test_successful_registration(self, driver):
        registration_page = RegistrationPage(driver)
        registration_page.open_registration_page()
        registration_page.fill_first_name_field("Test")
        registration_page.fill_last_name_field("Test1")

        email = f"test.qa.{uuid.uuid4().hex[:8]}@example.com"
        registration_page.fill_email_field(email)

        registration_page.fill_password_field("Test123!")
        registration_page.fill_confirm_password_field("Test123!")
        registration_page.click_on_register_button()

        assert registration_page.get_success_message() == "Your registration completed"

    def test_registration_with_empty_first_name(self, driver):
        registration_page = RegistrationPage(driver)
        registration_page.open_registration_page()
        registration_page.fill_last_name_field("Test1")
        registration_page.fill_email_field("negative.qa.1401@example.com")
        registration_page.fill_password_field("Test123!")
        registration_page.fill_confirm_password_field("Test123!")
        registration_page.click_on_register_button()

        assert registration_page.get_first_name_error() == "First name is required."

    def test_registration_with_empty_last_name(self, driver):
        registration_page = RegistrationPage(driver)
        registration_page.open_registration_page()
        registration_page.fill_first_name_field("Test")
        registration_page.fill_email_field("negative.qa.1402@example.com")
        registration_page.fill_password_field("Test123!")
        registration_page.fill_confirm_password_field("Test123!")
        registration_page.click_on_register_button()

        assert registration_page.get_last_name_error() == "Last name is required."

    def test_registration_with_different_passwords(self, driver):
        registration_page = RegistrationPage(driver)
        registration_page.open_registration_page()
        registration_page.fill_first_name_field("Test")
        registration_page.fill_last_name_field("Test1")
        registration_page.fill_email_field("negative.qa.1403@example.com")
        registration_page.fill_password_field("Test123!")
        registration_page.fill_confirm_password_field("Test456!")
        registration_page.click_on_register_button()

        assert registration_page.get_confirm_password_error() == "The password and confirmation password do not match."