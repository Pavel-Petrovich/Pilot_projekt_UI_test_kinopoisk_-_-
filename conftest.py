import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from urls import MAIN_URL
from pages.main_page import MainPage
#from pages.product_page import ProductPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.set_window_size(1920,1080)
    driver.get(MAIN_URL)
    yield driver
    driver.quit()

@pytest.fixture()
def main_page(driver):
    driver.get(MAIN_URL)
    return MainPage(driver)
