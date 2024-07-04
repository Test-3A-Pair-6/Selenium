from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import Constants as const

from utils import Driver

class PageEducation:
    def __init__(self, driver):
        self.driver = driver
        self.user_name = None
        self.password = None
        self.login_button = None

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
        sleep(40)  # Has been added because Tobeto put reCaptcha and told us to manually pass it.
        self.login_button.click()

    def operationResult(self):
        self.toast_message = Driver.wait(self.driver, By.XPATH, "//div[@class='toast-body']").text
        return self.toast_message

    def education_life(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='details pack-bg-2']/button[@class='btn btn-primary w-100 ']")))
        self.driver.find_element(By.XPATH, "//div[@class='details pack-bg-2']/button[@class='btn btn-primary w-100 ']").click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//span[.='Eğitim Hayatım']")))
        self.driver.find_element(By.XPATH, "//span[.='Eğitim Hayatım']").click()
        sleep(5)
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".select__input-container")))
        sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, ".select__input-container").click()
        self.driver.find_element(By.ID, "react-select-5-option-2").click()
        self.driver.find_element(By.NAME, "University").send_keys("Kocaeli Üniversitesi")
        self.driver.find_element(By.NAME, "Department").send_keys("TestUzmanı")
        self.driver.find_element(By.CSS_SELECTOR, ".col-12:nth-child(4) .form-control").send_keys("2020")
        self.driver.find_element(By.CSS_SELECTOR, ".col-12:nth-child(5) .form-control").send_keys("2024")
        self.driver.find_element(By.NAME, "Department").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()



