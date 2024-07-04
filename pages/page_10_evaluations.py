from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utils import Driver
from selenium.webdriver.support import expected_conditions as EC


class EvaluationsPage:

    user_name = None
    password = None
    login_button = None
    evaluations_button_on_top_menu = None
    start_evaluations_button = None
    confirm_start_button = None
    radio_buttons = []
    evaluations_forward_button = None
    other_forward_buttons = None
    iframe_widget_div = None
    main_page_button_on_menu = None
    front_end_exam_start_button = None
    start_to_exam_button = None
    exam_first_option = None
    exam_next_button = None
    exam_done_text = None


    def __init__(self, driver):
        self.driver = driver

    def login_info(self):
        self.user_name = Driver.wait(self.driver, By.XPATH, "//input[@name=\"email\"]")
        self.password = Driver.wait(self.driver, By.XPATH, "//input[@name=\"password\"]")

    def submit_button(self):
        self.login_button = Driver.wait(self.driver, By.XPATH, "//button[@type=\"submit\"]", "click", 50)

    def find_evaluations_button(self):
        self.evaluations_button_on_top_menu = Driver.wait(self.driver, By.XPATH,
                                                         '//*[@id="__next"]/div/nav/div[1]/ul/li[3]/a', "click", 5)

    def find_start_button_for_evaluations(self):
        self.start_evaluations_button = Driver.wait(self.driver, By.XPATH,
                                                   '//*[@id="__next"]/div/main/section[2]/div/div/div[1]/div/a',
                                                   "click", 5)

    def find_confirm_start_button(self):
        self.confirm_start_button = Driver.wait(self.driver, By.XPATH,
                                                '//*[@id="__next"]/div/main/section/div/div/div/div[3]/a', "click", 5)

    def find_radio_buttons(self):
        self.radio_buttons = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//input[@value='1']")))

    def find_evaluations_forward_button(self):
        self.evaluations_forward_button = Driver.wait(self.driver, By.XPATH,
                                                     '//*[@id="__next"]/div/main/section/div/div/div[2]/div[2]/button',
                                                     "click", 5)

    def find_other_forward_buttons(self):
        self.other_forward_buttons = Driver.wait(self.driver, By.XPATH,
                                                 '//*[@id="__next"]/div/main/section/div/div/div[2]/div[2]/button[2]',
                                                 "click", 5)

    def find_widget(self):
        self.iframe_widget_div = Driver.wait(self.driver, By.XPATH, '//*[@id="exaironWebchat"]/div/div', "visit", 5)

    def find_main_page_on_top_menu(self):
        self.main_page_button_on_menu = Driver.wait(self.driver, By.XPATH,
                                                    '//*[@id="__next"]/div/nav/div[1]/ul/li[1]/a', "click", 5)

    def find_front_end_exam_start_button(self):
        self.front_end_exam_start_button = Driver.wait(self.driver, By.XPATH, '//*[@id="__next"]/div/main/section[2]/div/div/div[4]/div/div[1]/button', "click", 5)

    def find_start_exam_button(self):
        self.start_to_exam_button = Driver.wait(self.driver, By.XPATH, '/html/body/div[5]/div/div/div/div/div[2]/div[2]/button', "click", 5)

    def find_exam_options(self):
        self.exam_first_option = Driver.wait(self.driver, By.XPATH, "//button[@class='option ']", "click", 5)

    def find_exam_next_button(self):
        self.exam_next_button = Driver.wait(self.driver, By.XPATH, "//button[@class='btn btn-next']", "click", 5)

    def find_exam_done_text(self):
        self.exam_done_text = Driver.wait(self.driver, By.CSS_SELECTOR, 'body > div.fade.modal.show > div > div > div > div > div > span', "visit", 5).text

