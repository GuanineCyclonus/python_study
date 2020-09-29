import socket
import os
import re
import threading

def service_client(new_client):
    request = new_client.recv(1024).decode('utf-8')
    # print(request)

    request_lines = request.splitlines()
    print(request_lines)

    ret = re.match(r'[^/]+(/[^ ]*)', request_lines[0])

    if ret:
        file_name = ret.group(1)
        if file_name == '/':
            file_name = '/index.html'
    try:
        f = open('/Users/cx/Desktop/moban4583' + file_name, 'rb')
    except:
        repsonse = 'HTTP/1.1 404 NOT FOUND\r\n'
        repsonse += '\r\n'
        repsonse += '<h1>404 NOT FOUND</h1>'
        new_client.send(repsonse.encode('utf-8'))

    else:
        print('*'*50, file_name)

        response = 'HTTP/1.1 200 OK\r\n'
        response += '\r\n'
        # response += '<h1>hello world!!</h1>\r\n'
        # response += "<h2>YOU'RE WELCOME!!</h2>\r\n"
        # response += "<h3>the NAME of the Website's Creator:程乾</h3>\r\n"


        html_content = f.read()
        f.close()



        new_client.send(response.encode('utf-8'))
        new_client.send(html_content)

        new_client.close()

def main():
    # 1.买个手机（创建套接字）
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 2.插上电话卡（绑定本地地址）
    tcp_server_socket.bind(('' , 12345))

    # 3.将手机设置为正常的响铃模式（让主动套接字变为被动套接字）
    tcp_server_socket.listen(128)
    while True:
        new_client, client_addr = tcp_server_socket.accept()
        p = threading.Thread(target=service_client, args=(new_client,))
        p.start()

    tcp_server_socket.close()

if __name__ == '__main__':
    try:
        os.chdir('/Users/cx/Desktop')
        main()
    except:
        print('服务器连接错误!!!')
