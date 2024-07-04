from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from utils import Driver
from utils import Constants as const


class PageLogin:

    def __init__(self, driver):
        self.alerts = None
        self.toast_body_message = None
        self.burger_menu = None
        self.login_button = None
        self.password = None
        self.user_name = None
        self.error_message = None
        self.driver = driver

    def main(self):
        self.user_name = self.driver.find_element(By.XPATH, "//input[@name=\"email\"]")
        self.password = self.driver.find_element(By.XPATH, "//input[@name=\"password\"]")
        self.login_button = self.driver.find_element(By.XPATH, "//button[@type=\"submit\"]")

    def fills_input_fields_with_valid_information(self):
        self.user_name.send_keys(const.valid_user_name)
        self.password.send_keys(const.valid_password)
        self.driver.execute_script("window.scrollTo(0, 300);")

    def pass_the_rerecaptcha(self):
        frames = self.driver.find_elements(By.TAG_NAME, "iframe")
        self.driver.switch_to.frame(frames[0])
        rechaptcha = self.driver.find_element(By.XPATH,
                                              "//div[@class='recaptcha-checkbox-border' and @role='presentation']")
        rechaptcha.click()
        self.driver.switch_to.default_content()
        sleep(20)

    def clicks_the_login_button(self):
        login_button = self.driver.find_element(By.XPATH, "//button[@type=\"submit\"]")
        self.driver.execute_script("arguments[0].click();", login_button)

    def fills_input_fields_with_invalid_information(self):
        self.user_name.send_keys(const.invalid_user_name)
        self.password.send_keys(const.invalid_password_)
        self.driver.execute_script("window.scrollTo(0, 300);")

    def deletes_input_fields(self):
        self.user_name.send_keys(Keys.CONTROL + 'a')
        self.user_name.send_keys(Keys.DELETE)
        self.password.send_keys(Keys.CONTROL + "a")
        self.password.send_keys(Keys.DELETE)

    def success_login_message(self):
        self.toast_body_message = Driver.wait(self.driver, By.XPATH, "//div[@class=\"toast-body\"]").text
        return self.toast_body_message

    def empty_email_password_message(self):
        self.alerts = self.driver.find_elements(By.XPATH, "//p[text()='Doldurulması zorunlu alan*']")
        alert_texts = [alert.text for alert in self.alerts]
        return " ".join(alert_texts)

    def failed_login_message(self):
        self.error_message = self.driver.find_element(By.XPATH, "//div[@class=\"toast-body\"]").text
        return self.error_message

