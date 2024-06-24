from selenium.webdriver.common.by import By

from utils import Driver


class PagePlatform:
    user_name = None
    password = None
    login_button = None
    title = None
    app = None
    lessons = None
    my_courses = None
    my_announcements = None
    my_survey = None
    announcements = None
    button_more = None
    exam = None
    report_close = None
    result_close = None
    deneme = None
    button_pack_1 = None
    button_pack_2 = None
    button_pack_3 = None

    def __init__(self, driver):
        self.driver = driver

    def login_info(self):
        self.user_name = Driver.wait(self.driver, By.XPATH, "//input[@name=\"email\"]")
        self.password = Driver.wait(self.driver, By.XPATH, "//input[@name=\"password\"]")

    def submit_button(self):
        self.login_button = Driver.wait(self.driver, By.XPATH, "//button[@type=\"submit\"]", "click", 50)

    def platform(self):
        self.title = Driver.wait(self.driver, By.XPATH, "//span[@class='text-secondary']")
        self.app = Driver.wait(self.driver, By.CSS_SELECTOR, ".status-card.status_accepted")

    def platform_tabs(self):
        self.my_courses = Driver.wait(self.driver, By.XPATH, "//button[@id=\"lessons-tab\"]", "click")
        self.my_announcements = Driver.wait(self.driver, By.XPATH, "//button[@id=\"notification-tab\"]", "click")
        self.my_survey = Driver.wait(self.driver, By.XPATH, "//button[@id=\"mySurvey-tab\"]", "click")

    def lessons_tab(self):
        self.lessons = Driver.multiple_wait(self.driver, By.XPATH,
                                            "//div[@id=\"all-lessons-tab-pane\"]//div[@class=\"col-md-3 col-12 mb-4\"]")

    def more_button_func(self):
        self.button_more = Driver.wait(self.driver, By.XPATH, "//div[@class=\"showMoreBtn\"]")

    def announcement_tab(self):
        self.announcements = Driver.multiple_wait(self.driver, By.XPATH, "//div[@class=\"notfy-card notify\"]")

    def exam_card(self):
        self.exam = Driver.wait(self.driver, By.CLASS_NAME, "exam-card  ")

    def exam_report_card(self):
        self.report_close = Driver.wait(self.driver, By.XPATH, "//button[contains(text(),'Raporu Görüntüle')]")

    def exam_result_card(self):
        self.result_close = Driver.wait(self.driver, By.XPATH, "//button[contains(text(),'Kapat')]")

    def create_profile_card(self):
        self.button_pack_1 = Driver.wait(self.driver, By.XPATH, "//div[@class=\"details pack-bg-2\"]//button")

    def evaluate_yourself_card(self):
        self.button_pack_2 = Driver.wait(self.driver, By.XPATH, "//div[@class=\"details pack-bg-3\"]//button")
        
    def start_learn_card(self):
        self.button_pack_3 = Driver.wait(self.driver, By.XPATH, "//div[@class=\"details pack-bg-1\"]//button")
