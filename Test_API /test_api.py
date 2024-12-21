import allure
import pytest

import param
from Test_API.param import basketor

from apiPage import apiPage

base_url ='https://www.sibdar-spb.ru'

idCookie = f'"idCookie" : "{param.basketor}"'

data = 'data: {'+ idCookie +',"idProd":"178","type":"add"}'
data_del = 'data: {'+ idCookie +',"idProd":204,"type":"delete"}'

cookie = {"Cookie" : f'basketor={param.basketor}; PHPSESSID=s6vEE2UEfZq1t4glabGu1myRX0hJWrAX'}


def test_add_product_to_basket():
    apitest = apiPage(base_url)
    response = apitest.post_product('/ajax/basketOrder.php', data, cookie)
    assert response.status_code == 200
    aa=response.text

    response = apitest.post_product('/ajax/basketOrder.php', data_del, cookie)
    rr = apitest.post_list('/ajax/basketList.php', cookie)
    assert rr.text != "Корзина"

