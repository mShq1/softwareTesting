from selenium.webdriver.common.by import By
from .base_page import BasePage

class ContactPage(BasePage):
    NAME_FIELD = (By.ID, "name")
    EMAIL_FIELD = (By.ID, "email")
    MESSAGE_FIELD = (By.ID, "message")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    SUCCESS_MSG = (By.CSS_SELECTOR, "#success")
    ERROR_MSG = (By.CSS_SELECTOR, "#error")

    def fill_form(self, name, email, message):
        self.fill(self.NAME_FIELD, name)
        self.fill(self.EMAIL_FIELD, email)
        self.fill(self.MESSAGE_FIELD, message)

    def submit(self):
        self.click(self.SUBMIT_BUTTON)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MSG)

    def get_error_message(self):
        return self.get_text(self.ERROR_MSG)
