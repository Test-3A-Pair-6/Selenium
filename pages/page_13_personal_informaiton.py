from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utils import Constants as const, Driver


class PagePersonalInformation:

    iframe_widget_div = None
    user_name = None
    password = None
    login_button = None

    def __init__(self, driver):
        self.driver = driver

    def login_info(self):
        self.user_name = Driver.wait(self.driver, By.XPATH, "//input[@name=\"email\"]")
        self.password = Driver.wait(self.driver, By.XPATH, "//input[@name=\"password\"]")

    def submit_button(self):
        self.login_button = Driver.wait(self.driver, By.XPATH, "//button[@type=\"submit\"]", "click", 50)

    def profile_title_control(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='details pack-bg-2']/button[@class='btn btn-primary w-100 ']")))
        self.driver.find_element(By.XPATH, "//div[@class='details pack-bg-2']/button[@class='btn btn-primary w-100 ']").click()

    def update_personal_information(self):
        self.name = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='name']")))
        self.name.send_keys(const.name)
        self.last_name = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='surname']")))
        self.last_name.send_keys(const.last_name)
        #self.phone_code = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//select[@name='phoneNumberCountry']")))
        #self.driver.find_element(By.XPATH, "//select[@name='phoneNumberCountry']").click()
        #self.phone_code.send_keys(const.phone_code)
        self.phone_number = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='phoneNumber']")))
        self.phone_number.send_keys(const.phone_number)
        self.birth_day = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='birthday']")))
        self.driver.find_element(By.XPATH, "//input[@name='birthday']").click()
        self.birth_day.send_keys(const.birth_day)
        self.id_number = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='identifier']")))
        self.id_number.send_keys(const.id_number)
        self.country = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='country']")))
        self.country.send_keys(const.country)
        self.city = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//select[@name='city']")))
        self.driver.find_element(By.XPATH, "//select[@name='city']").click()
        self.city.send_keys(const.city)
        self.district = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//select[@name='district']")))
        self.driver.find_element(By.XPATH, "//select[@name='district']").click()
        self.district.send_keys(const.district)
        self.neighbourhood = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//textarea[@name='address']")))
        self.neighbourhood.send_keys(const.neighbourhood)
        self.description = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//textarea[@name='description']")))
        self.description.send_keys(const.description)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-primary py-2 mb-3 d-inline-block mobil-btn']")))
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary py-2 mb-3 d-inline-block mobil-btn']").click()


    def add_profile_picture(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='photo-edit-btn cursor-pointer']")))
        self.driver.find_element(By.XPATH, "//div[@class='photo-edit-btn cursor-pointer']").click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='uppy-u-reset uppy-c-btn uppy-Dashboard-browse']")))
        self.driver.find_element(By.XPATH, "//button[@class='uppy-u-reset uppy-c-btn uppy-Dashboard-browse']").click()



    def id_control(self):
        self.name = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='name']")))
        self.name.send_keys(const.name)
        self.last_name = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='surname']")))
        self.last_name.send_keys(const.last_name)
        self.phone_number = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='phoneNumber']")))
        self.phone_number.send_keys(const.phone_number)
        self.birth_day = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='birthday']")))
        self.driver.find_element(By.XPATH, "//input[@name='birthday']").click()
        self.birth_day.send_keys(const.birth_day)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-primary py-2 mb-3 d-inline-block mobil-btn']")))
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-primary py-2 mb-3 d-inline-block mobil-btn']").click()

    def find_widget(self):
        self.iframe_widget_div = Driver.wait(self.driver, By.XPATH, '//*[@id="exaironWebchat"]/div/div', "visit", 5)

    def character_control(self):
        self.neighbourhood_character = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//textarea[@name='address']")))
        self.neighbourhood_character.send_keys(const.neighbourhood_character)
        self.description_character = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//textarea[@name='description']")))
        self.description_character.send_keys(const.description_character)
    def button(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-primary py-2 mb-3 d-inline-block mobil-btn']")))
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary py-2 mb-3 d-inline-block mobil-btn']").click()



