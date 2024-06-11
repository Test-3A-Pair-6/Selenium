from selenium.common import StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.common.by import By

from utils import Driver


class PageSocialMedia:
    user_name = None
    password = None
    login_button = None
    burger_menu = None
    menu_list = None
    edit_icon = None
    option = None
    account_type = None
    account_url = None
    save_button = None
    toast_message = None
    field_error = None
    media_count = None
    update_icons = None
    remove_icons = None
    update_input = None
    update_button = None
    remove_choice_yes = None

    def __init__(self, driver):
        self.driver = driver

    def home(self):
        self.user_name = self.driver.find_element(By.XPATH, "//input[@name=\"email\"]")
        self.password = self.driver.find_element(By.XPATH, "//input[@name=\"password\"]")
        self.login_button = self.driver.find_element(By.XPATH, "//button[@type=\"submit\"]")
        return self

    def platform(self):
        for attempt in range(3):
            try:
                self.burger_menu = Driver.wait(self.driver, By.XPATH, "//button[@data-bs-toggle=\"offcanvas\"]")
                return
            except StaleElementReferenceException and ElementClickInterceptedException:
                continue
        raise Exception("Element could not be clicked after multiple attempts due to StaleElementReferenceException")

    def mainMenu(self):
        main_menu = self.driver.find_element(By.XPATH, "//ul[@class=\"nav flex-column\"]")
        self.menu_list = main_menu.find_elements(By.TAG_NAME, "a")

    def editIcon(self):
        self.edit_icon = self.driver.find_element(By.CLASS_NAME, "cv-edit-icon")

    def options(self):
        lst = self.driver.find_element(By.CSS_SELECTOR, ".p-2.py-4.mobile-sidebar")
        self.option = lst.find_element(By.XPATH, "//span[contains(text(),'Medya Hesaplarım')]")

    def accountAddPage(self):
        self.account_type = Driver.wait(self.driver, By.CSS_SELECTOR, ".select__input-container input")
        self.account_url = self.driver.find_element(By.NAME, "socialMediaUrl")
        self.save_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='Kaydet']")

    def operationResult(self):
        self.toast_message = Driver.wait(self.driver, By.XPATH, "//div[@class='toast-body']").text

    def errors(self):
        self.field_error = self.driver.find_element(By.CLASS_NAME, "text-danger").text

    def mediaCount(self):
        self.media_count = len(self.driver.find_elements(By.XPATH, "//input[contains(@class, 'form-control')]"))

    def mediaIcons(self):
        self.update_icons = self.driver.find_elements(By.XPATH, "//*[contains(@class, 'fa fa-pencil-square')]")
        self.remove_icons = self.driver.find_elements(By.XPATH, "//*[contains(@class, 'btn social-delete')]")

    def updateFields(self):
        self.update_input = Driver.wait(self.driver, By.XPATH, "//input[@type='text' and @placeholder='https://']")
        self.update_button = Driver.wait(self.driver, By.XPATH,
                                         "//button[@class='btn btn-primary' and text()='Güncelle']")

    def removeChoice(self):
        self.remove_choice_yes = self.driver.find_element(By.XPATH, "//button[@class='btn btn-yes my-3']")
