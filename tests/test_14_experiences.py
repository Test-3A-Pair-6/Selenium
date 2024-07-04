from time import sleep

from selenium.common import NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import Driver, ConfigReader as cr, Constants as const
from pages import page_14_experiences


class TestExperiences:
    def setup_method(self):
        self.driver = Driver.get_driver()
        self.driver.get(cr.read_config("url_main"))
        self.page = page_14_experiences.PageExperiences(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def click_element(self, element):
        """
        Some elements unexpectedly accept a click pattern that other elements don't and
        don't allow to execute the other pattern, so this method will solve this problem in one line.
        Attempts to click on the given element. If the conventional click fails,
        Performs a click operation with JavaScript.

        To call:
        self.click_element(element)
        """
        try:
            element.click()
            print("Element clicked successfully.")
        except NoSuchElementException:
            print("Element not found.")
        except WebDriverException as e:
            print(f"Normal click failed: {e}. JavaScript will try clicking.")
            try:
                self.driver.execute_script("arguments[0].click()", element)
                print("Clicking with JavaScript was successful.")
            except Exception as js_e:
                print(f"The JavaScript click also failed: {js_e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def test_succes_add_experiences(self):
        self.page.login(const.valid_user_name, const.valid_password)
        WebDriverWait(self.driver, 20).until(EC.url_changes(const.loginURL))
        self.page.go_to_profile()
        self.page.succes_experiences()
        self.page.job_description()
        self.page.save_button()
        self.page.operationResult()
        assert const.experiences_message in self.page.operationResult()
        Driver.screenshot(self.driver, "../screenshots/screenshots_14_experiences",
                          "add_14_experiences_page.png")

    def test_empty_experiences(self):
        self.page.login(const.valid_user_name, const.valid_password)
        WebDriverWait(self.driver, 20).until(EC.url_changes(const.loginURL))
        self.page.go_to_profile()
        self.page.save_button()
        self.page.empty_experiences()
        Driver.screenshot(self.driver, "../screenshots/screenshots_14_experiences",
                          "empty_14_experiences_page.png")

    def test_many_characters_jobDesc(self):
        self.page.login(const.valid_user_name, const.valid_password)
        WebDriverWait(self.driver, 20).until(EC.url_changes(const.loginURL))
        self.page.go_to_profile()
        self.page.succes_experiences()
        self.page.many_characters_jobDesc()
        Driver.screenshot(self.driver, "../screenshots/screenshots_14_experiences",
                          "many_characters_14_experiences_page.png")

    def test_min_characters(self):
        self.page.login(const.valid_user_name, const.valid_password)
        WebDriverWait(self.driver, 20).until(EC.url_changes(const.loginURL))
        self.page.go_to_profile()
        self.page.min_characters()
        sleep(2)
        self.page.tangermsg()
        assert const.tanger_message in self.page.tangermsg()
        Driver.screenshot(self.driver, "../screenshots/screenshots_14_experiences",
                          "min_characters_14_experiences_page.png")

    def test_many_character(self):
        self.page.login(const.valid_user_name, const.valid_password)
        WebDriverWait(self.driver, 20).until(EC.url_changes(const.loginURL))
        self.page.go_to_profile()
        self.page.many_character()
        sleep(2)
        self.page.tangermsg()
        assert const.many_character_message in self.page.tangermsg()
        Driver.screenshot(self.driver, "../screenshots/screenshots_14_experiences",
                          "fifty_characters_14_experiences_page.png")




