import pytest
import allure

from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = None


@pytest.fixture
def setup():
    print("Start the browser")
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    yield
    print("Close the browser")
    driver.close()

@allure.severity(allure.severity_level.BLOCKER)
def test_01_login(setup):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    actual_title = driver.title
    if actual_title == "Swag Labs":
        assert True
    else:
        allure.attach(driver.get_screenshot_as_png(), name="test_01_login", attachment_type=AttachmentType.PNG)
        assert False
    print("Test 1 executed")

@allure.severity(allure.severity_level.NORMAL)
def test_02_login_logout(setup):
    test_01_login(setup)
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.ID, "logout_sidebar_link")))
    driver.find_element(By.ID, "logout_sidebar_link").click()
    actual_title = driver.title
    if actual_title == "Swag Labs":
        assert True
    else:
        allure.attach(driver.get_screenshot_as_png(), name="test_02_login_logout", attachment_type=AttachmentType.PNG)
        assert False
    print("Test 2 executed")


def test_03_empty_credential(setup):
    driver.find_element(By.ID, "user-name").send_keys("")
    driver.find_element(By.ID, "password").send_keys("")
    driver.find_element(By.ID, "login-button").click()
    error_message = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
    print(error_message.text)
    print("Test 3 executed")

# "C:/Users/JahidulIslam/PycharmProjects/pytestDemo/reports/"
