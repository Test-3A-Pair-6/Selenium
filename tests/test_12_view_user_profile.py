from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import Driver, ConfigReader as cr, Constants as const
from pages import page_12_view_user_profile

class TestViewUserProfile:

    def setup_method(self):
        self.driver = Driver.get_driver()
        self.driver.get(cr.read_config("url_main"))
        self.page = page_12_view_user_profile.PageViewUserProfile(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_profile_title_control(self):
        self.page.login(const.valid_user_name, const.valid_password)
        WebDriverWait(self.driver, 20).until(EC.url_changes(const.loginURL))
        self.driver.execute_script("window.scrollTo(0, 500);")
        self.page.profile_title_control()

