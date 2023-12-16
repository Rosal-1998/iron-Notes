# 导入 requests 包
# 文档：https://requests.readthedocs.io/en/latest/
import requests
import json


def GET(number):
    result = requests.get(
        'https://apis.tianapi.com/kuaidi/index?key=0e2c14f1c9ab22c92478155dfdeccb21&number=' + number)
    # 解析python request之后的返回结果的json格式
    resultJson = result.json()
    # print('---最高温度---', resultJson.get('result').get('highest'))
    return resultJson


def POST(number):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    result = requests.post('https://apis.tianapi.com/kuaidi/index',
                           data={
                               'key': '0e2c14f1c9ab22c92478155dfdeccb21',
                               'number': number,
                           }, headers=headers)
    resultJson = result.json()
    # print('---最高温度---', resultJson.get('result').get('highest'))
    return resultJson


def QueryWeatherDetail(choice, number):
    if choice == '1':
        print('----已选择GET协议！----')
        x = GET(number)
    elif choice == '2':
        print('----已选择POST协议！----')
        x = POST(number)
    else:
        print('----ERR:选择错误----')
    
    print('--------------查询结果：---------------')
    print(x)
    # print('城市：',x.get('result').get('area'))
    # print('天气：',x.get('result').get('weather'))
    # print('实时气温：',x.get('result').get('real'))
    # print('最高气温：',x.get('result').get('highest'))
    # print('最低气温：',x.get('result').get('lowest'))
    # print('天气小助手：',x.get('result').get('tips'))
    print('--------------查询结果：---------------')



print('请选择你想要使用的协议：1.GET 2.POST')
choice = input('你的协议选择：')
number = input('请输入需要查询快递的单号：')
QueryWeatherDetail(choice, number)