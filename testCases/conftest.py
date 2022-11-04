import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def setup():

    object = Service(r"C:\Users\Cliffex-Lead\Desktop\chrome\chromedriver.exe")
    driver= webdriver.Chrome(service=object)
    return driver











