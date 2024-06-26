from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import Driver

class PageLanguageCRUD:
    def __init__(self, driver):
        self.driver = driver
        self.user_name = None
        self.password = None
        self.login_button = None
        self.toast_message = None

    def home(self): 
        self.user_name = self.driver.find_element(By.XPATH, "//input[@name='email']")
        self.password = self.driver.find_element(By.XPATH, "//input[@name='password']")
        self.login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        return self

    def login(self, username, password):
        self.home()
        self.user_name.send_keys(username)
        self.password.send_keys(password)
        self.driver.execute_script("window.scrollTo(0, 300);")
        sleep(20)  # Added to manually pass the reCaptcha
        self.login_button.click()

    def navigate_to_languages(self, url):
        self.driver.get(url)

    def add_language(self, language=None, level=None):
        if language:
            dropdown1 = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#__next > div > main > section > div > div > div.col-12.col-lg-9 > form > div > div:nth-child(1) > div > div"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", dropdown1)
            dropdown1.click()
            option1_xpath = f"//div[contains(@class, 'select__option') and text()='{language}']"
            option1 = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, option1_xpath))
            )
            option1.click()

        if level:
            dropdown2 = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#__next > div > main > section > div > div > div.col-12.col-lg-9 > form > div > div:nth-child(2) > div > div"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", dropdown2)
            dropdown2.click()
            option2_xpath = f"//div[contains(@class, 'select__option') and text()='{level}']"
            option2 = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, option2_xpath))
            )
            option2.click()

        save_button_xpath = "//button[contains(@class, 'btn-primary') and contains(text(), 'Kaydet')]"
        save_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, save_button_xpath))
        )
        save_button.click()

    def delete_language(self, language):
        language_xpath = f"//*[@id=\"__next\"]/div/main/section/div/div/div[2]/div/div/div"
        delete_button_xpath = ".//span[@class='delete-lang']"

        language_element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, language_xpath))
        )

        action = ActionChains(self.driver)
        action.move_to_element(language_element).perform()

        delete_button = WebDriverWait(language_element, 20).until(
            EC.element_to_be_clickable((By.XPATH, delete_button_xpath))
        )
        delete_button.click()

        confirm_button_xpath = "//button[contains(@class, 'btn-yes') and text()='Evet']"
        confirm_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, confirm_button_xpath))
        )
        confirm_button.click()

    def verify_warnings(self, field_error_message):
        warning_xpath = f"//p[text()='{field_error_message}']"
        warnings = self.driver.find_elements(By.XPATH, warning_xpath)
        return len(warnings)

    def operationResult(self):
        self.toast_message = Driver.wait(self.driver, By.XPATH, "//div[@class='toast-body']").text
