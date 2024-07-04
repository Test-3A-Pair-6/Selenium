from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utils import Driver
from selenium.webdriver.support import expected_conditions as EC


class ProfilePage:

    user_name = None
    password = None
    login_button = None
    my_profile_button_on_top_menu = None
    title_professional_experience = None
    share_dropdown_button = None
    title_share_profile_link = None
    switch_checkbox_element = None
    switch_checkbox_aria_checked = None
    switch_button = None
    copy_icon = None
    header_on_share_link = None
    certification_clickable = None
    linkedin_icon = None
    linkedin_url = None
    evaluation_button_on_top_menu = None
    start_evaluation_button = None
    confirm_start_button = None
    radio_buttons = []
    evaluation_forward_button = None
    other_forward_buttons = None
    iframe_widget_div = None
    main_page_button_on_menu = None

    def __init__(self, driver):
        self.driver = driver

    def login_info(self):
        self.user_name = Driver.wait(self.driver, By.XPATH, "//input[@name=\"email\"]")
        self.password = Driver.wait(self.driver, By.XPATH, "//input[@name=\"password\"]")

    def submit_button(self):
        self.login_button = Driver.wait(self.driver, By.XPATH, "//button[@type=\"submit\"]", "click", 50)

    def find_profile_button_on_top_menu(self):
        self.my_profile_button_on_top_menu = Driver.wait(self.driver, By.XPATH, "//*[@id=\"__next\"]/div/nav/div[1]/ul/li[2]/a", "click", 5)

    def find_professional_job_experience_text(self):
        self.title_professional_experience = Driver.wait(self.driver, By.XPATH, "//*[@id=\"__next\"]/div/main/div/div/div[3]/div/div[1]/div/div[1]/div/span", "click", 5).text

    def find_share_dropdown(self):
        self.share_dropdown_button = Driver.wait(self.driver, By.XPATH, "//*[@id=\"dropdown-basic\"]", "click", 5)

    def find_share_button_title(self):
        self.title_share_profile_link = Driver.wait(self.driver, By.XPATH, "//*[@id=\"__next\"]/div/main/div/div/div[1]/div/div[2]/div[1]/div/div/div/div[2]/label", "visit", 5).text

    def find_switch_checkbox_attribute_value(self):
        self.switch_checkbox_element = Driver.wait(self.driver, By.XPATH, "//*[@id=\"__next\"]/div/main/div/div/div[1]/div/div[2]/div[1]/div/div/div/div[1]/div/input", "visit", 5)
        self.switch_checkbox_aria_checked = self.switch_checkbox_element.get_attribute("aria-checked")

    def find_switch_button(self):
        self.switch_button = Driver.wait(self.driver, By.XPATH, "//*[@id='__next']/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]", "click", 5)

    def find_copy_icon(self):
        self.copy_icon = Driver.wait(self.driver, By.XPATH, "//*[@id=\"__next\"]/div/main/div/div/div[1]/div/div[2]/div[1]/div/div/div/div[2]/div/i", "click", 5)

    def find_header_on_share_link(self):
        self.header_on_share_link = Driver.wait(self.driver, By.XPATH, "//*[@id=\"__next\"]/div/div/div/div[1]/div/div[1]/div/div/div/span[1]", "visit", 5).text

    def find_clickable_certification(self):
        self.certification_clickable = Driver.wait(self.driver, By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[5]/div[1]/div[2]/div[1]/div[1]", "click", 5)

    def find_linkedin_icon(self):
        self.linkedin_icon = Driver.wait(self.driver, By.XPATH, '//*[@id="__next"]/div/main/div/div/div[1]/div/div[2]/div[2]/div/span', "click", 5)

    def find_url_linkedin(self):
        self.linkedin_url = self.driver.current_url
