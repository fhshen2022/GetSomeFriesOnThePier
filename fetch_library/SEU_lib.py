import requests
import json

url = [
       'http://10.9.4.215/ClientWeb/pro/ajax/reserve.aspx?dialogid=&dev_id=107986279&lab_id=100417765&kind_id=108009515&room_id=&type=dev&prop=&test_id=&term=&number=&classkind=&test_name=&min_user=2&max_user=6&mb_list=%24172883%2C234116&start=2021-12-19+08%3A30&end=2021-12-19+12%3A00&start_time=830&end_time=1200&up_file=&memo=&memo=&act=set_resv&_=1639751053249'
        ]

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
               'Referer': 'http://10.9.4.215/ClientWeb/xcus/ic2/Default.aspx'}

cookies={'ASP.NET_SessionId':'5u525d2q4brmfxjkc5d4hwip'}


for i in range(100000):
    for j in range(len(url)):
        res = requests.get(url[j], headers, cookies=cookies)
        print(json.loads(res.text)['msg'])
