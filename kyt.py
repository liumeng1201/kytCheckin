from urllib import request, parse
import re
import time

push_key = ""
identity_frontend_cookie = ""

if(identity_frontend_cookie == ""):
   identity_frontend_cookie = input("identityfrontendcookie:")
   push_key = input("push:")

login = 'https://www.ablesci.com/site/login?email=597631025@qq.com&password=liumeng1201&remember=on'
checkin = 'https://www.ablesci.com/user/sign'
push = 'https://sc.ftqq.com/' + push_key + '.send?text=need_update_kyt_identity_frontend_cookie'

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


def day_diff():
    now = time.strftime("%Y-%m-%d", time.localtime())
    day1 = time.strptime(str('2020-10-19'), '%Y-%m-%d')
    day2 = time.strptime(str(now), '%Y-%m-%d')
    diff = (int(time.mktime(day2)) - int(time.mktime(day1))) / (24 * 60 * 60)
    day = abs(int(diff))
    if day > 25:
        print('need to update identity_frontend_cookie')
        request.urlopen(push)


reqlogin = request.Request(url=login, headers=headers, method='GET')
cookies = request.urlopen(reqlogin).getheader('Set-Cookie')
security_session_verify_cookie = re.search('security_session_verify=[^;]*;', cookies).group()
advanced_frontend_cookie = re.search('advanced-frontend=[^;]*;', cookies).group()
_csrf_cookie = re.search('_csrf=[^;]*;', cookies).group()
cookies = security_session_verify_cookie + advanced_frontend_cookie + _csrf_cookie + identity_frontend_cookie
print()
print(cookies)
req = request.Request(url=checkin, headers=headers, method='GET')
req.add_header('Cookie', cookies)
response = request.urlopen(req)
if response.status == 200:
    print("脚本执行成功")
else:
    print("脚本执行失败")
day_diff()