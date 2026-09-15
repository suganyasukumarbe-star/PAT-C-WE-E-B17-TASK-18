from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page Object for Zen Portal Login and Dashboard interactions."""

    # Locators (Update these locators matching your Zen portal's actual HTML elements)
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-btn")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-msg")
    DASHBOARD_MARKER = (By.ID, "dashboard-main")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Logout')]")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_username(self, username):
        self.send_keys_to_element(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.send_keys_to_element(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click_element(self.LOGIN_BUTTON)

    def click_logout(self):
        self.click_element(self.LOGOUT_BUTTON)

    def is_login_textbox_displayed(self):
        return self.is_element_displayed(self.USERNAME_INPUT)

    def is_password_textbox_displayed(self):
        return self.is_element_displayed(self.PASSWORD_INPUT)

    def is_login_button_displayed(self):
        return self.is_element_displayed(self.LOGIN_BUTTON)

    def is_dashboard_displayed(self):
        return self.is_element_displayed(self.DASHBOARD_MARKER)

    def is_error_message_displayed(self):
        return self.is_element_displayed(self.ERROR_MESSAGE)
