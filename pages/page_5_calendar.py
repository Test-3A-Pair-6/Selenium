from selenium.webdriver.common.by import By

from utils import Driver


class PageCalendar:
    logo = None
    button_calendar = None
    button_ended = None
    button_continue = None
    button_bought = None
    button_not_started = None
    lesson_list = None
    button_lesson_search = None
    button_instructor_search = None
    searched_lesson_list = None
    toolbar_title = None
    date_forward = None
    button_day = None
    button_week = None
    button_month = None
    button_today = None
    button_close = None

    def __init__(self, driver):
        self.driver = driver

    def main_page(self):
        self.logo = Driver.wait(self.driver, By.XPATH, "//img[contains(@alt,'Tobeto Logo')]")
        self.button_calendar = Driver.wait(self.driver, By.CLASS_NAME, "calendar-btn")

    def calendar_page(self):
        self.button_ended = Driver.wait(self.driver, By.XPATH, "//input[@name=\"eventEnded\"]")
        self.button_continue = Driver.wait(self.driver, By.XPATH, "//input[@name=\"eventContinue\"]")
        self.button_bought = Driver.wait(self.driver, By.XPATH, "//input[@name=\"eventBuyed\"]")
        self.button_not_started = Driver.wait(self.driver, By.XPATH, "//input[@name=\"eventNotStarted\"]")
        self.button_lesson_search = Driver.wait(self.driver, By.ID, "search-event")
        self.button_instructor_search = Driver.wait(self.driver, By.XPATH,
                                                    "//div[contains(@class,'css-19bb58m')]//input")
        self.button_close = Driver.wait(self.driver, By.CSS_SELECTOR, ".btn-close.btn-close-white")

    def buttons_clicked(self):
        self.lesson_list = self.driver.find_elements(By.XPATH, "//div[@class='fc-daygrid-event-harness']"
                                                               "//span[@class=\"text-truncate\"]")

    def searched(self):
        self.searched_lesson_list = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'fc-event-main')]"
                                                                        "//span[@class=\"text-truncate\"]")

    def toolbar(self):
        self.toolbar_title = Driver.wait(self.driver, By.CLASS_NAME, "fc-toolbar-title")

    def date_orientation(self):
        self.toolbar()
        self.date_forward = Driver.wait(self.driver, By.CSS_SELECTOR, ".fc-icon.fc-icon-chevron-right")
        self.button_day = Driver.wait(self.driver, By.XPATH, "//button[@title='Gün']")
        self.button_week = Driver.wait(self.driver, By.XPATH, "//button[@title='Hafta']")
        self.button_month = Driver.wait(self.driver, By.XPATH, "//button[@title='Ay']")
        self.button_today = Driver.wait(self.driver, By.XPATH, "//button[@title='Bugün']")
