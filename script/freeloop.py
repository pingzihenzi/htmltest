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


def get_ordered_list_up(query_body):
    """
    调用获取当前待被买接口，获取上午场待被买的订单号
    """
    uplist = []
    response = requests.get(
        url="https://api.dpjppta.com/api/seller/Orderlist.api",
        headers={'Content-Type':'application/x-www-form-urlencoded'},
        params=query_body
    )
    res = response.json()
    order_up = res['data']['OrderList']
    for orderinfo in order_up:
        for (key,value) in orderinfo.items():
            if key == 'times':
                if '上午' in value:
                    uplist.append(orderinfo['gid'])
    return uplist


def get_ordered_list_down(querybody):
    """
    调用获取当前待被买接口，获取下午场待被买的订单号
    """
    downlist = []
    response = requests.get(
        url="https://api.dpjppta.com/api/seller/Orderlist.api",
        headers={'Content-Type':'application/x-www-form-urlencoded'},
        params=querybody
    )
    res = response.json()
    order_down = res['data']['OrderList']
    for orderinfo in order_down:
        for (key,value) in orderinfo.items():
            if key == 'times':
                if '下午' in value:
                    downlist.append(orderinfo['gid'])
    return downlist





if __name__ == '__main__':
    me_sign = "bd7710aeaa934978552dc04928d824f4"
    me_login = {
        "mobile": "13776675187","password": "huangC123","token": "","sign": me_sign,"timestamp": "1659514505"
    }
    token_me = get_token(me_login)
    me_query = {
        "page":1,"type":1,"token":token_me,"sign":me_sign,"timestamp":"1659514505"
    }
    orderlist_me_up = get_ordered_list_up(me_query)
    print(orderlist_me_up)
    orderlist_me_down = get_ordered_list_down(me_query)
    print(orderlist_me_down)
