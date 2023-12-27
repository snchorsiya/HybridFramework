import datetime
import time

import pytest

from pageObjects.LoginPage import Login
from Utilits.readConfigData import ReadConfig
from Utilits import customLogger
from Utilits import utility

date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


class TestLogin:
    base_url = ReadConfig.getCommonData('commonData', 'base_url')
    username = ReadConfig.getCommonData('commonData', 'username')
    password = ReadConfig.getCommonData('commonData', 'password')
    loggor = customLogger.get_logger("LoginPage")
    file = ".\\TestData\\LoginMaster.xlsx"
    # file = 'D:\Automation\PythonAutomation\PyTestframework\HybridFramework\TestData\LoginMaster.xlsx'

    @pytest.mark.sanity
    @pytest.mark.smoke
    def test_home_page_validation(self, setup):
        self.loggor.info("===== TC01 Verify home page title =====")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        title = self.driver.title
        self.loggor.info("===== getting title =" + title)
        if title == ReadConfig.getCommonData('message', 'home_title'):
            self.driver.save_screenshot(f".//ScreenShots//home_title_{date}.png")
            self.loggor.info("===== Successfully home page title =====")
            assert True
        else:
            self.loggor.info("===== failed home page title =====")
            self.driver.save_screenshot(f".//ScreenShots//home_title_{date}.png")
            assert False
        self.driver.close()

    @pytest.mark.smoke
    def test_login_page_validation(self, setup):
        self.loggor.info("===== TC02 Verify login page title =====")
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = Login(self.driver)
        self.loggor.info("===== providing username =====")
        self.lp.setUsername(self.username)
        self.loggor.info("===== providing password =====")
        self.lp.setPassword(self.password)
        self.lp.submitLoginBtn()
        title = self.driver.title
        self.loggor.info("===== getting login title =" + title)
        if title == ReadConfig.getCommonData('message', 'login_title'):
            self.driver.save_screenshot(f".//ScreenShots//login_title_{date}.png")
            self.loggor.info("===== Successfully login page title =====")
            assert True
        else:
            self.loggor.info("===== failed login page title =====")
            self.driver.save_screenshot(f".//ScreenShots//login_title_{date}.png")
            assert False
        self.driver.close()

    @pytest.mark.regression
    def test_excel_login_page_validation(self, setup):
        row_count = utility.get_row_count(self.file, "Sheet1")
        list_status = []
        for r in range(2, row_count+1):
            username = utility.read_data(self.file, "Sheet1", r, 1)
            password = utility.read_data(self.file, "Sheet1", r, 2)
            result = utility.read_data(self.file, "Sheet1", r, 3)
            self.loggor.info("===== TC03 Verify login page title =====")
            self.driver = setup
            self.driver.get(self.base_url)
            self.lp = Login(self.driver)
            self.loggor.info("===== providing username =====")
            self.lp.setUsername(username)
            self.loggor.info("===== providing password =====")
            self.lp.setPassword(password)
            self.lp.submitLoginBtn()
            title = self.driver.title
            self.loggor.info("===== getting login title =" + title)
            if title == ReadConfig.getCommonData('message', 'login_title'):
                if result == "Pass":
                    utility.fill_green(self.file, "Sheet1", r, 3)
                    self.loggor.info("===== Successfully login page title =====")
                    self.driver.save_screenshot(f".//ScreenShots//login_title_{date}.png")
                    list_status.append("Pass")
                elif result == "Fail":
                    utility.fill_red(self.file, "Sheet1", r, 3)
                    self.loggor.info("===== failed login title =====")
                    self.driver.save_screenshot(f".//ScreenShots//failed_login_title_{date}.png")
                    list_status.append("Fail")
            elif title != ReadConfig.getCommonData('message', 'login_title'):
                if result == "Pass":
                    utility.fill_green(self.file, "Sheet1", r, 3)
                    self.loggor.info("===== Successfully login page title =====")
                    self.driver.save_screenshot(f".//ScreenShots//login_title_{date}.png")
                    list_status.append("Fail")
                elif result == "Fail":
                    utility.fill_red(self.file, "Sheet1", r, 3)
                    self.loggor.info("===== failed login title =====")
                    self.driver.save_screenshot(f".//ScreenShots//failed_login_title_{date}.png")
                    list_status.append("Pass")

                if "Fail" not in list_status:
                    self.loggor.info("Login is success")
                    assert True
                else:
                    self.loggor.info("Login is failed")
                    assert False
                # self.loggor.info("===== failed login page title =====")
                # self.driver.save_screenshot(f".//ScreenShots//login_title_{date}.png")

