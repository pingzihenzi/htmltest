from multiprocessing.sharedctypes import Value
from sqlite3 import Timestamp
from turtle import down
import requests
import json
from datetime import datetime
from urllib import parse
import os
import re


templist = [
    {'gid': 6578, 'times': '橘子画苑上午场', 'id': 6578, 'price': '3477.83', 'name': '【诚信是金2】B', 'img': 'https://api.dpjppta.com/upload_files/goods/20220730/5cf14147267ff1f3a19a07fa664984bb.jpeg', 'time': '2022-08-04 09:37', 'dollar': 519.08}, 
    {'gid': 5311, 'times': '橘子画苑下午场', 'id': 5311, 'price': '5454.42', 'name': '【淡泊明志】D', 'img': 'https://api.dpjppta.com/upload_files/goods/20220718/0836462e31ef117fdfbec440422e1efa.jpeg', 'time': '2022-08-04 14:32', 'dollar': 814.09},
    {'gid': 5245, 'times': '橘子画苑下午场', 'id': 5245, 'price': '5124.33', 'name': '【春和景明】B', 'img': 'https://api.dpjppta.com/upload_files/goods/20220718/6d7bc00c4c51441195322bc95cc9028d.jpeg', 'time': '2022-08-04 14:55', 'dollar': 764.83}, 
    {'gid': 3424, 'times': '橘子画苑上午场', 'id': 3424, 'price': '4157.63', 'name': '【紫气东来】C', 'img': 'https://api.dpjppta.com/upload_files/goods/20220627/10b23203b9bebd309e685a48d779652c.jpeg', 'time': '2022-08-04 09:40', 'dollar': 620.54}
    ]
uplist = []
downlist = []

for orderinfo in templist:
    for (key,value) in orderinfo.items():
        if key == "times":
            if '上午' in value:
                asset = orderinfo['gid']
                uplist.append(asset)
            elif '下午':
               asset = orderinfo['gid']
               downlist.append(asset)
               


