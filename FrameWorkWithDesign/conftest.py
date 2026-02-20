from datetime import datetime
import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
driver = None
def pytest_addoption(parser):
    parser.addoption(
           "--browser_name", action="store" , default="chrome", help="browser selection"
    )

@pytest.fixture(scope="function")
def browserInstance(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    service_obj = Service()
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=service_obj)
        driver.implicitly_wait(5)
    elif browser_name == "edge":
            driver = webdriver.Edge(service=service_obj)
            driver.implicitly_wait(5)
    yield driver
    # driver.close()   #post your test execution

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    # Execute all other hooks to obtain report object
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    # We only take screenshot for actual test call (not setup/teardown)
    if report.when == "call" and report.failed:
        print("in screenshot")
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # report_dir = os.path.join(os.path.dirname(__file__), 'Reports')
            # file_name = os.path.join(report_dir, report.nodeid.replace("::", "_")+".png")
            # print("filename is : ", file_name)

            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            test_name = item.name
            file_name = f"failure1_{timestamp}.png"
            file_path = os.path.join(screenshots_dir, file_name)
            save_screenshot(file_path)
            print(file_path)
            print(file_name)
            if file_name:
                html = f'<div><img src="{file_path}" style="width:304px;height:228px;"' 'onclick="window.open(this.src)" align="right"/></div>'
                extra.append(pytest_html.extras.html(html))

        report.extra =extra



            # print(f"\nScreenshot saved at: {file_path}")

def save_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)