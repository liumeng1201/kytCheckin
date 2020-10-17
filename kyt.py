from urllib import request, parse

cookie = ""
push_key = ""

if(cookie == ""):
   cookie = input("cookie:")
   push_key = input("push:")


url = 'https://www.ablesci.com/user/sign'
push = 'https://sc.ftqq.com/' + push_key + '.send?text=aihao_checkin_error'

headers = {
    'Host': 'www.ablesci.com',
    'Connection': 'keep-alive',
    'sec-ch-ua': '"\\Not;A\"Brand";v="99", "Google Chrome";v="85", "Chromium";v="85"',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'DNT': '1',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
}


req = request.Request(url=url, headers=headers, method='GET')
req.add_header('Cookie', cookie)
response = request.urlopen(req)
if response.status == 200:
    print("打卡成功")
else:
    request.urlopen(push)
    print("打卡失败")