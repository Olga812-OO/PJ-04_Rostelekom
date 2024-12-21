import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.auth_page import AuthPage


@pytest.fixture(scope="function")
def firefox_browser(web_browser):
    return AuthPage(web_browser)


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


def test_auth_page_title(firefox_browser):
    auth_stand = WebDriverWait(firefox_browser._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="standard_auth_btn"]'))
    )
    time.sleep(1)
    assert auth_stand.text == 'Войти со своим паролем'
    firefox_browser.standard_auth_btn.click()
    time.sleep(1)

    auth_title = WebDriverWait(firefox_browser._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div[1]/h1'))
    )
    time.sleep(3)
    assert auth_title.text == 'Авторизация'


def test_auth_page_all_tabs(firefox_browser):

    firefox_browser.standard_auth_btn.click()
    time.sleep(1)

    phone_tab_text = firefox_browser.btn_tab_phone.get_text()
    email_tab_text = firefox_browser.btn_tab_email.get_text()
    login_tab_text = firefox_browser.btn_tab_login.get_text()
    ls_tab_text = firefox_browser.btn_tab_ls.get_text()

    assert phone_tab_text == 'Телефон'
    assert email_tab_text == 'Почта'
    assert login_tab_text == 'Логин'
    assert ls_tab_text == 'Лицевой счёт'


def test_auth_page_all_fields(firefox_browser):
    username_input_xpath = '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/span'
    password_input_xpath = '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/span'

    firefox_browser.standard_auth_btn.click()
    time.sleep(1)

    username_input = WebDriverWait(firefox_browser._web_driver, 5).until(
        EC.presence_of_element_located((By.XPATH, username_input_xpath))
    )
    assert username_input.text == 'Мобильный телефон'
    password_input = firefox_browser._web_driver.find_element(By.XPATH, password_input_xpath)
    assert password_input.text == 'Пароль'

    firefox_browser.btn_tab_email.click()
    time.sleep(3)
    username_input = WebDriverWait(firefox_browser._web_driver, 5).until(
        EC.presence_of_element_located((By.XPATH, username_input_xpath))
    )
    assert username_input.text == 'Электронная почта'
    password_input = firefox_browser._web_driver.find_element(By.XPATH, password_input_xpath)
    assert password_input.text == 'Пароль'

    firefox_browser.btn_tab_login.click()
    time.sleep(3)
    username_input = WebDriverWait(firefox_browser._web_driver, 5).until(
        EC.presence_of_element_located((By.XPATH, username_input_xpath))
    )
    assert username_input.text == 'Логин'
    password_input = firefox_browser._web_driver.find_element(By.XPATH, password_input_xpath)
    assert password_input.text == 'Пароль'

    firefox_browser.btn_tab_ls.click()
    time.sleep(3)
    username_input = WebDriverWait(firefox_browser._web_driver, 5).until(
        EC.presence_of_element_located((By.XPATH, username_input_xpath))
    )
    assert username_input.text == 'Лицевой счёт'
    password_input = firefox_browser._web_driver.find_element(By.XPATH, password_input_xpath)
    assert password_input.text == 'Пароль'


def test_auth_page_forgot_passw_color(firefox_browser):

    firefox_browser.standard_auth_btn.click()
    time.sleep(1)

    forgot_password_text = firefox_browser.forgot_password.get_text()
    assert forgot_password_text == 'Забыл пароль'
    forgot_password = firefox_browser._web_driver.find_element(By.XPATH, '//*[@id="forgot_password"]')
    element_color = forgot_password.value_of_css_property('color')
    expected_color = 'rgba(16, 24, 40, 0.5)'
    assert element_color == expected_color  # проверяем что элемент "Забыл пароль" окрашен в серый цвет


def test_auth_page_enter_color(firefox_browser):

    firefox_browser.standard_auth_btn.click()
    time.sleep(1)

    enter_button_text = firefox_browser.btn_enter.get_text()
    assert enter_button_text == 'Войти'
    enter_button = firefox_browser._web_driver.find_element(By.XPATH, '//button[@id="kc-login"]')
    button_color = enter_button.value_of_css_property('color')
    expected_color = 'rgb(255, 255, 255)'
    assert button_color == expected_color


