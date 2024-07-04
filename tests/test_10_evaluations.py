import os
import pytest
import pyperclip
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages import page_10_evaluations
from utils import Driver
from utils import Constants as const
from utils import ConfigReader as cr
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.action_chains import ActionChains


class TestEvaluations:

    def setup_method(self):
        self.driver = Driver.get_driver()
        self.driver.get(cr.read_config("url_main"))
        self.page = page_10_evaluations.EvaluationsPage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def login(self):
        self.page.login_info()
        self.page.user_name.send_keys(const.valid_user_name)
        self.page.password.send_keys(const.valid_password)
        self.page.submit_button()
        self.driver.execute_script("arguments[0].click();", self.page.login_button)

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

    def get_new_url(self):
        self.new_url = self.driver.current_url
        print(self.new_url)

    def navigating_to_evaluations_page(self):
        self.login()
        self.page.find_evaluations_button()
        self.click_element(self.page.evaluations_button_on_top_menu)

    def navigating_to_evaluations_modul(self):
        self.navigating_to_evaluations_page()
        self.page.find_start_button_for_evaluations()
        self.click_element(self.page.start_evaluations_button)
        self.driver.execute_script("window.scrollTo(0, 650);")
        self.page.find_confirm_start_button()
        self.click_element(self.page.confirm_start_button)

    def hide_widget_div(self):
        self.page.find_widget()
        try:
            iframe_widget = self.page.iframe_widget_div
            self.driver.execute_script("arguments[0].style.display = 'none';", iframe_widget)
        except NoSuchElementException:
            pass

    def click_on_radio_buttons(self):
        self.page.find_radio_buttons()
        actions = ActionChains(self.driver)

        # Iterate through each radio button and click it
        for radio_button in self.page.radio_buttons:
            # Ensure the element is clickable before clicking
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(radio_button))

            # Scroll to the radio button
            actions.move_to_element(radio_button).perform()

            # Click the radio button
            radio_button.click()
            counter = 1
            name_attribute = radio_button.get_attribute('name')
            print(f"Click {counter}: Name attribute of the button is '{name_attribute}'")

            # Increment the counter
            counter += 1

    def first_forward(self):
        self.page.find_evaluations_forward_button()
        self.click_element(self.page.evaluations_forward_button)
        self.driver.execute_script("window.scrollTo(0, 550);")

    def other_forwards(self):
        self.page.find_other_forward_buttons()
        self.click_element(self.page.other_forward_buttons)
        self.driver.execute_script("window.scrollTo(0, 550);")

    def navigating_analyze_report(self):
        self.navigating_to_evaluations_page()
        self.page.find_start_button_for_evaluations()
        self.click_element(self.page.start_evaluations_button)

    def initial_exam(self):
        self.navigating_to_evaluations_page()
        self.driver.execute_script("window.scrollTo(0, 400);")
        self.hide_widget_div()
        self.page.find_front_end_exam_start_button()
        self.click_element(self.page.front_end_exam_start_button)
        self.page.find_start_exam_button()
        self.click_element(self.page.start_to_exam_button)
        self.driver.execute_script("window.scrollTo(0, 300);")

    def completing_exam(self):
        for _ in range(25):
            self.page.find_exam_options()
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.click_element(self.page.exam_first_option)
            self.page.find_exam_next_button()
            self.click_element(self.page.exam_next_button)

    def test_navigating_to_evaluations_page(self):
        self.navigating_to_evaluations_page()
        self.get_new_url()
        assert self.new_url == const.url_10_evaluation, "Driver failed to reach evaluations page"
        print("Driver navigated to Evaluations Page successfully")
        Driver.screenshot(self.driver, "../screenshots/screenshots_10_evaluation", "test_1_navigating_evaluationPage.png")

    def test_completing_evaluations_module(self):
        self.navigating_to_evaluations_modul()
        self.hide_widget_div()
        # before click first page
        Driver.screenshot(self.driver, "../screenshots/screenshots_10_evaluation", "test_2_1_evaluation_modul.png")
        self.click_on_radio_buttons()
        Driver.screenshot(self.driver, "../screenshots/screenshots_10_evaluation", "test_2_2_evaluation_modul.png")
        self.first_forward()  # 20
        self.click_on_radio_buttons()
        Driver.screenshot(self.driver, "../screenshots/screenshots_10_evaluation", "test_2_3_evaluation_modul.png")
        self.other_forwards()  # 30
        self.click_on_radio_buttons()
        Driver.screenshot(self.driver, "../screenshots/screenshots_10_evaluation", "test_2_4_evaluation_modul.png")
        self.other_forwards()  # 40
        self.click_on_radio_buttons()
        Driver.screenshot(self.driver, "../screenshots/screenshots_10_evaluation", "test_2_5_evaluation_modul.png")
        self.other_forwards()  # 50
        self.click_on_radio_buttons()
        Driver.screenshot(self.driver, "../screenshots/screenshots_10_evaluation", "test_2_6_evaluation_modul.png")
        self.other_forwards()  # 60
        self.click_on_radio_buttons()
        Driver.screenshot(self.driver, "../screenshots/screenshots_10_evaluation", "test_2_7_evaluation_modul.png")
        self.other_forwards()  # 70
        self.click_on_radio_buttons()
        Driver.screenshot(self.driver, "../screenshots/screenshots_10_evaluation", "test_2_8_evaluation_modul.png")
        self.other_forwards()  # 20
        self.click_on_radio_buttons()
        Driver.screenshot(self.driver, "../screenshots/screenshots_10_evaluation", "test_2_9_evaluation_modul.png")

    def test_display_evaluations_analyze_report(self):
        self.navigating_analyze_report()
        self.get_new_url()
        assert self.new_url == const.url_10_evaluation_report, "Navigating to analyze report failed"
        print("Analyze Report displayed successfully")
        Driver.screenshot(self.driver, "../screenshots/screenshots_10_evaluation", "test_3_evaluation_analyze_report.png")

    def test_complete_exam(self):
        self.initial_exam()
        self.completing_exam()

    def test_display_exam_results(self):
        self.initial_exam()  # same path to follow
        self.page.find_exam_done_text()
        assert self.page.exam_done_text == const.text_10_exam_done, "Displaying Test Results Failed"
        print("Test Results Displaying Successfully")
        Driver.screenshot(self.driver, "../screenshots/screenshots_10_evaluation", "test_5_evaluation_analyze_report.png")



