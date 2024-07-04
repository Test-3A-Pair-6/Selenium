from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import Driver, ConfigReader as cr, Constants as const
from pages import page_16_skills


class TestSkills:
    def setup_method(self):
        self.driver = Driver.get_driver()
        self.driver.get(cr.read_config("url_main"))
        self.page = page_16_skills.PageSkills(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_empty_skills(self):
        self.page.login(const.valid_user_name, const.valid_password)
        WebDriverWait(self.driver, 20).until(EC.url_changes(const.loginURL))
        self.page.skills()
        self.page.save_button()
        self.page.operationResult()
        assert const.skills_error_message1 in self.page.operationResult()
        Driver.screenshot(self.driver, "../screenshots/screenshots_16_skills",
                          "empty_skills_page.png")


    def test_add_skills(self):
        self.page.login(const.valid_user_name, const.valid_password)
        WebDriverWait(self.driver, 20).until(EC.url_changes(const.loginURL))
        self.page.skills()
        self.page.add_skills()
        self.page.save_button()
        self.page.operationResult()
        assert const.skills_error_message3 in self.page.operationResult()
        Driver.screenshot(self.driver, "../screenshots/screenshots_16_skills",
                          "add_skills_page.png")
        sleep(2)


    def test_delete_skills(self):
        self.page.login(const.valid_user_name, const.valid_password)
        WebDriverWait(self.driver, 20).until(EC.url_changes(const.loginURL))
        self.page.skills()
        self.page.delete_skills()
        sleep(3)
        self.page.operationResult()
        assert const.skills_error_message2 in self.page.operationResult()
        Driver.screenshot(self.driver, "../screenshots/screenshots_16_skills",
                          "delete_16_skills_page.png")
        sleep(2)