# БАГ
def test_auth_page_otp_btn_text(firefox_browser):

    firefox_browser.standard_auth_btn.click()
    time.sleep(1)

    back_to_otp_btn = WebDriverWait(firefox_browser._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="back_to_otp_btn"]'))
    )

    assert back_to_otp_btn.text == 'Войти по временному коду'

    firefox_browser.back_to_otp_btn.click()
    time.sleep(3)
    otp_btn = WebDriverWait(firefox_browser._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//h1[contains(text(), "Вход по временному коду")]'))
    )
    assert otp_btn.text == 'Вход по временному коду'


def test_auth_page_auth_policy(firefox_browser):

    firefox_browser.standard_auth_btn.click()
    time.sleep(1)

    auth_policy = WebDriverWait(firefox_browser._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Нажимая кнопку «Войти», '
                                                  'вы принимаете условия")]'))
    )
    assert auth_policy.text == 'Нажимая кнопку «Войти», вы принимаете условия'
    rt_auth_text = firefox_browser.rt_auth.get_text()

    assert rt_auth_text == 'пользовательского соглашения'


def test_auth_page_tinkoff(firefox_browser):
    firefox_browser.standard_auth_btn.click()
    time.sleep(3)

    social = WebDriverWait(firefox_browser._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "войти другим способом")]'))
    )
    assert (social.text == 'войти другим способом')
    firefox_browser.btn_tinkoff.click()

    tinkoff = WebDriverWait(firefox_browser._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div'))
    )

    assert tinkoff.text == 'Тинькофф теперь Т-Банк, а Tinkoff ID — T-ID'


def test_auth_page_auth_yandex(firefox_browser):
    firefox_browser.standard_auth_btn.click()
    time.sleep(3)

    social = WebDriverWait(firefox_browser._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "войти другим способом")]'))
    )

    assert (social.text == 'войти другим способом')
    firefox_browser.btn_yandex.click()
    time.sleep(6)

    yndx = WebDriverWait(firefox_browser._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "Яндекс")]'))
    )

    assert yndx.text == 'Яндекс'


def test_auth_page_auth_vk(firefox_browser):
    firefox_browser.standard_auth_btn.click()
    time.sleep(1)

    social = WebDriverWait(firefox_browser._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "войти другим способом")]'))
    )
    time.sleep(1)
    assert (social.text == 'войти другим способом')
    firefox_browser.btn_vk.click()
    time.sleep(3)

    vk = WebDriverWait(firefox_browser._web_driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div'
                                                  '/span[2]/span'))
    )
    time.sleep(1)
    assert vk.text == 'Отсканируйте QR-код сканером в приложении ВКонтакте или камерой устройства'


def test_auth_page_auth_mail(firefox_browser):
    firefox_browser.standard_auth_btn.click()
    time.sleep(1)
    social = WebDriverWait(firefox_browser._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "войти другим способом")]'))
    )
    time.sleep(1)
    assert social.text == 'войти другим способом'
    firefox_browser.btn_mail.click()
    time.sleep(1)

    vk = WebDriverWait(firefox_browser._web_driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Мой Мир@Mail.Ru")]'))
    )
    time.sleep(1)
    assert vk.text == 'Мой Мир@Mail.Ru'


def test_auth_page_auth_ok(firefox_browser):
    firefox_browser.standard_auth_btn.click()
    time.sleep(1)
    social = WebDriverWait(firefox_browser._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "войти другим способом")]'))
    )
    time.sleep(1)
    assert (social.text == 'войти другим способом')
    firefox_browser.btn_ok.click()
    time.sleep(3)

    ok = WebDriverWait(firefox_browser._web_driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@class="ext-widget_h_tx"]'))
    )
    time.sleep(1)
    assert ok.text == 'Одноклассники'


def test_auth_page_btn_register_text(firefox_browser):
    firefox_browser.standard_auth_btn.click()
    time.sleep(1)

    btn_register_text = firefox_browser.btn_register.get_text()
    firefox_browser.btn_register.click()
    time.sleep(1)
    reg_title = WebDriverWait(firefox_browser._web_driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//h1[contains(text(), "Регистрация")]'))
    )
    assert btn_register_text == 'Зарегистрироваться'
    assert reg_title.text == 'Регистрация'


def test_auth_page_help_color(firefox_browser):
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
