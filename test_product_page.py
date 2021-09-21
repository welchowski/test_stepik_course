import faker
import pytest
from .pages.basket_page import BasketPage
from .pages.locators import ProductPageLocators, MainPageLocators
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    print(link)
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()

    page_busket = ProductPage(browser, browser.current_url)
    page_busket.should_be_msg_same_produsct_added_to_basket()
    page_busket.should_be_single_price_with_product_added()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocators.PARAM_LINK_HANDBOOK)
    page.open()
    page.add_to_basket()

    page_busket = ProductPage(browser, browser.current_url)
    page_busket.should_not_be_success_message_by_is_not_element_present()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_go_to_login_page_from_product_page()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, ProductPageLocators.PARAM_LINK_HANDBOOK)
    page.open()
    page = ProductPage(browser, browser.current_url)
    page.should_not_be_success_message_by_is_not_element_present()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocators.PARAM_LINK_HANDBOOK)
    page.open()
    page.add_to_basket()
    page_busket = ProductPage(browser, browser.current_url)
    page_busket.should_not_be_success_message_by_is_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, MainPageLocators.LINK)
    page.open()
    page.open_basket_page()
    page.basket_should_not_be_full()
    page.should_be_empty_basket_massage()


@pytest.mark.login
class TestUserAddToBasketFromProductPage():
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    f = faker.Faker()
    password = "123WE@RF=89"

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = self.f.email()
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.register_new_user(email, self.password, browser)
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.add_to_basket()

        page_basket = ProductPage(browser, browser.current_url)
        page_basket.should_be_msg_same_produsct_added_to_basket()
        page_basket.should_be_single_price_with_product_added()

    @pytest.mark.need_review
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_not_be_success_message_by_is_not_element_present()
