import os,sys
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir)
sys.path.append("F:\\python\\YitihuaInterface\\venv\\Lib\\site-packages")


import requests
import unittest
import MySQLdb
import allure
import pytest

class Test(unittest.TestCase):


    # 下单接口
    @allure.feature('test_module_01')
    @allure.story('test_story_01')
    @allure.severity('blocker')
    def test_case_01(self):

        url='http://192.168.1.131:8443/order-service/order/trade/order'
        req={"charset":"UTF-8","content":"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","encryptType":"RSA","format":"format","merchantId":"000002","rsaType":"RSA","sign":"ej28XgnlPA/S947UUIQt2+B/hYtDj/H/XzdAucU2U9L6fKEJE0XJK68E4gp7mBKnANxQw5c+a1MXpz9CM5VIs7z1Yp3psgcrmQKMQwZ6cTenVNGsuEP1XGOBx4KE9LUaL+RLcYFxxhjkcGIvUE3IvupsVXdQHgVGrA7lZeuFsWg=","signType":"RSA","timestamp":"1617248569552","version":"1.0"}
        r=requests.post(url,json=req,headers={'Content-Type':'application/json'})
        print('下单返回结果:', r.text)
        result_dict=r.json()
        code=str(result_dict['code'])
        print('code:',code)
        self.assertEqual(code, '000000', "测试成功")

        assert code==000000


# 查询数据库
        db = MySQLdb.connect("192.168.1.131", "root", "123456", "zxepay_db", charset='utf8')
        cursor = db.cursor()
    # 使用execute方法执行SQL语句
        cursor.execute("SELECT F_ORDER_NO FROM zxepay_merc_order WHERE F_OUTER_ORDER_NO='1617243983786';")

    # 使用 fetchone() 方法获取一条数据
        data1=cursor.fetchone()
        data = str(data1[0])

        print(data1)
        print('数据库返回值：',data)
        return data

        db.close()



    # 下单查询接口
    @allure.feature('test_module_01')
    @allure.story('test_story_01')
    @allure.severity('critical')
    def test_case_02(self):

        url='http://192.168.1.131:8443/order-service/order/trade/orderquery'

        str={"merchantNo":"000002","merchantOrderNo":"1617248569549","orderId":self.test_01()}
        print(str)

#加密后字符串
        req={"charset":"UTF-8","content":"INtmyC+RvIqq5yTMk/h4SbcuS2pWa8z3ZNzlHMl5opDaJ/LO6S5IR2YCYGfvsKoZNvHZFnS74T/+zhqql7TOCzzpHSkLxzT3EP9+K/02SjQVhLUuFDq8nN6GLx63ak3cIwsR5GTnRp9uIOpsWOs4cczYnYKyeajzXwLFtSJbJY4=","encryptType":"RSA","format":"format","merchantId":"000002","rsaType":"RSA","sign":"ewjqD8R7XKtZnZd/e8WlSC9ILGSVV4vZrqMxSO2i+a7ZdzM07rTOImzOWA9dSv9NlrSYB8m0u4DzXyu6fJ2Vk5IUzIy0AnShuP1t6cBUbgNUYFNyiDlNU5zW8/M3yaKBhaVRDkZZ3hNVVNnKthbkQqlJTtFT7p49j0GmfFFx8NA=","signType":"RSA","timestamp":"1617173069861","version":"1.0"}


        r = requests.post(url,json=req, headers={'Content-Type':'application/json'})

        print('下单查询返回结果:',r.text)

        self.assertEqual(r.status_code,300,"测试成功")
        assert r.status_code==200


if __name__ == '__main__':
    unittest.main()
