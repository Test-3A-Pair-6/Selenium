from time import sleep

from selenium.common import WebDriverException, NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import Constants as const

from utils import Driver

class PageExperiences:
    company_name = None
    position = None
    sector = None
    job_desc = None

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
        sleep(30)  # Has been added because Tobeto put reCaptcha and told us to manually pass it.
        self.login_button.click()

    def click_element(self, element):
        """
        Some elements unexpectedly accept a click pattern that other elements don't and
        don't allow to execute the other pattern, so this method will solve this problem in one line.
        Attempts to click on the given element. If the conventional click fails,
        Performs a click operation with JavaScript.

        To call:
        self.click_element(element)
        """
        try:
            element.click()
            print("Element clicked successfully.")
        except NoSuchElementException:
            print("Element not found.")
        except WebDriverException as e:
            print(f"Normal click failed: {e}. JavaScript will try clicking.")
            try:
                self.driver.execute_script("arguments[0].click()", element)
                print("Clicking with JavaScript was successful.")
            except Exception as js_e:
                print(f"The JavaScript click also failed: {js_e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


    def operationResult(self):
        self.toast_message = Driver.wait(self.driver, By.XPATH, "//div[@class='toast-body']").text
        return self.toast_message

    def go_to_profile(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
            (By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button")))
        self.driver.find_element(By.XPATH,
                                 "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button").click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
            (By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[2]/span[2]")))
        self.driver.find_element(By.XPATH,
                                 "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[2]/span[2]").click()


    def succes_experiences(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                              "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/input[1]")))
        self.company_name = self.driver.find_element(By.NAME, "corporationName").send_keys("TOBETO")
        self.position = self.driver.find_element(By.NAME, "position").send_keys("YAZILIM TEST")
        self.driver.find_element(By.CSS_SELECTOR, ".select__input-container").click()
        self.driver.find_element(By.ID, "react-select-5-option-0").click()
        dropdown = self.driver.find_element(By.NAME, "country")
        dropdown.find_element(By.XPATH, "//option[. = 'İstanbul']").click()
        self.sector = self.driver.find_element(By.NAME, "sector").send_keys("YAZILIM")
        self.driver.find_element(By.XPATH,
                                 "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[6]/div/div/input").send_keys(
            "03.01.2020")
        self.driver.find_element(By.XPATH,
                                 "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[7]/div/div/input").send_keys(
            "11.02.2024")

    def job_description(self):
        job_desc = self.driver.find_element(By.CSS_SELECTOR, ".col-md-12 > .form-control")
        job_desc.click()
        job_desc.send_keys("TOBETO")

    submit = None

    def save_button(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-primary py-2 mb-3 d-inline-block mobil-btn']")))
        self.submit = self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary py-2 mb-3 d-inline-block mobil-btn']")
        self.click_element(self.submit)

    def empty_experiences(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
            (By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[1]/span")))
        assert self.driver.find_element(By.XPATH,
                                        "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[1]/span").text == "Doldurulması zorunlu alan*"
        assert self.driver.find_element(By.XPATH,
                                        "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[2]/span").text == "Doldurulması zorunlu alan*"
        assert self.driver.find_element(By.XPATH,
                                        "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[4]/span").text == "Doldurulması zorunlu alan*"

    def many_characters_jobDesc(self):
        job_desc = self.driver.find_element(By.CSS_SELECTOR, ".col-md-12 > .form-control")
        job_desc.click()
        job_desc.send_keys(
            "jwhfelwfhewıjekwjroejflkdncm xcöçmflkgoprtjgkfnvjbdkfherkjfbdsjlkdmekjıephfjkdbcnlskdjwoıdefnrjbruhfbjkdsnjcduehdjewfuhcjknekfhcnjechckjucbdkjehfkejufhdwkjuhoıjfıvrohınvfjkrehruhvkjfrbfkedbfjhrheıcbucbugrhfebkkjjcdjehurfrhrbhrbjejrygbrebjdbjfbcbcjehcljcnkjfhurhgvjfvneogtırvnrtuvbnjfruvhbfruhvjucnjddjjkk")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-primary")))
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
            (By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[8]/span")))
        assert self.driver.find_element(By.XPATH,
                                        "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[8]/span").text == "En fazla 300 karakter girebilirsiniz"

    def min_characters(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                              "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/input[1]")))
        self.company_name = self.driver.find_element(By.NAME, "corporationName").send_keys("TOBE")
        self.position = self.driver.find_element(By.NAME, "position").send_keys("YAZI")
        self.driver.find_element(By.CSS_SELECTOR, ".select__input-container").click()
        self.driver.find_element(By.ID, "react-select-5-option-0").click()
        dropdown = self.driver.find_element(By.NAME, "country")
        dropdown.find_element(By.XPATH, "//option[. = 'İstanbul']").click()
        self.sector = self.driver.find_element(By.NAME, "sector").send_keys("YAZI")
        self.driver.find_element(By.XPATH,
                                 "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[6]/div/div/input").send_keys(
            "03.01.2020")
        self.driver.find_element(By.XPATH,
                                 "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[7]/div/div/input").send_keys(
            "11.02.2024")
        job_desc = self.driver.find_element(By.CSS_SELECTOR, ".col-md-12 > .form-control")
        job_desc.click()
        job_desc.send_keys("TOBETO")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
            (By.XPATH, "//button[@class='btn btn-primary py-2 mb-3 d-inline-block mobil-btn']")))
        self.driver.find_element(By.XPATH,
                                 "//button[@class='btn btn-primary py-2 mb-3 d-inline-block mobil-btn']").click()

    def tangermsg(self):
        self.tanger_message = Driver.wait(self.driver, By.XPATH, "//span[@class='text-danger']").text
        return self.tanger_message

    def many_character(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                              "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/input[1]")))
        self.company_name = self.driver.find_element(By.NAME, "corporationName").send_keys("TOBEhgjjfldşsmncjklömsbxjklşfındndkfmgjvmfngbvbmfnchfhg")
        self.position = self.driver.find_element(By.NAME, "position").send_keys("YAZIjfhdgfhfhfhfhgnvjgjgjgjgjgjgjgjgkfldşfgjgjgjgbfnvbg5bghb")
        self.driver.find_element(By.CSS_SELECTOR, ".select__input-container").click()
        self.driver.find_element(By.ID, "react-select-5-option-0").click()
        dropdown = self.driver.find_element(By.NAME, "country")
        dropdown.find_element(By.XPATH, "//option[. = 'İstanbul']").click()
        self.sector = self.driver.find_element(By.NAME, "sector").send_keys("YAZInvnvnvnvnvnvnvnvgıyutırofhgjbvnggjtjfjfjgotjgkhjgjgk")
        self.driver.find_element(By.XPATH,
                                 "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[6]/div/div/input").send_keys(
            "03.01.2020")
        self.driver.find_element(By.XPATH,
                                 "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[7]/div/div/input").send_keys(
            "11.02.2024")
        job_desc = self.driver.find_element(By.CSS_SELECTOR, ".col-md-12 > .form-control")
        job_desc.click()
        job_desc.send_keys("TOBETO")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
            (By.XPATH, "//button[@class='btn btn-primary py-2 mb-3 d-inline-block mobil-btn']")))
        self.driver.find_element(By.XPATH,
                                 "//button[@class='btn btn-primary py-2 mb-3 d-inline-block mobil-btn']").click()

