import random
from django.shortcuts import render, HttpResponse, redirect
import requests as req
import json
import time
import simplejson
Cookies = {
    "Openid": "o_DYGt_gljnsTlD-xTz3KO6iJpJ4"
    # "Openid": "o_DYGt9MugrzUkb4Hc-tMuPyb6gc"
}

# Create your views here.
def index(request):
    return HttpResponse("欢迎使用")


def user_list(requests):
    return render(requests, "user_list.html")


def PostInfo(requests):
    return render(requests, 'xxx.html', {'index': 'value'})


# PreInfo/ 显示填写抢场信息页面
def PreInfo(requests):
    return render(requests, 'PreInfo.html')



# getPreInfo/ 接受显示输入的场地信息
def getPreInfo(requests):
    cookies = simplejson.loads(requests.GET.get('cookies'))
    global Cookies
    Cookies = cookies
    timeout = float(requests.GET.get('timeout'))
    if timeout < 2:
        timeout = 2
    print(requests.GET)
    urls = [
        'http://gzagwx.wxlgzh.com/Field/OrderField?checkdata=%5B%7B%22FieldNo%22%3A%22' + requests.GET.get(
            'FieldNum').__str__()
        + '%22%2C%22FieldTypeNo%22%3A%2211%22%2C%22FieldName%22%3A%22%E7%BE%BD%E6%AF%9B%E7%90%83' + requests.GET.get(
            'FieldNo').__str__()
        + '%E5%8F%B7%E5%9C%BA%22%2C%22BeginTime%22%3A%22' + requests.GET.get('StartTime').__str__() + '%3A00'
        + '%22%2C%22Endtime%22%3A%22' + requests.GET.get('EndTime').__str__() + '%3A00'
        + '%22%2C%22Price%22%3A%22' + requests.GET.get('Price').__str__()
        + '%22%7D%5D&' + 'dateadd=3&VenueNo=07'
    ]
    # 发送十/五分钟的请求
    duration = float(requests.GET.get('duration'))
    endTime = time.ctime(time.time()+duration*60)
    while time.ctime(time.time()) < endTime:
        try:
            response1 = req.get(urls[0], cookies=cookies, verify=False, timeout=timeout)
        except Exception:
            print(Exception)
            continue
        print("发送成功")
    return render(requests, 'end.html')

# start/
def result(requests):
    urls = [
        'http://gzagwx.wxlgzh.com/Field/GetFieldOrder?PageNum=1&PageSize=6&Condition=&_=16797606390' + random.randint(
            10, 99).__str__()
    ]
    response = req.get(urls[0], cookies=Cookies, verify=False, timeout=30)
    data = response.text
    output = json.loads(data)
    print(output)
    return render(requests, 'table.html', {'output': output,'cookies':Cookies})

#
#  方法区
#
