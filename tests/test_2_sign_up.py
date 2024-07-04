import pytest
from pages import page_2_sign_up
from utils import Driver, ConfigReader as cr, Constants as const


class TestSignUp:
    def setup_method(self):
        self.driver = Driver.get_driver()
        self.driver.get(cr.read_config("url_login"))
        self.page = page_2_sign_up.PageSignUp(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_success_sign_up(self):
        self.page.clicks_sign_up_option()
        self.page.main()
        self.page.fills_input_fields_with_valid_information()
        self.page.clicks_sign_up_button()
        self.page.checks_registration_approvals()
        self.page.valid_phone_number_input()
        self.page.clicks_sign_up_continue_button()

    def test_short_phone_number(self):
        self.page.clicks_sign_up_option()
        self.page.main()
        self.page.fills_input_fields_with_valid_information()
        self.page.clicks_sign_up_button()
        self.page.checks_registration_approvals()
        self.page.short_phone_number_input()
        self.page.clicks_sign_up_continue_button()

    def test_long_phone_number(self):
        self.page.clicks_sign_up_option()
        self.page.main()
        self.page.fills_input_fields_with_valid_information()
        self.page.clicks_sign_up_button()
        self.page.checks_registration_approvals()
        self.page.long_phone_number_input()
        self.page.clicks_sign_up_continue_button()

    def test_empty_phone_number(self):
        self.page.clicks_sign_up_option()
        self.page.main()
        self.page.fills_input_fields_with_valid_information()
        self.page.clicks_sign_up_button()
        self.page.checks_registration_approvals()
        self.page.empty_phone_number_input()
        self.page.clicks_sign_up_continue_button()

    def test_invalid_phone_number_characters(self):
        self.page.clicks_sign_up_option()
        self.page.main()
        self.page.fills_input_fields_with_valid_information()
        self.page.clicks_sign_up_button()
        self.page.checks_registration_approvals()
        self.page.invalid_phone_number_input()
        phone_number_value = self.page.phone_number_area.get_attribute('value')
        assert phone_number_value == "+90", f"Telefon numarası alanı sadece '+90' içeriyor.  {phone_number_value}"

    def test_invalid_email_input(self):
        self.page.clicks_sign_up_option()
        self.page.main()
        self.page.fills_input_fields_with_invalid_email()
        assert const.sign_up_invalid_email_text in self.page.invalid_email_input_text()

    def test_sign_up_existing_email(self):
        self.page.clicks_sign_up_option()
        self.page.main()
        self.page.fills_input_fields_with_existing_email()
        self.page.clicks_sign_up_button()
        self.page.checks_registration_approvals()
        self.page.valid_phone_number_input()
        self.page.clicks_sign_up_continue_button()

    def test_sign_up_short_password(self):
        self.page.clicks_sign_up_option()
        self.page.main()
        self.page.fills_input_fields_with_short_password()
        self.page.clicks_sign_up_button()
        self.page.checks_registration_approvals()
        self.page.valid_phone_number_input()
        self.page.clicks_sign_up_continue_button()

    def test_sign_up_different_password(self):
        self.page.clicks_sign_up_option()
        self.page.main()
        self.page.fills_input_fields_with_different_password()
        self.page.clicks_sign_up_button()
        self.page.checks_registration_approvals()
        self.page.valid_phone_number_input()
        self.page.clicks_sign_up_continue_button()







