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
        WebDriverWait(self.driver, 20).until(EC.url_changes("https://tobeto.com/giris"))
        self.page.navigate_to_languages("https://tobeto.com/profilim/profilimi-duzenle/yabanci-dil")

        self.page.add_language(language="Arapça", level=" Temel Seviye (A1, A2)")
        self.page.operationResult()
        assert "• Yabancı dil bilgisi eklendi." in self.page.toast_message
    
    def test_add_language_both_empty(self):
        self.page.login(const.valid_user_name, const.valid_password)
        WebDriverWait(self.driver, 20).until(EC.url_changes("https://tobeto.com/giris"))
        self.page.navigate_to_languages("https://tobeto.com/profilim/profilimi-duzenle/yabanci-dil")

        self.page.add_language()
        warnings = self.page.verify_warnings()
        assert warnings == 2, f"Expected 2 warnings, but found {warnings}"

    def test_add_language_only_language(self):
        self.page.login(const.valid_user_name, const.valid_password)
        WebDriverWait(self.driver, 20).until(EC.url_changes("https://tobeto.com/giris"))
        self.page.navigate_to_languages("https://tobeto.com/profilim/profilimi-duzenle/yabanci-dil")

        self.page.add_language(language="Arapça")
        warnings = self.page.verify_warnings()
        assert warnings == 1, f"Expected 1 warning, but found {warnings}"

    def test_add_language_only_level(self):
        self.page.login(const.valid_user_name, const.valid_password)
        WebDriverWait(self.driver, 20).until(EC.url_changes("https://tobeto.com/giris"))
        self.page.navigate_to_languages("https://tobeto.com/profilim/profilimi-duzenle/yabanci-dil")

        self.page.add_language(level=" Temel Seviye (A1, A2)")
        warnings = self.page.verify_warnings()
        assert warnings == 1, f"Expected 1 warning, but found {warnings}"