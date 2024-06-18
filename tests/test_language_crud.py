from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import Driver, ConfigReader as cr, Constants as const
from pages import page_language_crud

class TestLanguageCRUD:
    def setup_method(self):
        self.driver = Driver.get_driver()
        self.driver.get(cr.read_config("url_login"))
        self.page = page_language_crud.PageLanguageCRUD(self.driver)

    def teardown_method(self): 
        self.driver.quit()
    
    def test_add_language_success(self):
        self.page.login(const.valid_user_name, const.valid_password)
        WebDriverWait(self.driver, 20).until(EC.url_changes(const.loginURL))
        self.page.navigate_to_languages(const.languagesURL)

        self.page.add_language(language=const.language, level=const.level)
        self.page.operationResult()
        assert "• Yabancı dil bilgisi eklendi." in self.page.toast_message
    
    def test_add_language_both_empty(self):
        self.page.login(const.valid_user_name, const.valid_password)
        WebDriverWait(self.driver, 20).until(EC.url_changes(const.loginURL))
        self.page.navigate_to_languages(const.languagesURL)

        self.page.add_language()
        warnings = self.page.verify_warnings()
        assert warnings == 2, f"Expected 2 warnings, but found {warnings}"

    def test_add_language_only_language(self):
        self.page.login(const.valid_user_name, const.valid_password)
        WebDriverWait(self.driver, 20).until(EC.url_changes(const.loginURL))
        self.page.navigate_to_languages(const.languagesURL)

        self.page.add_language(language=const.language)
        warnings = self.page.verify_warnings()
        assert warnings == 1, f"Expected 1 warning, but found {warnings}"

    def test_add_language_only_level(self):
        self.page.login(const.valid_user_name, const.valid_password)
        WebDriverWait(self.driver, 20).until(EC.url_changes(const.loginURL))
        self.page.navigate_to_languages(const.languagesURL)

        self.page.add_language(level=const.level)
        warnings = self.page.verify_warnings()
        assert warnings == 1, f"Expected 1 warning, but found {warnings}"

    def test_delete_language(self):
        self.page.login(const.valid_user_name, const.valid_password)
        WebDriverWait(self.driver, 20).until(EC.url_changes(const.loginURL))
        self.page.navigate_to_languages(const.languagesURL)
        
        self.page.delete_language(language=const.language)
        self.page.operationResult()
        assert const.language_delete_message in self.page.toast_message