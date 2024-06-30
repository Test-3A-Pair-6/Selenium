from selenium.webdriver.common.by import By
from datetime import datetime

from utils import Driver


def convert_str_to_date(date_str):
    date_format = "%d.%m.%Y"  # Day, Month, Year
    return datetime.strptime(date_str, date_format)


class AnnouncementNews:
    user_name = None
    password = None
    login_button = None
    announcements = None
    more_announcements = None
    first_announcement_definitive_title = None
    main_title_my_announcements = None
    first_notify_card = None
    second_notify_card = None
    third_notify_card = None
    forth_notify_card = None
    fifth_notify_card = None
    sixth_notify_card = None
    seventh_notify_card = None
    eighth_notify_card = None
    ninth_notify_card = None
    all_notify_cards = None
    sort_dropdown_button = None
    sort_asc_button = None
    sort_desc_button = None
    first_announcement_date_text = None
    first_announcement_date_format = None
    date_element = None
    last_announcement_date_element = None
    forward_button = None
    tab_index_forward_button = None
    last_announcement_date_format = None
    announcement_type_dropdown_button = None
    type_news_button = None
    type_announcement_button = None
    info_no_announcement_found = None
    definitive_title_on_first_card = None
    search_bar = None
    search_button = None
    first_announcement_header = None

    def __init__(self, driver):
        self.driver = driver

    def login_info(self):
        self.user_name = Driver.wait(self.driver, By.XPATH, "//input[@name=\"email\"]")
        self.password = Driver.wait(self.driver, By.XPATH, "//input[@name=\"password\"]")

    def submit_button(self):
        self.login_button = Driver.wait(self.driver, By.XPATH, "//button[@type=\"submit\"]", "click", 50)

    def announcements_tab(self):
        self.announcements = Driver.wait(self.driver, By.XPATH, "//*[@id=\"notification-tab\"]")

    def announcement_definitive_title(self):
        self.first_announcement_definitive_title = Driver.wait(self.driver, By.XPATH, "//*[@id=\"notification-tab-pane\"]/div/div[1]/div/div[1]/div/span[1]", "visit", 5).text

    def show_more_announcements_button(self):
        self.more_announcements = Driver.wait(self.driver, By.XPATH, "//*[@id=\"notification-tab-pane\"]/div/div[4]")

    def my_all_announcements_title(self):
        self.main_title_my_announcements = Driver.wait(self.driver, By.XPATH, "//*[@id=\"__next\"]/div/main/div[1]/div/div/div/span").text

    def finding_all_notify_cards(self):
        self.first_notify_card = Driver.wait(self.driver, By.XPATH, "//*[@id=\"__next\"]/div/main/div[2]/div[2]/div[1]/div/div[1]/div/span[1]", "visit", 2).text
        self.second_notify_card = Driver.wait(self.driver, By.XPATH, "//*[@id=\"__next\"]/div/main/div[2]/div[2]/div[2]/div/div[1]/div/span[1]", "visit", 2).text
        self.third_notify_card = Driver.wait(self.driver, By.XPATH, "//*[@id=\"__next\"]/div/main/div[2]/div[2]/div[3]/div/div[1]/div/span[1]", "visit", 2).text
        self.forth_notify_card = Driver.wait(self.driver, By.XPATH, "//*[@id=\"__next\"]/div/main/div[2]/div[2]/div[4]/div/div[1]/div/span[1]", "visit", 2).text
        self.fifth_notify_card = Driver.wait(self.driver, By.XPATH, "//*[@id=\"__next\"]/div/main/div[2]/div[2]/div[5]/div/div[1]/div/span[1]", "visit", 2).text
        self.sixth_notify_card = Driver.wait(self.driver, By.XPATH, "//*[@id=\"__next\"]/div/main/div[2]/div[2]/div[6]/div/div[1]/div/span[1]", "visit", 2).text
        self.seventh_notify_card = Driver.wait(self.driver, By.XPATH, "//*[@id=\"__next\"]/div/main/div[2]/div[2]/div[7]/div/div[1]/div/span[1]", "visit", 2).text
        self.eighth_notify_card = Driver.wait(self.driver, By.XPATH, "//*[@id=\"__next\"]/div/main/div[2]/div[2]/div[8]/div/div[1]/div/span[1]", "visit", 2).text
        self.ninth_notify_card = Driver.wait(self.driver, By.XPATH, "//*[@id=\"__next\"]/div/main/div[2]/div[2]/div[9]/div/div[1]/div/span[1]", "visit", 2).text
        self.all_notify_cards = [self.first_notify_card, self.second_notify_card, self.third_notify_card, self.forth_notify_card, self.fifth_notify_card, self.sixth_notify_card, self.seventh_notify_card, self.eighth_notify_card, self.ninth_notify_card]
        self.driver.execute_script("window.scrollTo(0, 500);")

    def find_sort_dropdown_button(self):
        self.sort_dropdown_button = Driver.wait(self.driver, By.XPATH, "//*[@id=\"__next\"]/div/main/div[2]/div[1]/div/div[4]/div[1]/button", "click", 5)

    def find_sort_asc_button(self):
        self.sort_asc_button = Driver.wait(self.driver, By.XPATH, "//*[@id=\"__next\"]/div/main/div[2]/div[1]/div/div[4]/div[1]/ul/li[2]/a", "click", 5)

    def find_sort_desc_button(self):
        self.sort_desc_button = Driver.wait(self.driver, By.XPATH, "//*[@id=\"__next\"]/div/main/div[2]/div[1]/div/div[4]/div[1]/ul/li[1]/a", "click", 5)

    def find_first_announcement_date(self):
        self.first_announcement_date_text = Driver.wait(self.driver, By.XPATH, "//*[@id=\"__next\"]/div/main/div[2]/div[2]/div[1]/div/div[2]/span[1]", "visit", 5).text
        self.first_announcement_date_format = convert_str_to_date(self.first_announcement_date_text)

    def countdown_for_last_announcement(self):
        div_count = 9

        while div_count >= 1:
            xpath = f"//*[@id=\"__next\"]/div/main/div[2]/div[2]/div[{div_count}]/div/div[2]/span[1]"

            try:
                # finds element begins from 9
                # print(xpath)
                self.date_element = Driver.wait(self.driver, By.XPATH, xpath, "visit", 2)
                self.last_announcement_date_element = self.date_element.text  # last_announcement found
                break
            except Exception as e:
                print(f"This one is the last one: {e}")
                div_count -= 1  # So specific div number will go down to check others

        if self.last_announcement_date_element is None:
            print("None of them have been found")

    def find_forward_button_for_announcements(self):
        self.driver.execute_script("window.scrollTo(0, 300);")
        self.forward_button = Driver.wait(self.driver, By.XPATH, "//*[@id=\"__next\"]/div/main/div[2]/div[2]/ul/li[5]/a", "click", 5)
        self.tab_index_forward_button = self.forward_button.get_attribute("tabindex")

    def converting_announcements_str_to_date(self):
        self.countdown_for_last_announcement()
        self.last_announcement_date_format = convert_str_to_date(self.last_announcement_date_element)

    def find_type_dropdown_button(self):
        self.announcement_type_dropdown_button = Driver.wait(self.driver, By.XPATH, "//*[@id=\"__next\"]/div/main/div[2]/div[1]/div/div[2]/button", "click", 5)

    def find_type_news_button(self):
        self.type_news_button = Driver.wait(self.driver, By.XPATH, "//*[@id=\"typeNews\"]", "click", 5)

    def find_type_announcement_button(self):
        self.type_announcement_button = Driver.wait(self.driver, By.XPATH, "//*[@id=\"typeAnnouncement\"]", "click", 5)

    def find_no_announcement_info(self):
        self.info_no_announcement_found = Driver.wait(self.driver, By.XPATH, "//*[@id=\"__next\"]/div/main/div[2]/div[2]/div/p", "visit", 5).text

    def find_definitive_title_on_first_card(self):  # this one has different xpath because its on all announcements tab
        self.definitive_title_on_first_card = Driver.wait(self.driver, By.XPATH, "//*[@id=\"__next\"]/div/main/div[2]/div[2]/div[1]/div/div[1]/div/span[1]", "visit", 5).text

    def find_search_bar(self):
        self.search_bar = Driver.wait(self.driver, By.XPATH, "//*[@id=\"search\"]", "click", 5)

    def find_search_button(self):
        self.search_button = Driver.wait(self.driver, By.XPATH, "//*[@id=\"__next\"]/div/main/div[2]/div[1]/div/div[1]/button", "click", 5)

    def find_first_announcement_header(self):
        self.first_announcement_header = Driver.wait(self.driver, By.XPATH, "//*[@id=\"__next\"]/div/main/div[2]/div[2]/div[1]/div/div[1]/span", "visit", 5).text