from selenium.webdriver.common.by import By

from utils import Driver


class PageTrainings:
    user_name = None
    password = None
    login_button = None
    my_courses = None
    lessons = None
    button_more = None
    button_favorite = None
    button_like = None
    button_about = None
    like_before = None
    like_after = None

    def __init__(self, driver):
        self.driver = driver

    def login_info(self):
        self.user_name = Driver.wait(self.driver, By.XPATH, "//input[@name=\"email\"]")
        self.password = Driver.wait(self.driver, By.XPATH, "//input[@name=\"password\"]")

    def submit_button(self):
        self.login_button = Driver.wait(self.driver, By.XPATH, "//button[@type=\"submit\"]", "click", 50)

    def platform(self):
        self.my_courses = Driver.wait(self.driver, By.XPATH, "//button[@id=\"lessons-tab\"]", "click")

    def lessons_tab(self):
        self.lessons = Driver.multiple_wait(self.driver, By.XPATH,
                                            "//div[@id=\"all-lessons-tab-pane\"]//div[@class=\"col-md-3 col-12 mb-4\"]")

    def more_button_func(self):
        self.button_more = Driver.wait(self.driver, By.XPATH, "//div[@class=\"showMoreBtn\"]")

    def lesson_content(self):
        self.button_favorite = Driver.wait(self.driver, By.CLASS_NAME, "activity-favorite")
        self.button_like = Driver.wait(self.driver, By.XPATH, "//div[@id='main-content']")
        self.button_about = Driver.wait(self.driver, By.XPATH, "//div[@data-node-key='about']")
        self.like_before = Driver.wait(self.driver, By.XPATH, "//span[@class='like-text']//span")

    def toast_message(self):
        return Driver.wait(self.driver, By.XPATH, "//div[@class='growl-item-content']").text

    def like_after_func(self):
        self.like_after = Driver.wait(self.driver, By.XPATH, "//span[@class='like-text liked']//span")

