from .pages.basket_page import BasketPage
from .pages.locators import MainPageLocators
from .pages.login_page import LoginPage
from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, MainPageLocators.LINK)
    page.open()
    page.open_basket_page()
    page.basket_should_not_be_full()
    page.should_be_empty_basket_massage()
