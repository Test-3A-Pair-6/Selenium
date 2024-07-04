from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class PageViewUserProfile:
    login_button = None
    password = None
    user_name = None

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

    def profile_title_control(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='details pack-bg-2']/button[@class='btn btn-primary w-100 ']")))
        self.driver.find_element(By.XPATH, "//div[@class='details pack-bg-2']/button[@class='btn btn-primary w-100 ']").click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//a[.='Deneyimlerim']" )))
        self.driver.find_element(By.XPATH, "//a[.='Deneyimlerim']").click()



