import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        object = Service(r"C:\Users\Cliffex-Lead\Desktop\chrome\chromedriver.exe")
        driver = webdriver.Chrome(service=object)
        print("lunchin chrome....")
    elif browser == "firefox":
        object = Service(r"C:\Users\Cliffex-Lead\Desktop\chrome\geckodriver.exe")
        driver = webdriver.Firefox(service=object)
        print("lunchin firefox....")
    else:
        object = Service(r"C:\Users\Cliffex-Lead\Desktop\chrome\chromedriver.exe")
        driver = webdriver.Chrome(service=object)
        print("launching chrome....")

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


def pytest_configure(config):
    config._metadata['Project Name'] = 'Hybrid Framework Practice'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Piyush'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA HOME", None)
    metadata.pop("Plugins", None)





















# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
#
#
# @pytest.fixture
# def setup():
#
#     object = Service(r"C:\Users\Cliffex-Lead\Desktop\chrome\chromedriver.exe")
#     driver = webdriver.Chrome(service=object)
#     return driver
#
#
#
#
