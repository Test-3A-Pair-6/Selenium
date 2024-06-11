from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from utils import ConfigReader


def wait(driver, selector, element, flag="visit", timeout=20):
    if flag == "visit":
        return WebDriverWait(driver, timeout).until(ec.visibility_of_element_located((selector, element)))
    if flag == "click":
        return WebDriverWait(driver, timeout).until(ec.element_to_be_clickable((selector, element)))


def get_driver():
    driver = None
    option = None
    flag = ConfigReader.read_config("headless")

    if flag == "1":
        option = Options()
        option.add_argument("--headless")
    browser = ConfigReader.read_config("browser")
    try:
        match browser:
            case "chrome":
                driver = webdriver.Chrome(options=option)
            case "firefox":
                driver = webdriver.Firefox(options=option)
            case "edge":
                driver = webdriver.Edge(options=option)
            case "safari":
                driver = webdriver.Safari(options=option)
            case _:
                raise Exception("Invalid browser")
    except Exception as e:
        print(e)
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver
