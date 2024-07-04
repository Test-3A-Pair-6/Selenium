import pytest
from pages import page_1_login
from utils import Driver, ConfigReader as cr, Constants as const
from utils.Driver import get_driver


class TestLogin:
    def setup_method(self):
        self.driver = Driver.get_driver()
        self.driver.get(cr.read_config("url_login"))
        self.page = page_1_login.PageLogin(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_succes_login(self):
        self.page.main()
        self.page.fills_input_fields_with_valid_information()
        self.page.pass_the_rerecaptcha()
        self.page.clicks_the_login_button()
        assert const.success_message in self.page.success_login_message()

    def test_empty_email_password(self):
        self.page.main()
        self.page.fills_input_fields_with_invalid_information()
        self.page.pass_the_rerecaptcha()
        self.page.clicks_the_login_button()
        self.page.deletes_input_fields()
        assert const.empty_email_password_text in self.page.empty_email_password_message()

    def test_invalid_username_password_login(self):
        self.page.main()
        self.page.fills_input_fields_with_invalid_information()
        self.page.pass_the_rerecaptcha()
        self.page.clicks_the_login_button()
        assert const.failed_log_in_message in self.page.failed_login_message()
