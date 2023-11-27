# 导入 requests 包
import requests

# 发送请求
x = requests.get('https://apis.tianapi.com/tianqi/index?key=0e2c14f1c9ab22c92478155dfdeccb21&city=101020100&type=1')

# 返回网页内容
print(x.text)