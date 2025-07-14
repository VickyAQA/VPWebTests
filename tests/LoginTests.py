from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
import allure


BASE_URL = 'https://ok.ru/'
EMPTY_LOGIN_ERROR = 'Введите логин'
VALID_LOGIN = "second-point@mail.ru"
EMPTY_PASSWORD_ERROR = 'Введите пароль'


@allure.suite('Проверка формы авторизации')
@allure.title('Проверка ошибки при пустой форме авторизации')
def test_empty_login_and_password(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.click_login()
    assert LoginPage.get_error_text() == EMPTY_LOGIN_ERROR


@allure.suite('Проверка формы авторизации')
@allure.title('Проверка ошибки с валидным логином и пустой формой пароля')
def test_login_with_valid_login_and_empty_password(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.enter_login(VALID_LOGIN)
    login_page.enter_password("")
    login_page.click_login()
    assert login_page.get_error_text() == EMPTY_PASSWORD_ERROR, "Текст ошибки не соответствует ожидаемому"





