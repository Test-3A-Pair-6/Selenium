import os
from time import sleep
import pytest

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


from pages import page_8_announcements
from utils import Driver
from utils import Constants as const
from utils import ConfigReader as cr


class TestAnnouncementNews:
    def setup_method(self):
        self.driver = Driver.get_driver()
        self.driver.get(cr.read_config("url_main"))
        self.page = page_8_announcements.AnnouncementNews(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def login(self):
        self.page.login_info()
        self.page.user_name.send_keys(const.user_mail_ismet)
        self.page.password.send_keys(const.user_password_ismet)
        self.page.submit_button()
        self.driver.execute_script("arguments[0].click();", self.page.login_button)

    def navigate_to_first_announcements_tab(self):
        self.login()
        self.page.announcements_tab()
        self.driver.execute_script("arguments[0].click();", self.page.announcements)

    def navigate_to_all_announcements(self):
       self.navigate_to_first_announcements_tab()
       self.page.show_more_announcements_button()
       self.driver.execute_script("arguments[0].click();", self.page.more_announcements)

    def navigate_sort_announcements(self):
        self.navigate_to_all_announcements()
        self.page.find_sort_dropdown_button()
        self.driver.execute_script("arguments[0].click();", self.page.sort_dropdown_button)

    def sort_announcements_by_date_asc(self):
        self.navigate_sort_announcements()
        self.page.find_sort_asc_button()
        self.driver.execute_script("arguments[0].click();", self.page.sort_asc_button)
        self.driver.execute_script("window.scrollTo(0, 350);")
        sleep(1)
        Driver.screenshot(self.driver, "../screenshots/screenshots_8_announcements", "oldest_Announcement_on_first_page.png")

    def sort_announcements_by_date_desc(self):
        self.navigate_sort_announcements()
        self.page.find_sort_desc_button()
        self.driver.execute_script("arguments[0].click();", self.page.sort_desc_button)
        self.driver.execute_script("window.scrollTo(0, 350);")
        sleep(1)
        Driver.screenshot(self.driver, "../screenshots/screenshots_8_announcements",
                          "latest_Announcement_on_first_page.png")

    def click_forward_until_last_page(self):
        while True:
            self.page.find_forward_button_for_announcements()
            tab_index_str = self.page.tab_index_forward_button
            tab_index = int(tab_index_str)

            if tab_index == -1:
                break

            self.driver.execute_script("arguments[0].click()", self.page.forward_button)

        print("Last Announcement")
        sleep(2)

    def find_last_announcement(self):
        self.click_forward_until_last_page()
        self.page.countdown_for_last_announcement()

    def navigating_to_type_dropdown(self):
        self.navigate_to_all_announcements()
        self.page.find_type_dropdown_button()
        self.driver.execute_script("arguments[0].click()", self.page.announcement_type_dropdown_button)

    def navigating_to_news_type(self):
        self.navigating_to_type_dropdown()
        self.page.find_type_news_button()
        self.driver.execute_script("arguments[0].click()", self.page.type_news_button)
        self.driver.execute_script("window.scrollTo(0, 150);")

    def navigating_to_announcement_type(self):
        self.navigating_to_type_dropdown()
        self.page.find_type_announcement_button()
        self.driver.execute_script("arguments[0].click()", self.page.type_announcement_button)
        self.driver.execute_script("window.scrollTo(0, 150);")

    def input_text_into_search_bar(self):
        self.navigate_to_all_announcements()
        self.page.find_search_bar()
        self.page.find_search_button()
        self.page.search_bar.send_keys(const.search_bar_input_text)
        self.driver.execute_script("arguments[0].click()", self.page.search_button)
        self.driver.execute_script("window.scrollTo(0, 150);")
        sleep(2)
        self.page.find_first_announcement_header()  # Should be called after search
        self.header = self.page.first_announcement_header


    def test_navigate_first_announcements_tab(self):
        self.navigate_to_first_announcements_tab()
        self.page.announcement_definitive_title()
        assert self.page.first_announcement_definitive_title == const.announcement_definitive_title, "Driver is not on announcement tab"
        Driver.screenshot(self.driver, "../screenshots/screenshots_8_announcements", "onAnnouncementsTab.png")

    def test_navigate_to_all_announcements(self):
        self.navigate_to_all_announcements()
        self.page.my_all_announcements_title()
        assert self.page.main_title_my_announcements == const.main_announcement_title, "Driver has not navigated to all announcements"
        Driver.screenshot(self.driver, "../screenshots/screenshots_8_announcements", "onAll_AnnouncementsTab.png")

    def test_checking_nine_announcements(self):
        self.navigate_to_all_announcements()
        sleep(2)
        self.driver.refresh()
        self.page.finding_all_notify_cards()
        for card_title in self.page.all_notify_cards:
            assert card_title == const.announcement_definitive_title, f"Attention {card_title} is not matching"
        sleep(1)
        Driver.screenshot(self.driver, "../screenshots/screenshots_8_announcements", "found_All_Announcements.png")

    def test_sort_announcements_by_date_asc(self):
        self.sort_announcements_by_date_asc()  # changes order from previous to latest
        self.page.find_first_announcement_date()
        self.click_forward_until_last_page()  # keeps clicking until the last page
        Driver.screenshot(self.driver, "../screenshots/screenshots_8_announcements", "latest_Announcement_on_last_page.png")
        self.page.converting_announcements_str_to_date()
        first_date = self.page.first_announcement_date_format
        last_date = self.page.last_announcement_date_format
        if first_date != last_date:
            assert last_date > first_date, "Sorting is working on the contrary"
        else:
            print("All announcements are on the same day.")
        print("Sorting is working properly from previous to latest")

    def test_sort_announcements_by_date_desc(self):
        self.sort_announcements_by_date_desc()  # changes order from previous to latest
        self.page.find_first_announcement_date()
        self.click_forward_until_last_page()  # keeps clicking until the last page
        Driver.screenshot(self.driver, "../screenshots/screenshots_8_announcements", "oldest_Announcement_on_last_page.png")
        self.page.converting_announcements_str_to_date()
        first_date = self.page.first_announcement_date_format
        last_date = self.page.last_announcement_date_format
        if first_date != last_date:
            assert last_date < first_date, "Sorting is working on the contrary"
        else:
            print("All announcements are on the same day.")
        print("Sorting is working properly from previous to latest")

    def test_type_no_news(self):
        self.navigating_to_news_type()
        self.page.find_no_announcement_info()
        assert self.page.info_no_announcement_found == const.no_announcement_found_message, "Page is not empty"
        Driver.screenshot(self.driver, "../screenshots/screenshots_8_announcements", "no_type_news.png")

    def test_type_announcements(self):
        self.navigating_to_announcement_type()
        self.page.find_definitive_title_on_first_card()
        assert self.page.definitive_title_on_first_card == const.announcement_definitive_title, "Driver is not on announcement tab"
        Driver.screenshot(self.driver, "../screenshots/screenshots_8_announcements", "typeAnnouncements_matches.png")

    def test_input_into_search_bar(self):
        self.input_text_into_search_bar()
        assert const.search_bar_input_text in self.header, "Results have not matched with input"
        Driver.screenshot(self.driver, "../screenshots/screenshots_8_announcements", "search_bar_input_Announcements_matches.png")
