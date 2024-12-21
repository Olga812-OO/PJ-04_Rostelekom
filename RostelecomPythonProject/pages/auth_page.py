from pages.base import WebPage
from pages.elements import WebElement


class AuthPage(WebPage):
    def __init__(self, web_driver, url=''):
        url = 'https://lk.rt.ru/'
        super().__init__(web_driver, url)

    standard_auth_btn = WebElement(xpath='//*[@id="standard_auth_btn"]')
    btn_tab_phone = WebElement(xpath='//*[@id="t-btn-tab-phone"]')
    btn_tab_email = WebElement(xpath='//*[@id="t-btn-tab-mail"]')
    btn_tab_login = WebElement(xpath='//*[@id="t-btn-tab-login"]')
    btn_tab_ls = WebElement(xpath='//*[@id="t-btn-tab-ls"]')
    input_username = WebElement(xpath='//*[@id="username"]')
    input_password = WebElement(xpath='//*[@id="password"]')
    forgot_password = WebElement(xpath='//*[@id="forgot_password"]')
    btn_enter = WebElement(xpath='//*[@id="kc-login"]')
    back_to_otp_btn = WebElement(xpath='//*[@id="back_to_otp_btn"]')
    rt_auth = WebElement(xpath='//*[@id="rt-auth-agreement-link"]')
    btn_tinkoff = WebElement(xpath='//*[@id="oidc_tinkoff"]')
    btn_yandex = WebElement(xpath='//*[@id="oidc_ya"]')
    btn_vk = WebElement(xpath='//*[@id="oidc_vk"]')
    btn_mail = WebElement(xpath='//*[@id="oidc_mail"]')
    btn_ok = WebElement(xpath='//*[@id="oidc_ok"]')
    help_modal = WebElement(xpath='//*[@id="faq-open"]/a')
    btn_register = WebElement(xpath='//*[@id="kc-register"]')
