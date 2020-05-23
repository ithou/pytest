import requests
import re

ipip_net_url = 'http://myip.ipip.net'
res = requests.get(ipip_net_url).text

pattern = re.compile(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b")
LOCAL_IP = re.findall(pattern, res)[0]