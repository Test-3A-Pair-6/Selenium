

from selenium.webdriver.common.by import By
from utils import Driver, Constants as const


class PageForgotPassword:
    def __init__(self, driver):
        self.unsuccess_password_reset_message = None
        self.forgot_password_invalid_email_input = None
        self.forgot_password_email_input = None
        self.success_password_reset_message = None
        self.new_password_again = None
        self.new_password = None
        self.toast_body_message = None
        self.send_button = None
        self.driver = driver

    def fills_in_email_input(self):
        self.forgot_password_email_input = self.driver.find_element(By.XPATH, "//input[contains(@class, \"form-control\")]")
        self.forgot_password_email_input.send_keys(const.forgot_password_email)

    def clicks_send_button(self):
        self.send_button = self.driver.find_element(By.XPATH,
                                                    "//button[contains(@class, \"btn\") and contains(@class, \"btn-primary\")]")
        self.send_button.click()

    def success_message(self):
        self.toast_body_message = self.driver.find_element(By.XPATH, "//div[@class=\"toast-body\"]").text
        return self.toast_body_message

    def enters_the_new_password(self):
        self.new_password = self.driver.find_element(By.XPATH, "//input[@name=\"password\"]")
        self.new_password.send_keys(const.new_password)
        self.new_password_again = self.driver.find_element(By.XPATH, "//input[@name=\"passwordConfirmation\"]")
        self.new_password_again.send_keys(const.new_password)

    def success_reset_message(self):
        self.success_password_reset_message = self.driver.find_element(By.XPATH,"//div[@class=\"toast-body\"]").text
        return self.success_password_reset_message

    def fills_in_email_input_with_invalid_email(self):
        self.forgot_password_invalid_email_input = self.driver.find_element(By.XPATH, "//input[contains(@class, \"form-control\")]")
        self.forgot_password_invalid_email_input.send_keys(const.forgot_password_invalid_email)

    def failed_reset_message(self):
        self.unsuccess_password_reset_message = self.driver.find_element(By.XPATH, "//div[@class=\"toast-body\"]").text
        return self.unsuccess_password_reset_message