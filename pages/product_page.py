from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button_basket = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button_basket.click()

    def should_be_added(self):
        self.should_be_alert_messages()
        self.should_be_alert_product_name_correct()
        self.should_be_alert_product_price_correct()

    def should_be_alert_messages(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_MESSAGES), "alert messages not found"

    def should_be_alert_product_name_correct(self):
        product_name = self.get_text(*ProductPageLocators.PRODUCT_NAME)
        product_name_alert = self.get_text(*ProductPageLocators.SUCCESS_PRODUCT_NAME)
        assert product_name_alert == product_name, "incorrect product name in alert message"

    def should_be_alert_product_price_correct(self):
        product_price = self.get_text(*ProductPageLocators.PRODUCT_PRICE)
        product_price_in_basket = self.get_text(*ProductPageLocators.BASKET_PRICE)
        assert product_price in product_price_in_basket, "incorrect product price in alert message"
