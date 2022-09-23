import pytest

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
    driver.maximize_window()
    yield
    print("Close the browser")
    driver.close()

@pytest.mark.parametrize("username, password",
                         [
                             ("standard_user", "secret_sauce"),
                             ("", ""),
                             ("standard_user", ""),
                             ("", "secret_sauce"),
                             ("locked_out_user", "secret_sauce"),
                             ("problem_user", "secret_sauce"),
                             ("performance_glitch_user", "secret_sauce"),
                         ])
def test_01_login(setup, username, password):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='login_button_container']/div/form/div[3]")))
    message = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]")
    print("ERROR: " + message.text)
    driver.get("https://www.saucedemo.com/")
