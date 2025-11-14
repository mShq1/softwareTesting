from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "submit")
        self.success_message = (By.CSS_SELECTOR, "h1.post-title")
        self.logout_button = (By.LINK_TEXT, "Log out")

    def open(self, url: str):
        self.driver.get(url)

    def enter_username(self, username: str):
        elem = self.driver.find_element(*self.username_input)
        elem.clear()
        elem.send_keys(username)

    def enter_password(self, password: str):
        elem = self.driver.find_element(*self.password_input)
        elem.clear()
        elem.send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def is_logged_in(self) -> bool:
        try:
            return self.driver.find_element(*self.logout_button).is_displayed()
        except Exception:
            return False
