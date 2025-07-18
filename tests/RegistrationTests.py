from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
import allure
from pages.RegistrationPage import RegistrationPageHelperHelper

BASE_URL = 'https://ok.ru/'

@allure.suite('Проверка регистрации')
@allure.title('Проверка регистрации с рандомными странами')
def test_registration_random_country(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.click_registration()
    RegistrationPage = RegistrationPageHelperHelper(browser)
    selected_country_code = RegistrationPage.select_random_country()
    actual_country_code = RegistrationPage.get_phone_field_value()
    assert selected_country_code == actual_country_code

