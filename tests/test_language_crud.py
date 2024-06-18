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
    
    def test_add_language(self):
        self.page.login(const.valid_user_name, const.valid_password)
        WebDriverWait(self.driver, 20).until(EC.url_changes("https://tobeto.com/giris"))
        self.page.navigate_to_languages("https://tobeto.com/profilim/profilimi-duzenle/yabanci-dil")

        self.page.add_language()

        self.page.operationResult()
        assert "• Yabancı dil bilgisi eklendi." in self.page.toast_message