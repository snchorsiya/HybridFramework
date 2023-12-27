import pytest
from selenium import webdriver


# pytest -v -s -n=2 --browser firefox testCases/test_login_testcase.py >> Specific browser
# - n=2 is parallel testing
# pytest -v -s -n=2 --browser chrome --html=Reports/report.html testCases/test_login_testcase.py >> generate html report
# pytest -v -s -m "sanity or smoke" --browser chrome --html=Reports/report.html testCases/test_login_testcase.py

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Edge()

    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.hookimpl(optionalhook=True)
def pytest_metadat(metadata):
    metadata.pop("Platform", None)
    metadata.pop("Packages", None)
    metadata.pop("Plugins", None)


# @pytest.hookimpl(tryfirst=True)
# def pytest_sessionfinish(session, exitstatus):
#     session.config._metadata["Project Name"] = "Mercury Tours"


def pytest_html_report_title(report):
    '''modifying the title of html report'''
    report.title = "Custom title"
