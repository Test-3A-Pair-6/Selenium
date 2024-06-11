import os
from time import sleep

import pytest
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages import page_social_media
from utils import Driver, ConfigReader as cr, Constants as const


class TestSocialMedia:
    def setup_method(self):
        self.driver = Driver.get_driver()
        self.driver.get(cr.read_config("url_login"))
        self.page = page_social_media.PageSocialMedia(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def prc_social_media(self, flag=False):
        self.page.home()
        self.page.user_name.send_keys(const.valid_user_name)
        self.page.password.send_keys(const.valid_password)
        self.driver.execute_script("window.scrollTo(0, 300);")
        sleep(2)
        frames = self.driver.find_elements(By.TAG_NAME, "iframe")
        self.driver.switch_to.frame(frames[0])
        rechaptcha = self.driver.find_element(By.XPATH, "//div[@class='recaptcha-checkbox-border' and @role='presentation']")
        rechaptcha.click()
        self.driver.switch_to.default_content()
        sleep(2)
        login_button = self.driver.find_element(By.XPATH, "//button[@type=\"submit\"]")
        self.driver.execute_script("arguments[0].click();", login_button)
        Driver.wait(self.driver, By.XPATH, "//button[@data-dismiss='toast']", "click").click()
        self.page.platform()
        try:
            self.page.burger_menu.click()
        except ElementClickInterceptedException:
            self.page.platform()
            self.driver.execute_script("arguments[0].click();", self.page.burger_menu)
        self.page.mainMenu()
        self.page.menu_list[2].click()
        self.page.editIcon()
        self.page.edit_icon.click()
        self.page.options()
        self.page.option.click()
        if flag:
            self.page.accountAddPage()

    @pytest.mark.parametrize("media, url", cr.read_json("../data/socialMedia.json"))
    def test_social_media_add(self, media, url):
        self.prc_social_media(True)
        if media == "Instagram":
            self.page.save_button.click()
            self.page.errors()
            assert const.field_error_message in self.page.field_error
        self.page.account_type.send_keys(media, Keys.ENTER)
        self.page.account_url.send_keys(url)
        self.page.save_button.click()
        self.page.operationResult()
        screenshot_dir = '../screenshots'
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f'{media}_added.png')
        sleep(1)
        self.driver.save_screenshot(screenshot_path)
        assert const.social_media_add_message in self.page.toast_message
        if media == "Twitter":
            self.page.mediaCount()
            assert self.page.media_count == 3

    def test_social_media_update_and_remove(self):
        self.prc_social_media()
        self.page.mediaIcons()
        self.driver.execute_script("arguments[0].click();", self.page.update_icons[1])
        self.page.updateFields()
        self.page.update_input.clear()
        self.page.update_input.send_keys(f"updated")
        self.driver.execute_script("arguments[0].click();", self.page.update_button)
        self.page.operationResult()
        assert const.social_media_update_message in self.page.toast_message
        self.page.mediaIcons()
        self.driver.execute_script("arguments[0].click();", self.page.remove_icons[1])
        self.page.removeChoice()
        self.driver.execute_script("arguments[0].click();", self.page.remove_choice_yes)
