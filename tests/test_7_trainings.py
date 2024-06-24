from time import sleep

from selenium.webdriver.common.by import By

from pages import page_7_trainings
from utils import Driver, ConfigReader as cr, Constants as const


class TestTrainings:
    def setup_method(self):
        self.driver = Driver.get_driver()
        self.driver.get(cr.read_config("url_main"))
        self.page = page_7_trainings.PageTrainings(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_trainings(self):
        self.page.login_info()
        self.page.user_name.send_keys(const.valid_user_name)
        self.page.password.send_keys(const.valid_password)
        self.page.submit_button()
        self.page.login_button.click()
        self.page.platform()
        self.driver.execute_script("arguments[0].click();", self.page.my_courses)
        self.page.lessons_tab()
        assert len(self.page.lessons) == 4, "Lessons are not displayed"
        self.page.more_button_func()
        self.driver.execute_script("arguments[0].click();", self.page.button_more)
        self.page.lessons_tab()
        assert len(self.page.lessons) > 4, "More button is not working"
        for lesson in self.page.lessons:
            if lesson.find_element(By.TAG_NAME, "span").text == const.lesson_name:
                self.driver.execute_script("arguments[0].click();", lesson.find_element(By.TAG_NAME, "button"))
                break
        self.page.lesson_content()
        self.page.button_favorite.click()
        assert self.page.toast_message() == const.favorite_add_message, "Favorite add failed"
        like_count_before = int(self.page.like_before.text)
        self.page.button_like.click()
        self.page.like_after_func()
        like_count_after = int(self.page.like_after.text)
        assert like_count_before < like_count_after, "Like button is not working"
        self.page.button_about.click()
        Driver.screenshot(self.driver, "../screenshots/screenshots_7_trainings", "lesson_about.png")
