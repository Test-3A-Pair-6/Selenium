from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import Driver, ConfigReader as cr, Constants as const
from pages import page_15_my_education_life


class TestEducation:
    def setup_method(self):
        self.driver = Driver.get_driver()
        self.driver.get(cr.read_config("url_main"))
        self.page = page_15_my_education_life.PageEducation(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_add_education(self):
        self.page.login(const.valid_user_name, const.valid_password)
        WebDriverWait(self.driver, 20).until(EC.url_changes(const.loginURL))
        self.page.education_life()
        self.page.operationResult()
        assert const.education_message in self.page.operationResult()
        Driver.screenshot(self.driver, "../screenshots/screenshots_15_education",
                         "add_education_page.png")
        sleep(5)