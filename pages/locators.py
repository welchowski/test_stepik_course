from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LINK = "http://selenium1py.pythonanywhere.com"


class LoginPageLocators():
    REGISTR_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    REGESTRATION_EMAIL = (By.NAME, "registration-email")
    REGESTRATION_PASSWORD = (By.NAME, "registration-password1")
    CONFIRM_PASSWORD = (By.NAME, "registration-password2")
    REGESTRATION_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators():
    PARAM_LINK_HANDBOOK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    MSG_PRODUCT_ADDED = (By.CSS_SELECTOR, ".alertinner :nth-child(1)")
    LINK_HANDBOOK = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, "h1")
    PRICE = (By.CSS_SELECTOR, ".price_color")


class BasketPageLocators():
    MSG_PRODUCT_ADDED = (By.CSS_SELECTOR, ".alertinner :nth-child(1)")
    PRICE_MSG = (By.CSS_SELECTOR, ".alert-info strong")
    BASKET_INFO_OF_PRODUCT = (By.CSS_SELECTOR, ".basket-title hidden-xs")
    BASKET_IS_EMPTY_MSG = (By.CSS_SELECTOR, "p :nth-child(1)")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BOTTOM = (By.CSS_SELECTOR, "span :nth-child(1)")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
