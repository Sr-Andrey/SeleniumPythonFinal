from .base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    # Локаторы элементов
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_TOTAL = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")

    def add_product_to_basket(self):
            """Добавляет товар в корзину."""
            add_button = self.browser.find_element(*self.ADD_TO_BASKET_BUTTON)
            add_button.click()

    def get_product_name(self):
        """Возвращает название товара."""
        return self.browser.find_element(*self.PRODUCT_NAME).text

    def get_product_price(self):
        """Возвращает цену товара."""
        return self.browser.find_element(*self.PRODUCT_PRICE).text

    def get_success_message(self):
        """Возвращает сообщение о добавлении товара."""
        return self.browser.find_element(*self.SUCCESS_MESSAGE).text

    def get_basket_total(self):
        """Возвращает сумму корзины."""
        return self.browser.find_element(*self.BASKET_TOTAL).text

    def should_be_success_message(self, product_name):
        """Проверяет, что сообщение о добавлении товара соответствует названию товара."""
        success_message = self.get_success_message()
        assert success_message == product_name, (
            f"Product name in success message ('{success_message}') does not match the actual product name ('{product_name}')"
        )

    def should_be_correct_basket_total(self, product_price):
        """Проверяет, что сумма корзины совпадает с ценой товара."""
        basket_total = self.get_basket_total()
        assert basket_total == product_price, (
            f"Basket total ('{basket_total}') does not match the product price ('{product_price}')"
        )
