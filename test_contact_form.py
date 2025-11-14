import pytest
from pages.contact_page import ContactPage

URL = "http://127.0.0.1:5500/form.html"  

@pytest.mark.usefixtures("driver")
class TestContactForm:

    def test_positive_valid_data(self, driver):
        """Все поля валидные"""
        page = ContactPage(driver, URL)
        page.open()
        page.fill_form("Точно не я", "maria@mail.ru", "Привет, ты очень крутая")
        page.submit()
        assert "успешно" in page.get_success_message().lower()

    def test_positive_message_with_cyrillic(self, driver):
        """Проверка кириллицы в сообщении"""
        page = ContactPage(driver, URL)
        page.open()
        page.fill_form("Рамиль", "ramil@mail.ru", "Ты действительно классная!")
        page.submit()
        assert "успешно" in page.get_success_message().lower()

    def test_positive_email_format(self, driver):
        """Корректный формат email"""
        page = ContactPage(driver, URL)
        page.open()
        page.fill_form("Оля", "olya@mail.ru", "Я в шоке")
        page.submit()
        assert "успешно" in page.get_success_message().lower()

    def test_negative_empty_name(self, driver):
        """Пустое имя"""
        page = ContactPage(driver, URL)
        page.open()
        page.fill_form("", "test@mail.ru", "Я забыл имя при виде тебя")
        page.submit()
        error_message = page.get_error_message().lower()
        assert error_message != "" 

    def test_negative_empty_message(self, driver):
        """Пустое сообщение"""
        page = ContactPage(driver, URL)
        page.open()
        page.fill_form("Алексей", "alexey@mail.ru", "")
        page.submit()
        error_message = page.get_error_message().lower()
        assert error_message != ""
