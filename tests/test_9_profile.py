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
        assert self.new_url != const.url_9_my_profile
        print("Media link is working")

