import pytest
from selenium import webdriver
from .pages.product_page import ProductPage

@pytest.fixture(scope="function")
def browser():
    """Фикстура для инициализации браузера."""
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


# Параметризация ссылок
@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()

    # Получаем название товара и его цену
    product_name = page.get_product_name()
    product_price = page.get_product_price()

    # Добавляем товар в корзину
    page.add_product_to_basket()

    # Решаем математическую задачу
    page.solve_quiz_and_get_code()

    # Проверяем сообщение о добавлении товара
    page.should_be_success_message(product_name)

    # Проверяем сумму корзины
    page.should_be_correct_basket_total(product_price)



def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    pass
