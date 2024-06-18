from time import sleep

from selenium.webdriver import Keys
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

    def add_language(self):
        try:
            dropdown1 = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#__next > div > main > section > div > div > div.col-12.col-lg-9 > form > div > div:nth-child(1) > div > div"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", dropdown1)
            dropdown1.click()
            option1_xpath = "//div[contains(@class, 'select__option') and text()='Arapça']"
            option1 = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, option1_xpath))
            )
            option1.click()

            dropdown2 = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#__next > div > main > section > div > div > div.col-12.col-lg-9 > form > div > div:nth-child(2) > div > div"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", dropdown2)
            dropdown2.click()
            option2_xpath = "//div[contains(@class, 'select__option') and text()=' Temel Seviye (A1, A2)']"
            option2 = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, option2_xpath))
            )
            option2.click()

            save_button_xpath = "//button[contains(@class, 'btn-primary') and contains(text(), 'Kaydet')]"
            save_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, save_button_xpath))
            )
            save_button.click()

        except Exception as e:
            print("Error adding language:", e)
            print(self.driver.page_source)

    def operationResult(self):
        self.toast_message = Driver.wait(self.driver, By.XPATH, "//div[@class='toast-body']").text
