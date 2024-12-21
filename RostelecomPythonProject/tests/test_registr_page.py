import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.registr_page import RegPage


@pytest.fixture(scope="function")
def firefox_browser(web_browser):
    return RegPage(web_browser)


def test_page_left_lk(firefox_browser):
    firefox_browser.standard_auth_btn.click()

    lk = WebDriverWait(firefox_browser._web_driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="page-left"]/div/div[2]/h2'))
    )
    assert lk.text == 'Личный кабинет'


def test_page_left_desc(firefox_browser):
    firefox_browser.standard_auth_btn.click()

    inf = WebDriverWait(firefox_browser._web_driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="page-left"]/div/div[2]/p'))
    )
    assert inf.text == 'Персональный помощник в цифровом мире Ростелекома'


def test_reg_page_all_fields(firefox_browser):
    firefox_browser.standard_auth_btn.click()
    firefox_browser.btn_kc_register.click()
    time.sleep(1)

    first_name_span_xpath = '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/span'
    second_name_span_xpath = '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/span'
    region_span_xpath = '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/div/span'
    email_or_phone_span_xpath = '//*[@id="page-right"]/div/div[1]/div/form/div[3]/div/div/span'
    password_span_xpath = '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[1]/div/span'
    confirm_password_span_xpath = '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[2]/div/span'

    first_name_span = WebDriverWait(firefox_browser._web_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, first_name_span_xpath))
    )
    assert first_name_span.text == 'Имя'

    second_name_span = WebDriverWait(firefox_browser._web_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, second_name_span_xpath))
    )
    assert second_name_span.text == 'Фамилия'

    region_span = WebDriverWait(firefox_browser._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, region_span_xpath))
    )
    assert region_span.text == 'Регион'

    email_or_phone_span = WebDriverWait(firefox_browser._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, email_or_phone_span_xpath))
    )
    assert email_or_phone_span.text == 'E-mail или мобильный телефон'

    password_span = WebDriverWait(firefox_browser._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, password_span_xpath))
    )
    assert password_span.text == 'Пароль'

    confirm_password_span = WebDriverWait(firefox_browser._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, confirm_password_span_xpath))
    )
    assert confirm_password_span.text == 'Подтверждение пароля'


def test_reg_page_register_button_text_color(firefox_browser):
    firefox_browser.standard_auth_btn.click()
    firefox_browser.btn_kc_register.click()
    time.sleep(1)

    register_button_text = firefox_browser.btn_register.get_text()
    assert register_button_text == 'Зарегистрироваться'
    register_button = firefox_browser._web_driver.find_element(By.XPATH, '//button[@name="register"]')
    button_color = register_button.value_of_css_property('background-color')
    expected_color = 'rgb(255, 79, 18)'
    assert button_color == expected_color


def test_reg_page_reg_policy(firefox_browser):

    firefox_browser.standard_auth_btn.click()
    firefox_browser.btn_kc_register.click()
    time.sleep(1)

    auth_policy = WebDriverWait(firefox_browser._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Нажимая кнопку «Зарегистрироваться», '
                                                  'вы принимаете условия")]'))
    )
    assert auth_policy.text == 'Нажимая кнопку «Зарегистрироваться», вы принимаете условия'
    rt_auth_text = firefox_browser.rt_auth.get_text()

    assert rt_auth_text == 'пользовательского соглашения'


def test_reg_page_help_color(firefox_browser):
    firefox_browser.standard_auth_btn.click()
    time.sleep(1)

    help_modal_text = firefox_browser.help_modal.get_text()
    assert help_modal_text == 'Помощь'
    help_modal = firefox_browser._web_driver.find_element(By.XPATH, '//*[@id="faq-open"]/a')
    element_color = help_modal.value_of_css_property('color')
    expected_color = 'rgb(255, 79, 18)'
    assert element_color == expected_color
    firefox_browser.help_modal.click()

    time.sleep(2)
    heading = WebDriverWait(firefox_browser._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//h1[contains(text(), "Ваш безопасный ключ к сервисам Ростелекома")]'))
    )
    assert heading.text == 'Ваш безопасный ключ к сервисам Ростелекома'
