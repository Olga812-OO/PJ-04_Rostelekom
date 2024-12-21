import pytest
import os
import time

from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.registr_page import RegPage

load_dotenv()

valid_email = os.getenv('valid_email')
valid_phone = os.getenv('valid_phone')

valid_password_email = os.getenv('valid_password_email')
valid_password_phone = os.getenv('valid_password_phone')


@pytest.fixture(scope="function")
def firefox_browser(web_browser):
    return RegPage(web_browser)


def test_reg_email_exists(firefox_browser):
    firefox_browser.standard_auth_btn.click()
    firefox_browser.btn_kc_register.click()
    time.sleep(1)

    firefox_browser.input_first_name.send_keys('Ольга')
    firefox_browser.input_last_name.send_keys('Орехова')
    firefox_browser.region.click()
    choose_region = WebDriverWait(firefox_browser._web_driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//section[@id="page-right"]/div/div/div/form/div[2]/div[2]/div[2]'
                                                  '/div/div[15]'))
    )
    choose_region.click()
    firefox_browser.input_email_or_phone.send_keys(valid_email)
    firefox_browser.input_password.send_keys(valid_password_phone)
    firefox_browser.input_confirm_password.send_keys(valid_password_phone)
    firefox_browser.btn_register.click()
    time.sleep(10)
    alert_title = WebDriverWait(firefox_browser._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div/div/h2'))
    )
    assert alert_title.text == 'Учётная запись уже существует'
    time.sleep(5)


def test_reg_phone_exists(firefox_browser):
    firefox_browser.standard_auth_btn.click()
    firefox_browser.btn_kc_register.click()
    time.sleep(1)

    firefox_browser.input_first_name.send_keys('Ольга')
    firefox_browser.input_last_name.send_keys('Орехова')
    firefox_browser.region.click()
    choose_region = WebDriverWait(firefox_browser._web_driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//section[@id="page-right"]/div/div/div/form/div[2]/div[2]/div[2]'
                                                  '/div/div[15]'))
    )
    choose_region.click()
    firefox_browser.input_email_or_phone.send_keys(valid_phone)
    firefox_browser.input_password.send_keys(valid_password_phone)
    firefox_browser.input_confirm_password.send_keys(valid_password_phone)
    firefox_browser.btn_register.click()
    time.sleep(10)
    alert_title = WebDriverWait(firefox_browser._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div/div/h2'))
    )
    assert alert_title.text == 'Учётная запись уже существует'
    time.sleep(3)


def test_invalid_reg(firefox_browser):
    firefox_browser.standard_auth_btn.click()
    firefox_browser.btn_kc_register.click()
    time.sleep(1)

    firefox_browser.input_first_name.send_keys('111')
    firefox_browser.input_last_name.send_keys('222')

    firefox_browser.input_email_or_phone.send_keys('violetmail.ru')
    firefox_browser.input_password.send_keys('промапра')
    firefox_browser.input_confirm_password.send_keys('промапра')
    firefox_browser.btn_register.click()
    time.sleep(5)

    input_error_first_name = WebDriverWait(firefox_browser._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/span'))
    )
    assert input_error_first_name.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

    input_error_second_name = WebDriverWait(firefox_browser._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/span'))
    )
    assert input_error_second_name.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

    input_error_region = WebDriverWait(firefox_browser._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/span'))
    )
    assert input_error_region.text == 'Укажите регион'

    input_error_email_or_phone = WebDriverWait(firefox_browser._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[3]/div/span'))
    )
    assert input_error_email_or_phone.text == ('Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email'
                                               ' в формате example@email.ru')

    password_error = WebDriverWait(firefox_browser._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[1]/span'))
    )
    assert password_error.text == 'Пароль должен содержать только латинские буквы'


def test_reg_password_invalid_lower(firefox_browser):
    firefox_browser.standard_auth_btn.click()
    firefox_browser.btn_kc_register.click()
    time.sleep(1)

    firefox_browser.input_first_name.send_keys('Ольга')
    firefox_browser.input_last_name.send_keys('Орехова')

    firefox_browser.region.click()
    choose_region = WebDriverWait(firefox_browser._web_driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//section[@id="page-right"]/div/div/div/form/div[2]/div[2]/div[2]'
                                                  '/div/div[15]'))
    )
    choose_region.click()

    firefox_browser.input_email_or_phone.send_keys(valid_email)
    firefox_browser.input_password.send_keys('kjhkhhgjhjkh5')
    firefox_browser.input_confirm_password.send_keys('kjhkhhgjhjkh5')
    firefox_browser.btn_register.click()
    time.sleep(3)

    password_error = WebDriverWait(firefox_browser._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[1]/span'))
    )
    assert password_error.text == 'Пароль должен содержать хотя бы одну заглавную букву'


def test_reg_password_invalid_caps(firefox_browser):
    firefox_browser.standard_auth_btn.click()
    firefox_browser.btn_kc_register.click()
    time.sleep(1)

    firefox_browser.input_first_name.send_keys('Ольга')
    firefox_browser.input_last_name.send_keys('Орехова')

    firefox_browser.region.click()
    choose_region = WebDriverWait(firefox_browser._web_driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//section[@id="page-right"]/div/div/div/form/div[2]/div[2]/div[2]'
                                                  '/div/div[15]'))
    )
    choose_region.click()

    firefox_browser.input_email_or_phone.send_keys(valid_email)
    firefox_browser.input_password.send_keys('GJJHGJHGJHGGF6')
    firefox_browser.input_confirm_password.send_keys('GJJHGJHGJHGGF6')
    firefox_browser.btn_register.click()

    password_error = WebDriverWait(firefox_browser._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[1]/span'))
    )
    assert password_error.text == 'Пароль должен содержать хотя бы одну строчную букву'


def test_reg_password_invalid_length(firefox_browser):
    firefox_browser.standard_auth_btn.click()
    firefox_browser.btn_kc_register.click()
    time.sleep(1)

    firefox_browser.input_first_name.send_keys('Ольга')
    firefox_browser.input_last_name.send_keys('Орехова')

    firefox_browser.region.click()
    choose_region = WebDriverWait(firefox_browser._web_driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//section[@id="page-right"]/div/div/div/form/div[2]/div[2]/div[2]'
                                                  '/div/div[15]'))
    )
    choose_region.click()

    firefox_browser.input_email_or_phone.send_keys(valid_email)
    firefox_browser.input_password.send_keys('111')
    firefox_browser.input_confirm_password.send_keys('111')
    firefox_browser.btn_register.click()

    password_error = WebDriverWait(firefox_browser._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[1]/span'))
    )
    assert password_error.text == 'Длина пароля должна быть не менее 8 символов'
