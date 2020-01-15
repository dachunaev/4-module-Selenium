from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_INPUT_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_INPUT_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_LINK_RECOVERY = (By.CSS_SELECTOR, "a[href='/ru/password-reset/']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[name='login_submit']")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_INPUT_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_INPUT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_INPUT_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.basket-mini")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    ALERT_MESSAGES = (By.CSS_SELECTOR, "#messages")
    SUCCESS_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert:nth-child(1) strong")
    SUCCESS_MASSAGE = (By.CSS_SELECTOR, ".alert:nth-child(2) strong")
    SUCCESS_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alert:nth-child(3) strong")
