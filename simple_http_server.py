import socket

s=socket.socket()
host=socket.gethostname()
print(host)
host='139.129.208.83'
port=6888
s.bind((host,port))
# s.settimeout(10000)
s.listen(5)

while True:
    conn,addr=s.accept()
    print(addr)
    data=conn.recv(2048)
    # parse the first line
    first_line = str(data,encoding='utf-8').split('\n')[0]

    # get url
    url = first_line.split(' ')[1]
    print(url)
    http_pos = url.find("://") # find pos of ://
    if (http_pos==-1):
        temp = url
    else:
        temp = url[(http_pos+3):] # get the rest of url

    port_pos = temp.find(":") # find the port pos (if any)

    # find end of web server
    webserver_pos = temp.find("/")
    if webserver_pos == -1:
        webserver_pos = len(temp)

    webserver = ""
    port = -1
    if (port_pos==-1 or webserver_pos < port_pos):

        # default port
        port = 80
        webserver = temp[:webserver_pos]

    else: # specific port
        port = int((temp[(port_pos+1):])[:webserver_pos-port_pos-1])
        webserver = temp[:port_pos]
        # c.send(b'hello')
        conn.close()
    print(webserver,port)


    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.settimeout(config['CONNECTION_TIMEOUT'])
    s1.connect((webserver, port))
    print(data)
    s1.sendall(data)
    while 1:
    # receive data from web server
        data = s1.recv(4096)

        if len(data) > 0:
            conn.send(data) # send to browser/client
        else:
            break
    s1.close()
    conn.close()
