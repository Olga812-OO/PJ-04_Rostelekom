import pytest
import os
import time

from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.auth_page import AuthPage

load_dotenv()

valid_email = os.getenv('valid_email')
valid_phone = os.getenv('valid_phone')
valid_login = os.getenv('valid_login')

valid_password_email = os.getenv('valid_password_email')
valid_password_phone = os.getenv('valid_password_phone')


@pytest.fixture(scope="function")
def firefox_browser(web_browser):
    return AuthPage(web_browser)


def test_successful_auth_by_email(firefox_browser):
    firefox_browser.standard_auth_btn.click()

    firefox_browser.btn_tab_email.click()
    firefox_browser.input_username.send_keys(valid_email)
    firefox_browser.input_password.send_keys(valid_password_email)
    time.sleep(15)  # чтобы ввести капчу
    firefox_browser.btn_enter.click()
    time.sleep(5)
    heading = WebDriverWait(firefox_browser._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="app-header_profile_header_user"]'))
    )
    user_name = heading.find_element(By.XPATH, './div[1]')
    assert user_name.text == 'Ольга Орехова'


def test_successful_auth_by_phone(firefox_browser):
    firefox_browser.standard_auth_btn.click()
    firefox_browser.input_username.send_keys(valid_phone)
    firefox_browser.input_password.send_keys(valid_password_phone)
    time.sleep(15)  # чтобы ввести капчу
    firefox_browser.btn_enter.click()
    time.sleep(5)
    header = WebDriverWait(firefox_browser._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="app-header_profile_header_user"]'))
    )
    user_name = header.find_element(By.XPATH, './div[1]')
    assert user_name.text == 'Ольга Орехова'


def test_successful_auth_by_login(firefox_browser):
    firefox_browser.standard_auth_btn.click()
    firefox_browser.btn_tab_login.click()
    firefox_browser.input_username.send_keys(valid_login)
    firefox_browser.input_password.send_keys(valid_password_email)
    time.sleep(15)  # чтобы ввести капчу
    firefox_browser.btn_enter.click()
    time.sleep(1)
    header = WebDriverWait(firefox_browser._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="app-header_profile_header_user"]'))
    )
    user_name = header.find_element(By.XPATH, './div[1]')
    assert user_name.text == 'Ольга Орехова'
