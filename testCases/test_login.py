from selenium import webdriver
from pageObjects.LoginPage import Login
import pytest
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen

class Test_001:
    url = ReadConfig.getApplicationURl()
    # url2 = ReadConfig.getUrl2()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()

    logger = logGen.loggen()

    def test_homepage_title(self,setup):
        self.logger.info("***************** Test_001 ******************")
        self.logger.info("***************** verify home page ******************")
        self.driver = setup
        self.driver.get(self.url)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            self.logger.info("***************** title is pass ******************")
            self.driver.close()
            assert True

        else:
            self.logger.error("***************** title is failed******************")
            self.driver.close()
            assert False



    def test_login(self,setup):
        self.logger.info("***************** test_login is started ******************")
        self.driver = setup
        self.driver.get(self.url)
        self.lp = Login(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.click_login()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            self.driver.save_screenshot(".\\Screenshots\\"+"login2.png")
            self.logger.info("***************** title is pass ******************")
            self.driver.close()
            assert True


        else:
            self.logger.error("***************** title is failed ******************")
            self.driver.close()
            assert False


    # def test_perpose(self,setup):
    #     self.driver = setup
    #     self.driver.get("https://" +username_in_url+":"+password_in_url+"@"+self.url2)
    #     indiefolio = self.driver.title
    #
    #     if indiefolio == "Indieflio || Hire The Best Freelancers For Your Creative Needs":
    #         print("pass")
    #         assert True
    #     else:
    #         print("fail")
    #         assert False








































































































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
