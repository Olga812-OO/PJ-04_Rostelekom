import pytest
import os
import time

from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from pages.auth_page import AuthPage

load_dotenv()

invalid_phone = os.getenv('invalid_phone')
invalid_email = os.getenv('invalid_email')
invalid_login = os.getenv('invalid_login')

invalid_password = os.getenv('invalid_password')


@pytest.fixture(scope="function")
def firefox_browser(web_browser):
    return AuthPage(web_browser)


def test_invalid_auth_email(firefox_browser):
    firefox_browser.standard_auth_btn.click()
    time.sleep(1)
    firefox_browser.btn_tab_email.click()

    forgot_password_text = firefox_browser.forgot_password.get_text()
    assert forgot_password_text == 'Забыл пароль'
    forgot_password = firefox_browser._web_driver.find_element(By.XPATH, '//*[@id="forgot_password"]')
    element_color = forgot_password.value_of_css_property('color')
    expected_color = 'rgba(16, 24, 40, 0.5)'
    assert element_color == expected_color  # проверяем что элемент "Забыл пароль" окрашен в серый цвет

    firefox_browser.input_username.send_keys(invalid_email)
    firefox_browser.input_password.send_keys(invalid_password)
    time.sleep(15)  # чтобы ввести капчу
    firefox_browser.btn_enter.click()
    time.sleep(3)

    error_message = firefox_browser._web_driver.find_element(By.ID, 'form-error-message')
    assert error_message.text == 'Неверный логин или пароль'

    forgot_password = firefox_browser._web_driver.find_element(By.XPATH, '//*[@id="forgot_password"]')
    element_color = forgot_password.value_of_css_property('color')
    expected_color = 'rgb(255, 79, 18)'
    assert element_color == expected_color  # проверяем что элемент "Забыл пароль" окрашен в оранжевый цвет


def test_invalid_auth_phone(firefox_browser):
    firefox_browser.standard_auth_btn.click()
    time.sleep(1)

    forgot_password_text = firefox_browser.forgot_password.get_text()
    assert forgot_password_text == 'Забыл пароль'
    forgot_password = firefox_browser._web_driver.find_element(By.XPATH, '//*[@id="forgot_password"]')
    element_color = forgot_password.value_of_css_property('color')
    expected_color = 'rgba(16, 24, 40, 0.5)'
    assert element_color == expected_color  # проверяем что элемент "Забыл пароль" окрашен в серый цвет

    firefox_browser.input_username.send_keys(invalid_phone)
    firefox_browser.input_password.send_keys(invalid_password)
    time.sleep(15)  # чтобы ввести капчу
    firefox_browser.btn_enter.click()
    time.sleep(3)

    error_message = firefox_browser._web_driver.find_element(By.ID, 'form-error-message')
    assert error_message.text == 'Неверный логин или пароль'

    forgot_password = firefox_browser._web_driver.find_element(By.XPATH, '//*[@id="forgot_password"]')
    element_color = forgot_password.value_of_css_property('color')
    expected_color = 'rgb(255, 79, 18)'
    assert element_color == expected_color  # проверяем что элемент "Забыл пароль" окрашен в оранжевый цвет


def test_invalid_auth_login(firefox_browser):
    firefox_browser.standard_auth_btn.click()
    firefox_browser.btn_tab_login.click()

    forgot_password_text = firefox_browser.forgot_password.get_text()
    assert forgot_password_text == 'Забыл пароль'
    forgot_password = firefox_browser._web_driver.find_element(By.XPATH, '//*[@id="forgot_password"]')
    element_color = forgot_password.value_of_css_property('color')
    expected_color = 'rgba(16, 24, 40, 0.5)'
    assert element_color == expected_color  # проверяем что элемент "Забыл пароль" окрашен в серый цвет

    firefox_browser.input_username.send_keys(invalid_login)
    firefox_browser.input_password.send_keys(invalid_password)
    time.sleep(15)  # чтобы ввести капчу
    firefox_browser.btn_enter.click()
    time.sleep(3)

    error_message = firefox_browser._web_driver.find_element(By.ID, 'form-error-message')
    assert error_message.text == 'Неверный логин или пароль'

    forgot_password = firefox_browser._web_driver.find_element(By.XPATH, '//*[@id="forgot_password"]')
    element_color = forgot_password.value_of_css_property('color')
    expected_color = 'rgb(255, 79, 18)'
    assert element_color == expected_color  # проверяем что элемент "Забыл пароль" окрашен в оранжевый цвет
