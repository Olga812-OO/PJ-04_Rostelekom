from pages.base import WebPage
from pages.elements import WebElement


class RegPage(WebPage):
    def __init__(self, web_driver, url=''):
        url = 'https://lk.rt.ru/'
        super().__init__(web_driver, url)

    standard_auth_btn = WebElement(xpath='//*[@id="standard_auth_btn"]')
    input_first_name = WebElement(xpath='//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/input')
    input_last_name = WebElement(xpath='//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input')

    region = WebElement(xpath='//input[@class="rt-input__input rt-select__input rt-input__input--rounded rt-input'
                              '__input--orange"]')
    input_region = WebElement(xpath='//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/div/input')
    opt_region = WebElement(class_name='rt-input.rt-input--rounded.rt-input--orange.rt-input--actions')
    input_email_or_phone = WebElement(xpath='//*[@id="address"]')
    input_password = WebElement(xpath='//*[@id="password"]')
    input_confirm_password = WebElement(xpath='//*[@id="password-confirm"]')

    btn_kc_register = WebElement(xpath='//*[@id="kc-register"]')
    btn_register = WebElement(xpath='//*[@id="page-right"]/div/div[1]/div/form/button')
    rt_auth = WebElement(xpath='//*[@id="rt-auth-agreement-link"]')
    help_modal = WebElement(xpath='//*[@id="faq-open"]/a')

    region_selector = WebElement(xpath='//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/div/input')
