from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import Driver

class PageSettings:
    def __init__(self, driver):
        self.driver = driver

    def home(self): 
        self.user_name = self.driver.find_element(By.XPATH, "//input[@name=\"email\"]")
        self.password = self.driver.find_element(By.XPATH, "//input[@name=\"password\"]")
        self.login_button = self.driver.find_element(By.XPATH, "//button[@type=\"submit\"]")
        return self
    
    def login(self, username, password):
        self.home()
        self.user_name.send_keys(username)
        self.password.send_keys(password)
        self.driver.execute_script("window.scrollTo(0, 300);")
        sleep(20) #Has been added because Tobeto put reCaptcha and told us to manually pass it.
        self.login_button.click()

    def navigate_to_settings(self, url):
        self.driver.get(url)

    def operationResult(self):
        self.toast_message = Driver.wait(self.driver, By.XPATH, "//div[@class='toast-body']").text

    def verify_warnings(self, field_error_message):
        warning_xpath = f"//span[text()='{field_error_message}']"
        warnings = self.driver.find_elements(By.XPATH, warning_xpath)
        return len(warnings)

    def change_password(self, current_password, new_password):
        current_password_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "currentPassword"))
        )
        new_password_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        confirm_password_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "passwordConfirmation"))
        )

        current_password_input.send_keys(current_password)
        new_password_input.send_keys(new_password)
        confirm_password_input.send_keys(new_password)

        change_password_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Şifre Değiştir')]"))
        )
        change_password_button.click()
    