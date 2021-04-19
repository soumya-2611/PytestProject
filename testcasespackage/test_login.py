
import pytest
from selenium import webdriver
from pageobjectpackage.loginpage import Login
from utilitiespackage.readproperties import Readconfig
from utilitiespackage.customlogger import Loggen

class Test_001_Login:
    baseurl = Readconfig.geturl()
    username =Readconfig.getusername()
    password = Readconfig.getpassword()
    loggers=Loggen.loggen()

    @pytest.mark.regression
    def test_homepagetitle(self,setup):
        self.loggers.info("******************* Verifying  Test_001_Login  ***********************")
        self.loggers.info("******************* Verifying  test_homepagetitle  ***********************")
        self.driver=setup
        self.driver.get(self.baseurl)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.loggers.info("******************* test_homepagetitle passed  ***********************")
        else:
            self.driver.save_screenshot("C:\\Users\\Soumya.Mohanty\\Desktop\\python39\\PytestProject\\screenshotsfolder"+"test_homepagetitle.png")
            self.driver.close()
            self.loggers.info("******************* test_homepagetitle failed  ***********************")
            assert False
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.loggers.info("******************* Verifying  test_login  ***********************")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.lp=Login(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.loggers.info("******************* test_login passed  ***********************")
        else:
            self.driver.save_screenshot("C:\\Users\\Soumya.Mohanty\\Desktop\\python39\\PytestProject\\screenshotsfolder"+"test_login.png")
            self.driver.close()
            self.loggers.info("******************* test_login failed  ***********************")
            assert False
