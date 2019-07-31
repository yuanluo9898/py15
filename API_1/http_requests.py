# -*- coding: utf-8 -*-#
# @time   : 2019/4/18 18:47
# @Author : luoge
import requests

class HTTPRequest:
    """
    使用这个类的request方法去完成不同的HTTP请求，并且返回响应结果
    """

    def request(self, method, url, data=None, json=None, cookies=None):

        method = method.upper()  # 将method强制转成全大小

        if method == 'GET':
            resp = requests.get(url, params=data, cookies=cookies)  # resp 是Response对象
        elif method == 'POST':
            if json:
                resp = requests.post(url, json=json, cookies=cookies)
            else:
                resp = requests.post(url, data=data, cookies=cookies)
        else:
            resp = None
            print('UN-support method')

        return resp

if __name__ == '__main__':
    url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
    params = {"mobilephone": "15810447878", "pwd": "123456"}
    http_request = HTTPRequest()
    res = http_request.request('get',url,params)
    print(res)