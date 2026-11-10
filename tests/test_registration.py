from pages.registration_page import RegistrationPage

class TestRegistration:
    def test_successful_registration(self, driver):
        registration_page = RegistrationPage(driver)
        registration_page.open_registration_page()
        registration_page.fill_first_name_field("Test")
        registration_page.fill_last_name_field("Test1")
        registration_page.fill_email_field("test.qa.789@example.com")
        registration_page.fill_password_field("Test123!")
        registration_page.fill_confirm_password_field("Test123!")
        registration_page.click_on_register_button()

        assert registration_page.get_success_message() == "Your registration completed"