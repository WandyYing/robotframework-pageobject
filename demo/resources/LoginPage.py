import os
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from .fetchyaml import FetchYaml


class LoginPage(PageObject):
    PAGE_TITLE = "Login - PageObjectLibrary Demo"
    PAGE_URL = "/login.html"

    # these are accessible via dot notaton with self.locator
    # (eg: self.locator.username, etc)
    # _locators = {
    #     "username": "id=id_username",
    #     "password": "id=id_password",
    #     "submit_button": "id=id_submit",
    #
    # _here = os.path.dirname(__file__)
    # print(_here)
    _locators=FetchYaml().load_yaml(os.path.dirname(__file__) + "/LoginPage.yml")["LoginPage"]

    def login_as_a_normal_user(self):
        config = BuiltIn().get_variable_value("${CONFIG}")
        self.enter_username(config.username)
        self.enter_password(config.password)
        with self._wait_for_page_refresh():
            self.click_the_submit_button()

    def enter_username(self, username):
        """Enter the given string into the username field"""
        self.selib.input_text(self.locator.username, username)

    def enter_password(self,password):
        """Enter the given string into the password field"""
        self.selib.input_text(self.locator.password, password)

    def click_the_submit_button(self):
        """Click the submit button, and wait for the page to reload"""
        with self._wait_for_page_refresh():
            self.selib.click_button(self.locator.submit_button)

if __name__=='__main__':
    lp = LoginPage()
    print(lp._locators)