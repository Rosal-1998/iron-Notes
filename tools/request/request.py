# 导入 requests 包
# 文档：https://requests.readthedocs.io/en/latest/
import requests
import json

def GET(city):
    result = requests.get(
        'https://apis.tianapi.com/tianqi/index?key=0e2c14f1c9ab22c92478155dfdeccb21&city=' + city + '&type=1')
    print('---------------')
    print(result)
    print('---------------')
    print(result.text)
    # 解析python request之后的返回结果的json格式
    resultJson = result.json()
    
    print('---最高温度---',resultJson.get('result').get('highest'))
    return result


# def POST(city):
#     headers = {
#     'Content-Type': 'application/x-www-form-urlencoded'
# }
#     result = requests.post('https://httpbin.org/post',
#                            data={
#                                'key': '0e2c14f1c9ab22c92478155dfdeccb21',
#                                'city': '南昌',
#                                'type': 1
# 							   }, headers=headers)
#     print(result.json())
#     result = result.read()
#     data = result.decode('utf-8')
#     dict_data = json.loads(data)
#     print(dict_data)
#     return result


choice = input('请选择你想要使用的协议：1.GET 2.POST')
# choice = '2'
if choice == '1':
    print('----已选择GET协议！----')
    city = input("请输入需要查询的天气: ")
    GET(city)
elif choice == '2':
    print('----已选择POST协议！----')
    city = input("请输入需要查询的天气: ")
else:
    print('----ERR:选择错误----')
