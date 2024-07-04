from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from utils import Driver, Constants as const


class PageSignUp:
    def __init__(self, driver):
        self.register_button = None
        self.signup_option = None
        self.invalid_email = None
        self.phone_number = None
        self.phone_number_area = None
        self.sign_up_button = None
        self.sign_up_password = None
        self.sign_up_password_again = None
        self.sign_up_email = None
        self.sign_up_last_name = None
        self.sign_up_first_name = None
        self.success_sign_up_text = None
        self.driver = driver

    def clicks_sign_up_option(self):
        self.signup_option = self.driver.find_element(By.CSS_SELECTOR, ".signup")
        self.signup_option.click()
        self.driver.execute_script("window.scrollTo(0, 300);")

    def main(self):
        self.sign_up_first_name = self.driver.find_element(By.XPATH, "//input[@name=\"firstName\"]")
        self.sign_up_last_name = self.driver.find_element(By.XPATH, "//input[@name=\"lastName\"]")
        self.sign_up_email = self.driver.find_element(By.XPATH, "//input[@name=\"email\"]")
        self.sign_up_password = self.driver.find_element(By.XPATH, "//input[@name=\"password\"]")
        self.sign_up_password_again = self.driver.find_element(By.XPATH, "//input[@name=\"passwordAgain\"]")

    def fills_input_fields_with_valid_information(self):
        self.sign_up_first_name.send_keys(const.sign_up_first_name)
        self.sign_up_last_name.send_keys(const.sign_up_last_name)
        self.sign_up_email.send_keys(const.sign_up_email)
        self.sign_up_password.send_keys(const.sign_up_password)
        self.sign_up_password_again.send_keys(const.sign_up_password)

    def clicks_sign_up_button(self):
        self.sign_up_button = self.driver.find_element(By.XPATH, "//button[contains(@class, 'btn-primary')]")
        self.sign_up_button.click()
        sleep(20)

    def checks_registration_approvals(self):
        self.driver.execute_script('document.querySelector(\'input[name="contact"]\').click();')
        self.driver.execute_script('document.querySelector(\'input[name="membershipContrat"]\').click();')
        self.driver.execute_script('document.querySelector(\'input[name="emailConfirmation"]\').click();')
        self.driver.execute_script('document.querySelector(\'input[name="phoneConfirmation"]\').click();')

    def valid_phone_number_input(self):
        self.driver.execute_script(f'document.getElementById("phoneNumber").value = "{const.valid_sign_up_phone_number}";')

    def empty_phone_number_input(self):
        self.phone_number = self.driver.find_element(By.XPATH, "//input[@class=\"PhoneInputInput\"]")
        self.phone_number.send_keys("5552221203")
        self.phone_number.send_keys(Keys.CONTROL + 'a')
        self.phone_number.send_keys(Keys.DELETE)

    def clicks_sign_up_continue_button(self):
        self.register_button = self.driver.find_element(By.CSS_SELECTOR, ".btn-yes")
        self.driver.execute_script("arguments[0].disabled = false;", self.register_button)
        self.register_button.click()

    def success_sign_up_text_func(self):
        self.success_sign_up_text = Driver.wait(self.driver, By.XPATH, "//span[@class=\"success-payment-text\"]").text
        return self.success_sign_up_text

    def short_phone_number_input(self):
        self.driver.execute_script(
            f'document.getElementById("phoneNumber").value = "{const.short_sign_up_phone_number}";')

    def long_phone_number_input(self):
        self.driver.execute_script(
            f'document.getElementById("phoneNumber").value = "{const.long_sign_up_phone_number}";')

    def invalid_phone_number_input(self):
        self.phone_number_area = self.driver.find_element(By.XPATH, "//input[@id=\"phoneNumber\"]")
        self.phone_number_area.send_keys(const.invalid_phone_number_sign_up)

    def fills_input_fields_with_invalid_email(self):
        self.sign_up_first_name.send_keys(const.sign_up_first_name)
        self.sign_up_last_name.send_keys(const.sign_up_last_name)
        self.sign_up_email.send_keys(const.sign_up_invalid_email)

    def invalid_email_input_text(self):
        self.invalid_email = self.driver.find_element(By.CSS_SELECTOR, "p[style*='color: red']").text
        return self.invalid_email

    def fills_input_fields_with_existing_email(self):
        self.sign_up_first_name.send_keys(const.sign_up_first_name)
        self.sign_up_last_name.send_keys(const.sign_up_last_name)
        self.sign_up_email.send_keys(const.forgot_password_email)
        self.sign_up_password.send_keys(const.sign_up_password)
        self.sign_up_password_again.send_keys(const.sign_up_password)

    def fills_input_fields_with_short_password(self):
        self.sign_up_first_name.send_keys(const.sign_up_first_name)
        self.sign_up_last_name.send_keys(const.sign_up_last_name)
        self.sign_up_email.send_keys(const.sign_up_email)
        self.sign_up_password.send_keys(const.sign_up_short_password)
        self.sign_up_password_again.send_keys(const.sign_up_short_password)

    def fills_input_fields_with_different_password(self):
        self.sign_up_first_name.send_keys(const.sign_up_first_name)
        self.sign_up_last_name.send_keys(const.sign_up_last_name)
        self.sign_up_email.send_keys(const.sign_up_email)
        self.sign_up_password.send_keys(const.sign_up_password)
        self.sign_up_password_again.send_keys(const.sign_up_short_password)


