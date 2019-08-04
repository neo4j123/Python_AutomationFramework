import pytest
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils
import allure
import moment


@pytest.mark.usefixtures("test_setup")
class TestLogin:

    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)
        login = LoginPage(driver)
        login.do_login(utils.USERNAME, utils.PASSWORD)

    def test_logout(self):
        try:
            driver = self.driver
            homepage = HomePage(driver)
            homepage.do_logout()
            x = driver.title
            assert x == 'abc'

        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            currentTimeStamp = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName = utils.whoami()
            screenshotName = testName+"_"+currentTimeStamp
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                      attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("/home/akash/PycharmProjects/AutomationFramework/screenshots/"+screenshotName+".png")
            raise

        except:
            print("There was an exception")
            raise

        else:
            print("No Exception raised")