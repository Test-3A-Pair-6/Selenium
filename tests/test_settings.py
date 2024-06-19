from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import Driver, ConfigReader as cr, Constants as const
from pages import page_settings

class TestSettings:
    def setup_method(self):
        self.driver = Driver.get_driver()
        self.driver.get(cr.read_config("url_login"))
        self.page = page_settings.PageSettings(self.driver)

    def teardown_method(self): 
        self.driver.quit()

    def test_change_password_success(self):
        self.page.login(const.settings_user_name, const.settings_password)
        WebDriverWait(self.driver, 20).until(EC.url_changes(const.loginURL))
        self.page.navigate_to_settings(const.settingsURL)

        self.page.change_password(const.settings_password, const.settings_new_password, const.settings_new_password)
        self.page.operationResult()
        assert const.change_password_msg in self.page.toast_message

    def test_change_password_all_empty(self):
        self.page.login(const.settings_user_name, const.settings_new_password)
        WebDriverWait(self.driver, 20).until(EC.url_changes(const.loginURL))
        self.page.navigate_to_settings(const.settingsURL)

        self.page.change_password("","","")
        warnings = self.page.verify_warnings(const.field_error_message)
        assert warnings == 3, f"Expected 3 warnings, but found {warnings}"

    def test_change_password_confirmation_empty(self):
        self.page.login(const.settings_user_name, const.settings_new_password)
        WebDriverWait(self.driver, 20).until(EC.url_changes(const.loginURL))
        self.page.navigate_to_settings(const.settingsURL)

        self.page.change_password(const.settings_new_password, const.settings_password, "")
        warnings = self.page.verify_warnings(const.field_error_message)
        assert warnings == 1, f"Expected 1 warnings, but found {warnings}"

    def test_change_password_character_count(self):
        self.page.login(const.settings_user_name, const.settings_new_password)
        WebDriverWait(self.driver, 20).until(EC.url_changes(const.loginURL))
        self.page.navigate_to_settings(const.settingsURL)

        self.page.change_password(const.settings_new_password, const.settings_short_new_password, const.settings_short_new_password)
        self.page.operationResult()
        assert const.change_password_short_msg in self.page.toast_message

    def test_change_password_match(self):
        self.page.login(const.settings_user_name, const.settings_new_password)
        WebDriverWait(self.driver, 20).until(EC.url_changes(const.loginURL))
        self.page.navigate_to_settings(const.settingsURL)

        self.page.change_password(const.settings_new_password, const.settings_password, const.settings_short_new_password)
        self.page.operationResult()
        assert const.password_do_not_match_msg in self.page.toast_message

    def test_change_password_repeat(self):
        self.page.login(const.settings_user_name, const.settings_new_password)
        WebDriverWait(self.driver, 20).until(EC.url_changes(const.loginURL))
        self.page.navigate_to_settings(const.settingsURL)

        self.page.change_password(const.settings_new_password, const.settings_new_password, const.settings_new_password)
        self.page.operationResult()
        assert const.change_password_repeat_msg in self.page.toast_message
