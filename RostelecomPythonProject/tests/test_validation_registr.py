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


def test_successful_registration_by_email(firefox_browser):
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
    firefox_browser.input_password.send_keys(valid_password_email)
    firefox_browser.input_confirm_password.send_keys(valid_password_email)

    firefox_browser.btn_register.click()
    time.sleep(10)
    confirm_phone_title = WebDriverWait(firefox_browser._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div/h1'))
    )
    assert confirm_phone_title.text == 'Подтверждение email'


def test_successful_registration_by_phone(firefox_browser):
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
    confirm_phone_title = WebDriverWait(firefox_browser._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div/h1'))
    )
    assert confirm_phone_title.text == 'Подтверждение телефона'


