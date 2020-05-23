import pytest
import requests
import json
import re
from . import get_ip
# from . import const

# 获取本地IP
ipip_net_url = 'http://myip.ipip.net'
ip_info = requests.get(ipip_net_url).text
pattern = re.compile(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b")

# httpbin
LOCAL_IP = get_ip.LOCAL_IP
# LOCAL_IP = re.findall(pattern, ip_info)[0]  # 查找IP正则表达式
BASE_URL = "http://httpbin.org/"
IP_URL = "/ip"
POST_TEST_URL = "/post"


class Test_httpbin():
    def test_get_ip(self):
        url = BASE_URL + IP_URL
        print(url)
        r = requests.get(url)
        print(r.headers)
        response_data = json.loads(r.text)
        print(response_data)
        assert 200 == r.status_code
        assert LOCAL_IP == response_data["origin"]

    def test_post_method(self):
        url = BASE_URL + POST_TEST_URL
        post_data = {"name": "test", "pwd": "123456"}
        r = requests.post(url, data=post_data)
        print(r.headers)
        print(r.text)
        response_data = r.json()
        assert 200 == r.status_code
        assert post_data["name"] == response_data["form"]["name"]
        assert post_data["pwd"] == response_data["form"]["pwd"]
