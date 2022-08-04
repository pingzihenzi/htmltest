from sqlite3 import Timestamp
import requests
import json
from datetime import datetime
from urllib import parse
import os


"""
脚本运行逻辑：
1、调用登录接口，实时获取token
2、获取对应账户的待拍批次id
3、调用toordergoods接口下单
"""

def get_token(body):
    """
    实时调用登录接口，获取token
    :return:
    """
    response = requests.post(
        url="https://api.dpjppta.com/api/Login/login.api",  # 对外登录接口
        headers={
            'content-type': 'application/x-www-form-urlencoded'  # 写死请求头
        },
        data=body
    )
    res = response.json()
    token = res['data']['token']
    return token
