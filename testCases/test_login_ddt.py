import time

from selenium import webdriver
from pageObjects.LoginPage import Login
import pytest
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen
from utilities import XLUtils

class Test_002_DDT_Login:
    url = ReadConfig.getApplicationURl()
    path = ".//testData/testdata123.xlsx"

    logger = logGen.loggen()


    def test_login_ddt(self,setup):
        self.logger.info("***************** test_login is started ******************")
        self.driver = setup
        self.driver.get(self.url)
        self.lp = Login(self.driver)
        self.rows =XLUtils.getRowCount(self.path,"Sheet1")
        print("Nu,bers od rows in a exel",self.rows)

        st_list = []
        for r in range(2,self.rows+1):
            self.user= XLUtils.readData(self.path,'Sheet1',r,1)
            self.password = XLUtils.readData(self.path,"Sheet1",r,2)
            self.result = XLUtils.readData(self.path, "Sheet1", r, 3)
            self.lp.setusername(self.user)
            self.lp.setpassword(self.password)
            self.lp.click_login()
            time.sleep(4)

            act_tilte= self.driver.title
            exp_tilte = "Dashboard / nopCommerce administration"

            if act_tilte==exp_tilte:
                if self.result== "pass":
                    self.lp.click_logout()
                    st_list.append("pass")
                elif self.result == "fail":
                    self.lp.click_logout()
                    st_list.append("fail")

            elif act_tilte!=exp_tilte:
                if self.result== "pass":
                    self.lp.click_logout()
                    st_list.append("fail")
                elif self.result == "fail":
                    self.lp.click_logout()
                    st_list.append("pass")

        if "fail" not in st_list:
            print("pass the ddtt test ")
            self.driver.close()
            assert True

        else:
            print("fail")
            self.driver.close()
            assert False









































































































# import pytest
# from selenium import webdriver
# from pageObjects.LoginPage import Login
#
#
# class Test_001_login:
#     url = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
#     username="admin@yourstore.com"
#     password="admin"
#
#     def test_homepage_title(self,setup):
#         self.driver = setup
#         self.driver.get(self.url)
#         act_title= self.driver.title
#
#         if act_title =="Your store. Login":
#             self.driver.close()
#             assert True
#
#         else:
#             self.driver.save_screenshot(".\\Screenshots\\"+"test_homepage_title.png")
#             self.driver.close()
#             assert False
#
#
#     def test_login(self,setup):
#         self.driver = setup
#         self.driver.get(self.url)
#         self.lp = Login(self.driver)
#         self.lp.setusername(self.username)
#         self.lp.setpassword(self.password)
#         self.lp.clicklogin()
#         act_title =self.driver.title
#         if act_title ==  "Dashboard / nopCommerce administration":
#             self.driver.close()
#             assert True
#
#         else:
#             self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
#             self.driver.close()
#             assert False
#
#
#
#
#
#
