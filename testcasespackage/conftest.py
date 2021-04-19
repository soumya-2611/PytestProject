from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='firefox':#pytest -vs test_login.py --browse firefox
        driver=webdriver.Firefox()
        print("launching Ie")

    elif browser=='ie':#pytest -vs test_login.py --browse ie
        driver=webdriver.Ie()
        print("launching Ie")
    else:
        #driver = webdriver.Chrome()#directly run this default browser using pytest -vs test_login.py
        chromeoption = webdriver.ChromeOptions()
        chromeoption.add_argument("--disable-notifications")
        driver = webdriver.Chrome(options=chromeoption)

    return driver


def pytest_addoption(parser):#this will get the value from comandlineinterface
    parser.addoption("--browse")

@pytest.fixture()#this will pass the browser value to setup
def browser(request):
    return request.config.getoption("--browse")

#adding evnt and  project details to html report

def pytest_configure(config):
    config._metadata['Project Name']="nop commerce"
    config._metadata['Modulename'] = "Customers"
    config._metadata['Tester']="Soumya"
#to delete/modify envt details from html report
# @pytest.mark.optionalhook
# def pytest_metadata(metdata):
#     metdata.pop("JAVA_HOME",None)
#     metdata.pop("Plugins",None)





