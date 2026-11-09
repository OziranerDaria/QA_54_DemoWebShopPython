
import pytest
from selenium import webdriver
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    driver.get("https://demowebshop.tricentis.com/")

    yield driver

    driver.quit()





