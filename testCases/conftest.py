import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("launching chrome browser")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("launching edge browser")
    else:
        driver = webdriver.Chrome()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

#### ------ PTTEST HTML REPORT ----- #######
def pytest_configure(config):
    config._metadata['Project Name'] = 'E Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester Name'] = 'Shankar'
#@pytest.mark.optionalhook
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)



# @pytest.fixture()
# def setup():
#     driver=webdriver.Chrome()
#     return driver

# for step 07 use below
