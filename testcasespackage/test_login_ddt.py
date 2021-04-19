
import pytest
from selenium import webdriver
from pageobjectpackage.loginpage import Login
from utilitiespackage.readproperties import Readconfig
from utilitiespackage.customlogger import Loggen
from utilitiespackage import XLUtils
import time
class Test_002_DDT_Login:
    baseurl = Readconfig.geturl()
    path="C:\\Users\\Soumya.Mohanty\\Desktop\\python39\\PytestProject\\testdatafolder\\LoginData.xlsx"
    loggers=Loggen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.loggers.info("******************* Test_002_DDT_Login  ***********************")
        self.loggers.info("******************* Verifying  test_login_ddt  ***********************")
        self.driver=setup
        #self.driver.get(self.baseurl)
        self.lp=Login(self.driver)

        self.rows=XLUtils.rowcount(self.path,'Sheet1')
        print("No of rows in excel:", self.rows)
        list_status=[]
        for r in range(2,self.rows+1):
            self.user = XLUtils.readdata(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readdata(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readdata(self.path, 'Sheet1', r, 3)
            self.driver.get(self.baseurl)
            time.sleep(5)
            self.lp.setusername(self.user)
            self.lp.setpassword(self.password)
            self.lp.clicklogin()
            time.sleep(5)
            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=="pass":
                    self.loggers.info("Passed")
                    self.lp.logout()
                    list_status.append("pass")
                elif self.exp=="fail":
                    self.loggers.info("Failed")
                    self.lp.logout()
                    list_status.append("fail")
            elif act_title != exp_title:
                if self.exp == 'pass':
                    self.loggers.info("Failed")
                    list_status.append("fail")
                elif self.exp == 'fail':
                    self.loggers.info("Passed")
                    list_status.append("pass")

        if "fail" not in list_status:
            self.loggers.info("Test_002_DDT_Login Passed")
            self.driver.close()
            assert True
        else:
            self.loggers.info("Test_002_DDT_Login Failed")
            self.driver.close()
            assert False

        self.loggers.info("*****************End of Test_002_DDT_Login ***************")


































