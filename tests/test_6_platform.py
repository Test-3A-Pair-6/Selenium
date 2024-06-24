from time import sleep

from pages import page_6_platform
from utils import Driver, Constants as const, ConfigReader as cr


class TestPlatform:
    def setup_method(self):
        self.driver = Driver.get_driver()
        self.driver.get(cr.read_config("url_main"))
        self.page = page_6_platform.PagePlatform(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_login(self):
        self.page.login_info()
        self.page.user_name.send_keys(const.valid_user_name)
        self.page.password.send_keys(const.valid_password)
        self.page.submit_button()
        self.page.login_button.click()
        self.page.platform()
        self.page.title.is_displayed()
        assert self.driver.current_url == cr.read_config("url_platform"), "Login failed"
        assert self.page.app.is_displayed(), "application is not displayed"
        self.page.platform_tabs()
        self.driver.execute_script("arguments[0].click();", self.page.my_courses)
        self.page.lessons_tab()
        assert len(self.page.lessons) == 4, "Lessons are not displayed"
        self.page.more_button_func()
        self.driver.execute_script("arguments[0].click();", self.page.button_more)
        self.page.lessons_tab()
        assert len(self.page.lessons) > 4, "More button is not working"
        Driver.screenshot(self.driver, "../screenshots/screenshots_6_platform", "lessons.png")
        self.driver.back()
        self.page.platform_tabs()
        self.driver.execute_script("arguments[0].click();", self.page.my_announcements)
        self.page.announcement_tab()
        assert len(self.page.announcements) == 3, "Announcements are not displayed"
        Driver.screenshot(self.driver, "../screenshots/screenshots_6_platform", "announcements.png")
        self.page.platform_tabs()
        self.driver.execute_script("arguments[0].click();", self.page.my_survey)
        Driver.screenshot(self.driver, "../screenshots/screenshots_6_platform", "survey.png")
        self.page.exam_card()
        self.driver.execute_script("arguments[0].click();", self.page.exam)
        self.page.exam_report_card()
        self.driver.execute_script("arguments[0].click();", self.page.report_close)
        Driver.screenshot(self.driver, "../screenshots/screenshots_6_platform", "exam_report.png")
        self.page.exam_result_card()
        self.driver.execute_script("arguments[0].click();", self.page.result_close)
        self.page.exam_card()
        assert self.page.exam.is_displayed(), "Exam is not displayed"
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.page.create_profile_card()
        self.driver.execute_script("arguments[0].click();", self.page.button_pack_1)
        assert self.driver.current_url == cr.read_config("url_personal_info")
        Driver.screenshot(self.driver, "../screenshots/screenshots_6_platform", "my_profile.png")
        self.driver.back()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.page.evaluate_yourself_card()
        self.driver.execute_script("arguments[0].click();", self.page.button_pack_2)
        assert self.driver.current_url == cr.read_config("url_evaluations")
        Driver.screenshot(self.driver, "../screenshots/screenshots_6_platform", "evaluate_yourself.png")
        self.driver.back()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.page.start_learn_card()
        self.driver.execute_script("arguments[0].click();", self.page.button_pack_3)
        assert self.driver.current_url == cr.read_config("url_catalog")
        Driver.screenshot(self.driver, "../screenshots/screenshots_6_platform", "start_learn.png")
