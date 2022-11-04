import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login


class Test_001_login:
    url = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username="admin@yourstore.com"
    password="admin"

    def test_homepage_title(self,setup):
        self.driver= setup
        self.driver.get(self.url)
        act_title= self.driver.title

        if act_title =="Your store. Login":
            self.driver.close()
            assert True

        else:
            self.driver.close()
            assert False


    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        self.lp=Login(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        act_title =self.driver.title
        if act_title ==  "Dashboard / nopCommerce administration":
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False






