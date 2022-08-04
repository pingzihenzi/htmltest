from sqlite3 import Timestamp
import requests
import json
from datetime import datetime
from urllib import parse, response
import os


"""
脚本运行逻辑：
1、调用登录接口，实时获取token
2、获取对应账户的待拍批次id
3、调用toordergoods接口下单
"""

def get_token(login_body):
    """
    实时调用登录接口，获取token
    :return:
    """
    response = requests.post(
        url="https://api.dpjppta.com/api/Login/login.api",  # 对外登录接口
        headers={'Content-Type':'application/x-www-form-urlencoded'},  # 写死请求头,
        params=login_body
    )
    res = response.json()
    token = res['data']['token']
    return token


def get_ordered_list(query_body):
    """
    调用获取当前待被买接口，获取待被买的订单号
    区分上午场和下午场
    """
    response = requests.get(
        url="https://api.dpjppta.com/api/seller/Orderlist.api",
        headers={'Content-Type':'application/x-www-form-urlencoded'},
        params=query_body
    )
    res = response.json()
    order_up = res['data']['OrderList']
    return order_up



if __name__ == '__main__':
    me_sign = "bd7710aeaa934978552dc04928d824f4"
    me_login = {
        "mobile": "13776675187","password": "huangC123","token": "","sign": me_sign,"timestamp": "1659514505"
    }
    token_me = get_token(me_login)
    print(token_me)
    me_query = {
        "page":1,"type":1,"token":token_me,"sign":me_sign,"timestamp":"1659514505"
    }
    orderlist_me = get_ordered_list(me_query)
    print(orderlist_me)
