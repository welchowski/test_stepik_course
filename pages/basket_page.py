from .base_page import BasePage
from .locators import BasePageLocators, BasketPageLocators


class BasketPage(BasePage):
    def open_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_BOTTOM)
        link.click()

    def basket_should_not_be_full(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_INFO_OF_PRODUCT), \
            "Basket is not empty"

    def should_be_empty_basket_massage(self):
        msg = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY_MSG)
        assert self.is_not_element_present(*BasketPageLocators.BASKET_INFO_OF_PRODUCT), \
            "Basket is not empty"
