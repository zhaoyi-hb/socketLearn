import requests

proxy='139.129.208.83:6888'
# proxy="139.159.1.1:41815"
# proxy='39.137.95.75:80'

#如果代理需要验证，只需要在前面加上用户名密码，如下所示

# proxy='username:password@124.243.226.18:8888'
proxies={
    'http':'http://'+proxy,
    'https':'https://'+proxy,
}
try:
    url='http://httpbin.org/get'
    # url='https://baidu.com'
    response=requests.get(url,proxies=proxies)
    response.encoding="utf-8"
    print(response.text)
    print(response.encoding)
    print(response.headers)
except requests.exceptions.ConnectionError as e:
    print("Error",e.args)
