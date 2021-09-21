from .base_page import BasePage
from .locators import BasketPageLocators, LoginPageLocators, ProductPageLocators, MainPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def should_not_be_success_message(self):
        assert not self.is_element_present(*ProductPageLocators.MSG_PRODUCT_ADDED), \
            "Success message is presented"

    def should_be_msg_same_produsct_added_to_basket(self):
        name = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
        print(name)
        msg = self.browser.find_element(*BasketPageLocators.MSG_PRODUCT_ADDED).text
        assert name == msg, "name of product don't same"

    def should_be_single_price_with_product_added(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        msg_price = self.browser.find_element(*BasketPageLocators.PRICE_MSG).text
        print(self.browser.find_element(*ProductPageLocators.PRICE).text)
        print("price=" + price + " msg_prise=" + msg_price)
        assert price in msg_price, "price difference"

    def should_go_to_login_page_from_product_page(self):
        login_button = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_button.click()
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "register form not found"

    def should_not_be_success_message_by_is_not_element_present(self):
        assert self.is_not_element_present(*BasketPageLocators.MSG_PRODUCT_ADDED), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_by_is_disappeared(self):
        assert self.is_disappeared(*BasketPageLocators.MSG_PRODUCT_ADDED), \
            "Success message is presented, but should not be"
