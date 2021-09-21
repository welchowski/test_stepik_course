from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def register_new_user(self, email, password, browser):
        browser.find_element(*LoginPageLocators.LOGIN_LINK).click()
        browser.find_element(*LoginPageLocators.REGESTRATION_EMAIL).send_keys(email)
        browser.find_element(*LoginPageLocators.REGESTRATION_PASSWORD).send_keys(password)
        browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD).send_keys(password)
        browser.find_element(*LoginPageLocators.REGESTRATION_BUTTON).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "url has not 'login' in self  "

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login_form absent"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTR_FORM), "registr_form absent"
