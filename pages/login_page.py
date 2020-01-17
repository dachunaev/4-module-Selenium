from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REG_INPUT_EMAIL)
        password_input = self.browser.find_element(*LoginPageLocators.REG_INPUT_PASSWORD)
        confirm_password_input = self.browser.find_element(*LoginPageLocators.REG_INPUT_CONFIRM_PASSWORD)
        email_input.send_keys(email)
        password_input.send_keys(password)
        confirm_password_input.send_keys(password)
        button_reg = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        button_reg.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in f"{self.browser.current_url}", "wrong url, should be login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form not found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Register form not found"
