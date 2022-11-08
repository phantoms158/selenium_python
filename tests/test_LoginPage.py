import time
from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest

from pageObjects.facebook import FacebookPage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self):
        facebookPage= FacebookPage(self.driver)
        facebookPage.getEmail().send_keys("trongpq@gmail.com")
        facebookPage.getPassword().send_keys("123456789")
        time.sleep(2)
        facebookPage.screenshot()
        time.sleep(10)
        # facebookPage.submitForm().click()


        # assert ("Success" in alertText)
        # self.driver.refresh()

    # @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    # def getData(self, request):
    #     return request.param

