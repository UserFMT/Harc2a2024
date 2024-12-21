import pytest
import allure

from mainPage import mainPage
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
URL = "https://www.sibdar-spb.ru/"
selector = "addToCard('178', this, event);"
basket_count = 0
product_delete = 5


def test_add_basket():
    basePage = mainPage(driver, URL)
    #basePage.buttons_click('[class="btn-default js-order"]')
    with allure.step('Добавляем все товары активной страницы в корзину'):
        basePage.add_basket('[class="btn-default js-order"]')
    with allure.step('Сверяем кол-во товаров на странице и кол-во товаров в корзине'):
        basket_count = len(basePage.elements_selector('[class="btn-default js-order"]'))
        assert basePage.basket_count('bask_ic_count') == f"{basket_count} шт"


def test_delete_basket():
    basePage = mainPage(driver, URL)
    with allure.step('Добавляем все товары активной страницы в корзину'):
        basePage.add_basket('[class="btn-default js-order"]')
        basket_count = len(basePage.elements_selector('[class="btn-default js-order"]'))
    with allure.step('Переходим в корзину'):
        basePage.element_path('/html/body/header/div/div/div[2]/div/a').click()
        waiter = WebDriverWait(driver,10)
    with allure.step(f'Удаляем из корзины {product_delete} элементов'):
        basePage.delete_count_basket('order_item', '[class ="delet_pr_bas"]',product_delete)
    with allure.step('Проверяем остаток элементов в корзине'):
        assert len( basePage.elements_class('order_item')) == basket_count-product_delete
        waiter = WebDriverWait(driver, 20)


def test_edit_basket():
    basePage = mainPage(driver, URL)
    with allure.step('Добавляем все товары активной страницы в корзину'):
        basePage.add_basket('[class="btn-default js-order"]')
    with allure.step('Переходим в корзину'):
        basePage.element_path('/html/body/header/div/div/div[2]/div/a').click()
        waiter = WebDriverWait(driver, 10)
    with allure.step('Добавляем каждому товару 1 ед.'):
        products =  basePage.elements_class('order_item')
        for product_one in products:
            product_one.find_element(By.CSS_SELECTOR, '[class="plus_prod"]').click()
    with allure.step('Обновляем окно браузера и возвращаемся в корзину'):
        driver.refresh()
        basePage.element_path('/html/body/header/div/div/div[2]/div/a').click()
    with allure.step('Все элементы в корзине по 2 шт'):
        flag = True
        products =  basePage.elements_class('order_item')
        for product_one in products:
           cc = product_one.find_element(By.CSS_SELECTOR,'[name="colprod"]').get_attribute('value')
           if (cc != '2 шт'): flag = False
        assert flag is True
        waiter = WebDriverWait(driver, 20)

