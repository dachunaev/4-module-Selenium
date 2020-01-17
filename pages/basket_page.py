from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_no_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)

    def should_be_empty_basket_text_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE)
        if "/en-gb/" in self.browser.current_url:
            self.should_be_empty_basket_text_message_correct()

    def should_be_empty_basket_text_message_correct(self):
        should_be_text_message = "Your basket is empty"
        current_text_message = self.get_text(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE)
        assert should_be_text_message in current_text_message, "text message about empty basket incorrect"
