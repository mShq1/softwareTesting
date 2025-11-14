from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage

def test_login_success(browser):
    login_url = "https://practicetestautomation.com/practice-test-login/"
    valid_username = "student"
    valid_password = "Password123"

    login_page = LoginPage(browser)
    login_page.open(login_url)

    login_page.enter_username(valid_username)
    login_page.enter_password(valid_password)
    login_page.click_login()

    success_message_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(login_page.success_message)
    )
    
    success_text = success_message_element.text
    assert "Logged In Successfully" in success_text, f"Не найдено сообщение: 'Logged In Successfully', найдено: {success_text}"

def test_login_invalid_password(browser):
    login_url = "https://practicetestautomation.com/practice-test-login/"
    invalid_username = "maria"
    invalid_password = "stepanchuk"

    login_page = LoginPage(browser)
    login_page.open(login_url)

    login_page.enter_username(invalid_username)
    login_page.enter_password(invalid_password)
    login_page.click_login()

    error_message_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "error"))
    )
    
    error_message = error_message_element.text
    assert "Your password is invalid!" in error_message, f"Не найдено сообщение об ошибке: 'Your password is invalid!', найдено: {error_message}"
