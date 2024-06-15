from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import Driver

class PageCertificateCRUD:
    def __init__(self, driver):
        self.driver = driver
        self.user_name = None
        self.password = None
        self.login_button = None
        self.certificate_name_input = None
        self.year_element = None
        self.file_input = None
        self.submit_button = None
        self.first_row_element = None
        self.toast_message = ""

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
        sleep(20)
        self.login_button.click()
    
    def navigate_to_certificates(self, url):
        self.driver.get(url)
    
    def add_certificate(self, certificate_name, year, pdf_path):
        self.certificate_name_input = self.driver.find_element(By.NAME, "CertificateName")
        self.certificate_name_input.send_keys(certificate_name, Keys.TAB)

        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "react-datepicker__year-text"))
        )
        self.year_element = self.driver.find_element(By.XPATH, f"//div[contains(@class, 'react-datepicker__year-text') and text()='{year}']")
        self.year_element.click()

        self.file_input = self.driver.find_element(By.XPATH, "//input[@class='uppy-Dashboard-input' and not(@webkitdirectory)]")
        self.file_input.send_keys(pdf_path)

    def save_valid_certificate(self):
        uploaded_file_name_xpath = "//p[contains(text(), 'Python_Essentials_1_Badge20240523-8-9tn7xa.pdf')]"
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, uploaded_file_name_xpath))
        )

        submit_btn_selector = "#__next > div > main > section > div > div > div.col-12.col-lg-9 > div.row > form > div.w-100.d-flex.justify-content-center > button"
        self.submit_button = self.driver.find_element(By.CSS_SELECTOR, submit_btn_selector)
        self.submit_button.click()

    def verify_certificate_added(self, expected_certificate_name):
        table_xpath = "//div[contains(@class, 'table-responsive-sm')]//table"
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, table_xpath))
        )

        first_row_xpath = "//div[contains(@class, 'table-responsive-sm')]//table/tbody/tr[1]/td[1]"
        self.first_row_element = self.driver.find_element(By.XPATH, first_row_xpath)
        assert self.first_row_element.text == expected_certificate_name, f"Expected '{expected_certificate_name}', but got {self.first_row_element.text}"
    
    def verify_invalid_certificate_error(self, invalid_certificate_message):
        informer_xpath = "//div[@class='uppy-Informer-animated']/p"
        error_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, informer_xpath))
        )
        assert invalid_certificate_message in error_element.text, f"Expected error message not found, got {error_element.text}"

    def delete_certificate(self):
        delete_button_xpath = "//div[contains(@class, 'table-responsive-sm')]//table/tbody/tr[1]//span[contains(@class, 'trashIcon')]"
        delete_button = self.driver.find_element(By.XPATH, delete_button_xpath)
        self.driver.execute_script("arguments[0].click();", delete_button)

        alert_delete_xpath = "//button[contains(@class, 'btn btn-yes my-3')]"
        yes_btn = self.driver.find_element(By.XPATH, alert_delete_xpath)
        yes_btn.click()

    def operationResult(self):
        self.toast_message = Driver.wait(self.driver, By.XPATH, "//div[@class='toast-body']").text