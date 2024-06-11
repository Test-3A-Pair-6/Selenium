from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utils import Constants as const


class PageChatbot:
    chatbot_icon = None
    chatbot_window = None
    minimize_button = None
    close_button = None
    close_choices = None
    _input = None
    messages = None
    choices = None
    rate = None
    survey_button = None
    emojis_button = None
    emoji = None
    text_box = None
    file_box = None
    file_upload = None

    def __init__(self, driver):
        self.driver = driver

    def chatbotIcon(self):
        iframe = self.driver.find_element(By.XPATH, "//*[@id=\"exw-launcher-frame\"]")
        self.driver.switch_to.frame(iframe)
        self.chatbot_icon = self.driver.find_element(By.XPATH, "//*[@id=\"exw-launcher-frame-body\"]")

    def chatbotWindow(self):
        iframe = self.driver.find_element(By.XPATH, "//*[@class=\"exw-conversation-container-frame\"]")
        self.driver.switch_to.frame(iframe)
        self.chatbot_window = self.driver.find_element(By.XPATH, "//*[@id=\"exw-conversation-frame-body\"]")
        input_div = self.driver.find_element(By.CLASS_NAME, "exw-inline-response-input-container")
        self._input = input_div.find_element(By.TAG_NAME, "input")
        self.minimize_button = self.driver.find_element(By.CSS_SELECTOR, ".exw-minimize-button.header-button")
        self.close_button = self.driver.find_element(By.CSS_SELECTOR, ".exw-end-session-button.header-button")

    @staticmethod
    def wait_for_element(driver, by, value, count, timeout=20):
        WebDriverWait(driver, timeout).until(lambda drv: len(drv.find_elements(by, value)) == count)

    def chatbotWindowNameEntered(self, count):
        self.wait_for_element(self.driver, By.CLASS_NAME, "exw-sender-response", count)
        self.messages = self.driver.find_elements(By.CLASS_NAME, "exw-message-text")
        self.choices = self.driver.find_elements(By.CLASS_NAME, "exw-reply")

    def chatbotClose(self):
        close_choice = self.driver.find_element(By.CLASS_NAME, "finishSessionCheckButtons")
        self.close_choices = close_choice.find_elements(By.TAG_NAME, "button")

    def chatbotRate(self):
        self.rate = self.driver.find_element(By.XPATH, "//*[contains(@class, 'rateEmoji') and @data-value='1']")
        self.survey_button = self.driver.find_element(By.ID, "surveyBtn")

    def chatbotEmojis(self):
        self.emojis_button = self.driver.find_element(By.CSS_SELECTOR, "[type='button'][class*='exw-add-emoji']")

    def shadowRoot(self):
        emoji_picker = self.driver.find_element(By.CSS_SELECTOR, 'emoji-picker')
        shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', emoji_picker)
        self.emoji = shadow_root.find_element(By.CSS_SELECTOR, f"#emo-{const.emoji}")

    def textBox(self):
        self.text_box = self.driver.find_element(By.CLASS_NAME, "exw-new-message")

    def fileIcon(self):
        self.file_box = self.driver.find_element(By.CLASS_NAME, "exw-add-file")

    def fileUpload(self):
        self.file_upload = self.driver.find_element(By.CLASS_NAME, "exw-drag-drop-select-button")
