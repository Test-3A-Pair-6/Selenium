from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import Driver, ConfigReader as cr, Constants as const
from pages import page_13_personal_informaiton
class TestPersonalInformation:

    def setup_method(self):
        self.driver = Driver.get_driver()
        self.driver.get(cr.read_config("url_main"))
        self.page = page_13_personal_informaiton.PagePersonalInformation(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def login(self):
        self.page.login_info()
        self.page.user_name.send_keys(const.valid_user_name)
        self.page.password.send_keys(const.valid_password)
        self.page.submit_button()
        self.driver.execute_script("arguments[0].click();", self.page.login_button)

    def hide_widget_div(self):
        self.page.find_widget()
        self.driver.execute_script("arguments[0].style.display = 'none';", self.page.iframe_widget_div)


    def test_profile_title_control(self):
        self.login()
        WebDriverWait(self.driver, 20).until(EC.url_changes(const.loginURL))
        self.hide_widget_div()
        self.driver.execute_script("window.scrollTo(0, 650);")
        self.page.profile_title_control()


    def test_personal_information(self):
        self.login()
        WebDriverWait(self.driver, 20).until(EC.url_changes(const.loginURL))
        self.driver.execute_script("window.scrollTo(0, 650);")
        self.page.profile_title_control()
        self.page.update_personal_information()

    def test_add_profile_picture(self):
        self.login()
        WebDriverWait(self.driver, 20).until(EC.url_changes(const.loginURL))
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.page.profile_title_control()
        self.page.add_profile_picture()


    def test_id_control(self):
        self.login()
        WebDriverWait(self.driver, 20).until(EC.url_changes(const.loginURL))
        self.hide_widget_div()
        self.driver.implicitly_wait(10)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.page.profile_title_control()
        self.page.id_control()

    def test_check(self):
        self.login()
        self.hide_widget_div()
        self.driver.execute_script("window.scrollTo(0, 650);")
        self.page.profile_title_control()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.submit = Driver.wait(self.driver, By.XPATH, "//button[@class='btn btn-primary py-2 mb-3 d-inline-block mobil-btn']", "click", 5)
        print(self.submit.text)

    def test_character_control(self):
        self.login()
        self.hide_widget_div()
        self.driver.execute_script("window.scrollTo(0, 650);")
        self.page.profile_title_control()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.page.character_control()
        self.page.button()





