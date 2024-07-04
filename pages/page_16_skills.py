from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import Driver

class PageSkills:
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

    def skills(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='details pack-bg-2']/button[@class='btn btn-primary w-100 ']")))
        self.driver.find_element(By.XPATH, "//div[@class='details pack-bg-2']/button[@class='btn btn-primary w-100 ']").click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//span[.='Yetkinliklerim']")))
        self.driver.find_element(By.XPATH, "//span[.='Yetkinliklerim']").click()

    def save_button(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/button")))
        self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/button").click()

    def operationResult(self):
        self.toast_message = Driver.wait(self.driver, By.XPATH, "//div[@class='toast-body']").text
        return self.toast_message

    def add_skills(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@class=' css-19bb58m']")))
        self.driver.find_element(By.XPATH, "//div[@class=' css-19bb58m']").click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "react-select-5-option-0")))
        self.driver.find_element(By.ID, "react-select-5-option-1").click()

    def delete_skills(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//button[@class=' grade-delete g-del button-transparent']")))
        self.driver.find_element(By.XPATH, "//button[@class=' grade-delete g-del button-transparent']").click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-yes my-3']")))
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-yes my-3']").click()





