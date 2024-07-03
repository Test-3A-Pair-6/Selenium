import os
from time import sleep
import pytest
import pyperclip
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages import page_9_profile
from utils import Driver
from utils import Constants as const
from utils import ConfigReader as cr
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.action_chains import ActionChains


class TestProfile:
    shared_profile_url = None
    file_path = os.path.join(const.path_9_download,
                             const.pdf_file_9_downloaded)  # "file_path = os.path.join(download_path, file_name)"
    def setup_method(self):
        self.driver = Driver.get_driver()
        self.driver.get(cr.read_config("url_main"))
        self.page = page_9_profile.ProfilePage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def login(self):
        self.page.login_info()
        #self.page.user_name.send_keys(const.user_mail_ismet)
        #self.page.password.send_keys(const.user_password_ismet)
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

    def navigating_to_my_profile_page(self):
        self.login()
        self.page.find_profile_button_on_top_menu()
        self.driver.execute_script("arguments[0].click();", self.page.my_profile_button_on_top_menu)
        sleep(1)

    def navigating_to_share_dropdown(self):
        self.navigating_to_my_profile_page()
        self.page.find_share_dropdown()
        self.driver.execute_script("arguments[0].click();", self.page.share_dropdown_button)
        sleep(2)

    def click_share_switch_button(self):
        self.page.find_switch_button()
        self.driver.execute_script("window.scrollTo(0, 150);")
        self.page.switch_button.click()
        sleep(2)

    def deactivate_switch_button_as_default(self):
        self.page.find_switch_checkbox_attribute_value()
        if self.page.switch_checkbox_aria_checked == const.true_value_9_aria_checked:
            self.click_share_switch_button()
            print("Switch button deactivated")
        else:
            print("Switch button is already deactivated")

    def url_copy_icon(self):
        self.navigating_to_share_dropdown()
        self.page.find_copy_icon()
        self.click_element(self.page.copy_icon)
        self.shared_profile_url = pyperclip.paste()

    def navigating_to_shared_link_page(self):
        self.driver.get(self.shared_profile_url)

    def download_certificate(self):
        self.navigating_to_my_profile_page()
        self.driver.execute_script("window.scrollTo(0, 1650);")
        sleep(4)
        self.page.find_clickable_certification()
        sleep(2)
        self.click_element(self.page.certification_clickable)
        sleep(3)

    def checking_download_function(self):
        if os.path.isfile(self.file_path):
            const.pdf_file_9_download_status = True
            print("PDF founded successfully")
        else:
            const.pdf_file_9_download_status = False
            print("PDF found operation failed")
        return const.pdf_file_9_download_status

    def click_media_icon(self):
        self.navigating_to_my_profile_page()
        self.page.find_linkedin_icon()
        self.click_element(self.page.linkedin_icon)
        sleep(3)

    def get_new_url(self):
        self.new_url = self.driver.current_url
        print(self.new_url)

    def navigating_to_evaluation_page(self):
        self.login()
        self.page.find_evaluation_button()
        self.click_element(self.page.evaluation_button_on_top_menu)

    def navigating_to_evaluation_modul(self):
        self.navigating_to_evaluation_page()
        self.page.find_start_button_for_evaluation()
        sleep(1)
        self.click_element(self.page.start_evaluation_button)
        self.driver.execute_script("window.scrollTo(0, 650);")
        sleep(1)
        self.page.find_confirm_start_button()
        self.click_element(self.page.confirm_start_button)

    def hide_widget_div(self):
        self.page.find_widget()
        self.driver.execute_script("arguments[0].style.display = 'none';", self.page.iframe_widget_div)
        sleep(2)

    def click_on_radio_buttons(self):
        self.page.find_radio_buttons()
        sleep(3)
        actions = ActionChains(self.driver)

        # Iterate through each radio button and click it
        for radio_button in self.page.radio_buttons:
            # Ensure the element is clickable before clicking
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(radio_button))

            # Scroll to the radio button
            actions.move_to_element(radio_button).perform()

            # Click the radio button
            radio_button.click()
            counter = 1
            name_attribute = radio_button.get_attribute('name')
            print(f"Click {counter}: Name attribute of the button is '{name_attribute}'")

            # Increment the counter
            counter += 1
        sleep(3)

    def first_forward(self):
        self.page.find_evaluation_forward_button()
        self.click_element(self.page.evaluation_forward_button)
        self.driver.execute_script("window.scrollTo(0, 550);")
        sleep(1)

    def other_forwards(self):
        self.page.find_other_forward_buttons()
        self.click_element(self.page.other_forward_buttons)
        self.driver.execute_script("window.scrollTo(0, 550);")
        sleep(1)

    def navigating_analyze_report(self):
        self.navigating_to_evaluation_page()
        self.page.find_start_button_for_evaluation()
        self.click_element(self.page.start_evaluation_button)
        sleep(2)

    @pytest.mark.navigating_1
    def test_navigating_to_my_profile(self):
        self.navigating_to_my_profile_page()
        self.page.find_professional_job_experience_text()
        assert self.page.title_professional_experience == const.title_9_professional_xp, "Driver is not on the my profile page"
        Driver.screenshot(self.driver, "../screenshots/screenshots_9_profile", "test_1_navigating_profile.png")
        print("Navigated to my profile page")

    @pytest.mark.navigating_2
    def test_navigating_to_share_dropdown(self):
        self.navigating_to_share_dropdown()
        self.page.find_share_button_title()
        assert self.page.title_share_profile_link == const.title_9_profile_share_link, "Driver couldn't reach the share dropdown"
        Driver.screenshot(self.driver, "../screenshots/screenshots_9_profile", "test_2_navigating_share_dropdown.png")
        print("Clicked to share profile dropdown button")

    @pytest.mark.switch_1
    def test_share_switch_button_function(self):
        self.navigating_to_share_dropdown()
        self.deactivate_switch_button_as_default()  # checks and turns off button
        self.click_share_switch_button()
        self.page.find_switch_checkbox_attribute_value()
        assert self.page.switch_checkbox_aria_checked == const.true_value_9_aria_checked, "Switch button is already activated"
        Driver.screenshot(self.driver, "../screenshots/screenshots_9_profile", "test_3_1_switch_to_activate.png")
        print("Switch activation is successful")
        self.click_share_switch_button()
        self.page.find_switch_checkbox_attribute_value()
        assert self.page.switch_checkbox_aria_checked == const.false_value_9_aria_checked, "Switch button is already deactivated"
        Driver.screenshot(self.driver, "../screenshots/screenshots_9_profile", "test_3_2_switch_to_deactivate.png")
        print("Switch deactivation is successful")

    @pytest.mark.navigating_3
    def test_shared_profile(self):
        self.url_copy_icon()
        self.navigating_to_shared_link_page()
        self.page.find_header_on_share_link()
        assert self.page.header_on_share_link == const.header_9_on_profile_link, "Headers doesn't match"
        Driver.screenshot(self.driver, "../screenshots/screenshots_9_profile", "test_4_navigate_to_shared_profile.png")

    def test_download_certification(self): # FIRST REMOVE THE SAME PREVIOUS DOWNLOADED FROM PATH DIR
        self.download_certificate()
        self.checking_download_function()
        assert const.pdf_file_9_download_status == True, "PDF download failed"
        sleep(10)

    def test_navigating_social_media_via_icon(self):
        self.click_media_icon()
        self.get_new_url()
        Driver.screenshot(self.driver, "../screenshots/screenshots_9_profile", "test_6_navigating_social_media.png")
        assert self.new_url != const.url_my_profile
        print("Media link is working")

    def test_navigating_to_evaluation_page(self):
        self.navigating_to_evaluation_page()
        self.get_new_url()
        assert self.new_url == const.url_evaluation, "Driver failed to reach evaluations page"
        print("Driver navigated to Evaluations Page successfully")
        Driver.screenshot(self.driver, "../screenshots/screenshots_9_profile", "test_7_navigating_evaluationPage.png")

    def test_completing_evaluation_module(self):
        self.navigating_to_evaluation_modul()
        sleep(2)
        self.hide_widget_div()
        # before click first page
        Driver.screenshot(self.driver, "../screenshots/screenshots_9_profile", "test_8_1_evaluation_modul.png")
        self.click_on_radio_buttons()
        sleep(1)
        Driver.screenshot(self.driver, "../screenshots/screenshots_9_profile", "test_8_2_evaluation_modul.png")
        self.first_forward()  # 20
        self.click_on_radio_buttons()
        sleep(1)
        Driver.screenshot(self.driver, "../screenshots/screenshots_9_profile", "test_8_3_evaluation_modul.png")
        self.other_forwards()  # 30
        self.click_on_radio_buttons()
        sleep(1)
        Driver.screenshot(self.driver, "../screenshots/screenshots_9_profile", "test_8_4_evaluation_modul.png")
        self.other_forwards()  # 40
        self.click_on_radio_buttons()
        sleep(1)
        Driver.screenshot(self.driver, "../screenshots/screenshots_9_profile", "test_8_5_evaluation_modul.png")
        self.other_forwards()  # 50
        self.click_on_radio_buttons()
        sleep(1)
        Driver.screenshot(self.driver, "../screenshots/screenshots_9_profile", "test_8_6_evaluation_modul.png")
        self.other_forwards()  # 60
        self.click_on_radio_buttons()
        sleep(1)
        Driver.screenshot(self.driver, "../screenshots/screenshots_9_profile", "test_8_7_evaluation_modul.png")
        self.other_forwards()  # 70
        self.click_on_radio_buttons()
        sleep(1)
        Driver.screenshot(self.driver, "../screenshots/screenshots_9_profile", "test_8_8_evaluation_modul.png")
        self.other_forwards()  # 80
        sleep(1)
        self.click_on_radio_buttons()
        sleep(1)
        Driver.screenshot(self.driver, "../screenshots/screenshots_9_profile", "test_8_10_evaluation_modul.png")
        sleep(20)

    def test_display_evaluation_analyze_report(self):
        self.navigating_analyze_report()
        self.get_new_url()
        assert self.new_url == const.ur_evaluation_report, "Navigating to analyze report failed"
        print("Analyze Report displayed successfully")
        Driver.screenshot(self.driver, "../screenshots/screenshots_9_profile", "test_9_evaluation_analyze_report.png")
