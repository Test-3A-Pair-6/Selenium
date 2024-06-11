import os
from time import sleep

import pyautogui
import pytest
from selenium.webdriver import Keys

from pages import page_chatbot
from utils import ConfigReader as cr
from utils import Constants as const
from utils import Driver


class TestChatbot:
    def setup_method(self):
        self.driver = Driver.get_driver()
        self.driver.get(cr.read_config("url_login"))
        self.page = page_chatbot.PageChatbot(self.driver)

    def teardown_method(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_chatbot_icon(self):
        self.page.chatbotIcon()
        self.page.chatbot_icon.click()
        self.driver.switch_to.default_content()
        self.page.chatbotWindow()
        assert self.page.chatbot_window.is_displayed(), "Chatbot is not displayed"
        self.page.minimize_button.click()
        self.driver.switch_to.default_content()
        self.page.chatbotIcon()
        assert self.page.chatbot_icon.is_displayed(), "Chatbot icon is not displayed"

    @pytest.mark.skip
    @pytest.mark.parametrize("param", [1, 2])
    def test_chatbot_window(self, param):
        self.page.chatbotIcon()
        self.page.chatbot_icon.click()
        self.driver.switch_to.default_content()
        self.page.chatbotWindow()
        self.page._input.send_keys(const.user_name, Keys.ENTER)
        self.page.chatbotWindowNameEntered(3)
        assert const.chatbot_pleased_message in self.page.messages[-1].text, "Chatbot message is not displayed"
        assert self.page.choices[0].text == const.choice_1
        assert self.page.choices[1].text == const.choice_2
        if param == 1:
            self.page.choices[0].click()
            self.page.chatbotWindowNameEntered(6)
            assert const.choice_1_message in self.page.messages[-1].text, "Chatbot message is not displayed"
        else:
            self.page.choices[1].click()
            self.page.chatbotWindowNameEntered(5)
            assert const.choice_2_message in self.page.messages[-1].text, "Chatbot message is not displayed"

    @pytest.mark.skip
    def test_chatbot_window_close(self):
        self.page.chatbotIcon()
        self.page.chatbot_icon.click()
        self.driver.switch_to.default_content()
        self.page.chatbotWindow()
        self.page.close_button.click()
        self.page.chatbotClose()
        self.page.close_choices[0].click()
        self.page.chatbotRate()
        self.page.rate.click()
        self.page.survey_button.click()
        self.driver.switch_to.default_content()
        self.page.chatbotIcon()
        assert self.page.chatbot_icon.is_displayed(), "Chatbot icon is not displayed"

    def test_emoji_check(self):
        self.page.chatbotIcon()
        self.page.chatbot_icon.click()
        self.driver.switch_to.default_content()
        self.page.chatbotWindow()
        self.page._input.send_keys(const.user_name, Keys.ENTER)
        self.page.chatbotEmojis()
        self.page.emojis_button.click()
        self.page.shadowRoot()
        self.driver.execute_script("arguments[0].click();", self.page.emoji)
        self.page.chatbotEmojis()
        self.page.emojis_button.click()
        self.page.textBox()
        assert self.page.text_box.text == const.emoji

    def test_file_upload(self):
        self.page.chatbotIcon()
        self.page.chatbot_icon.click()
        self.driver.switch_to.default_content()
        self.page.chatbotWindow()
        self.page._input.send_keys(const.user_name, Keys.ENTER)
        self.page.fileIcon()
        self.page.file_box.click()
        self.page.fileUpload()
        self.page.file_upload.click()
        # Wait for the file manager to open
        sleep(2)
        screenshot_dir = '../screenshots'
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, 'file_manager.png')
        # screenshot the system screen
        screenshot = pyautogui.screenshot()
        screenshot.save(screenshot_path)
        assert os.path.exists(screenshot_path), "Screenshot is not saved"
