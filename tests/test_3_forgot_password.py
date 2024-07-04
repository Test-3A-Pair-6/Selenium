
import pytest
from pages import page_3_forgot_password
from utils import Driver, ConfigReader as cr, Constants as const


class TestForgotPassword:
    def setup_method(self):
        self.driver = Driver.get_driver()
        self.page = page_3_forgot_password.PageForgotPassword(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_send_forgot_password_reset_link(self):
        self.driver.get(cr.read_config("url_forgot_password"))
        self.page.fills_in_email_input()
        self.page.clicks_send_button()
        assert const.success_password_reset_message in self.page.success_reset_message()

    def test_password_reset(self):
        self.driver.get(const.reset_password_url)
        self.page.enters_the_new_password()
        self.page.clicks_send_button()
        assert const.success_password_reset_message2 in self.page.success_reset_message()

    def test_reset_password_invalid_email(self):
        self.driver.get(cr.read_config("url_forgot_password"))
        self.page.fills_in_email_input_with_invalid_email()
        self.page.clicks_send_button()
        assert const.unsuccess_password_reset_message in self.page.failed_reset_message()
