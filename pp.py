import json
import  time
from datetime import datetime
from time import sleep

from pip._vendor import requests


# 抓包请求
def request_url():
    url = 'https://j1.pupuapi.com/client/product/storeproduct/detail/4dcdeca2-f5a3-4be8-9e2f-e099889a23a0/9da7c562-faaa-4bba-8adf-85549ec8f2f8'
    head = {
        # 浏览器类型
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat'
    }
    # 对url地址发送请求
    respnse = requests.get(url, headers=head, verify=False)

    dict = json.loads(respnse.text)  # 字符串化成字典
    name = dict["data"]["name"]  # 名字
    spec = dict["data"]["spec"]  # 重量
    price = str(int(dict["data"]["price"]) / 100)  # 折扣价
    market_price = str(int(dict["data"]["market_price"]) / 100)  # 原价
    origin = dict["data"]["origin"]  # 地址
    # 输出内容
    print("---------------商品名称：" + name + "-----------------")
    print("重量：" + spec)
    print("折扣价：" + price)
    print("原价：" + market_price)
    print("地址：" + origin)
    print("--------------------------------------------------------")
    # 循环10次更新价格
    i = 1
    while 1<=10:
        # 当前系统时间
        GetNowTime = time.strftime('%Y-%m-%d %H:%M:%S')
        print("当前时间为:"+GetNowTime+"," + name + ":价格为:" + price)
        # 价格3秒刷新一次
        sleep(3)
        i = i + 1
if __name__ == '__main__':
    request_url()
