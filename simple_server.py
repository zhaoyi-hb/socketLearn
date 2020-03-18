import socket

s=socket.socket()
host=socket.gethostname()
print(host)
# host='139.129.208.83'
port=6888
s.bind((host,port))
# s.settimeout(10000)
s.listen(5)

while True:
    conn,addr=s.accept()
    print(addr)
    data=conn.recv(2048)
    print(str(data,encoding='utf-8'))
    # parse the first line
    conn.send(bytes('我是服务端',encoding='utf-8'))
    conn.close()
