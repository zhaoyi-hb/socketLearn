import socket               # 导入 socket 模块

s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 6888                # 设置端口号

s.connect((host, port))
s.send(b'ni hao ya')
s.send(bytes('我是客户端',encoding='utf-8'))
print(s.recv(1024))
s.close()
