from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import Driver, ConfigReader as cr, Constants as const
from pages import page_certificate_crud

class TestCertificateCRUD:
    def setup_method(self):
        self.driver = Driver.get_driver()
        self.driver.get(cr.read_config("url_login"))
        self.page = page_certificate_crud.PageCertificateCRUD(self.driver)

    def teardown_method(self): 
        self.driver.quit()
    
    def test_add_certificate(self):
        self.page.login(const.valid_user_name, const.valid_password)
        WebDriverWait(self.driver, 20).until(EC.url_changes(const.loginURL))

        self.page.navigate_to_certificates(const.certificatesURL)
        WebDriverWait(self.driver, 20).until(EC.url_contains("sertifikalarim"))
        
        self.page.add_certificate(const.certificateName, const.certificateYear, const.certificatePDF)
        self.page.save_valid_certificate()
        self.page.verify_certificate_added(const.certificateName)

    def test_add_invalid_certificate(self):
        self.page.login(const.valid_user_name, const.valid_password)
        WebDriverWait(self.driver, 20).until(EC.url_changes(const.loginURL))

        self.page.navigate_to_certificates(const.certificatesURL)
        WebDriverWait(self.driver, 20).until(EC.url_contains("sertifikalarim"))

        self.page.add_certificate(const.certificateName, const.certificateYear, const.invalidCertificate)
        self.page.verify_invalid_certificate_error(const.invalid_certificate_message)

    def test_delete_certificate(self):
        self.page.login(const.valid_user_name, const.valid_password)
        WebDriverWait(self.driver, 20).until(EC.url_changes(const.loginURL))

        self.page.navigate_to_certificates(const.certificatesURL)
        WebDriverWait(self.driver, 20).until(EC.url_contains("sertifikalarim"))

        self.page.delete_certificate()
        self.page.operationResult()
        assert const.certificate_delete_message in self.page.toast_message