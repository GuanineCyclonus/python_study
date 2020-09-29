import socket
import os
import re


def service_client(new_client, request):
    # request = new_client.recv(1024).decode('utf-8')
    # print(request)
    request_lines = request.splitlines()
    print(request_lines)

    ret = re.match(r'[^/]+(/[^ ]*)', request_lines[0])

    if ret:
        file_name = ret.group(1)
        if file_name == '/':
            file_name = '/index.html'


    try:
        f = open('/Users/cx/Desktop/moban4554' + file_name, 'rb')
    except:
        repsonse = 'HTTP/1.1 404 NOT FOUND\r\n'
        repsonse += '\r\n'
        repsonse += '<h1>404 NOT FOUND</h1>'
        new_client.send(repsonse.encode('utf-8'))
    else:
        print('*'*50, file_name)
        html_content = f.read()
        f.close()

        response_body = html_content

        response_header = 'HTTP/1.1 200 OK\r\n'
        response_header += 'Content-Length:%d\r\n' % len(response_body)
        response_header += '\r\n'

        response = response_header.encode('utf-8') + response_body

        # response += '<h1>hello world!!</h1>\r\n'
        # response += "<h2>YOU'RE WELCOME!!</h2>\r\n"
        # response += "<h3>the NAME of the Website's Creator:程乾</h3>\r\n"

        new_client.send(response)

def main():
    # 1.买个手机（创建套接字）
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 2.插上电话卡（绑定本地地址）
    tcp_server_socket.bind(('' , 12345))

    # 3.将手机设置为正常的响铃模式（让主动套接字变为被动套接字）
    tcp_server_socket.listen(128)
    tcp_server_socket.setblocking(False)  # 将套接字改为非堵塞

    client_socket_list = list()
    while True:
        try:
            new_client, client_addr = tcp_server_socket.accept()
        except Exception as ret:
            pass
        else:
            new_client.setblocking(False)
            client_socket_list.append(new_client)
            for client_socket in client_socket_list:
                try:
                    recv_data = client_socket.recv(1024).decode('utf-8')
                except Exception as ret:
                    pass
                else:
                    if recv_data:
                        service_client(client_socket, recv_data)
                    else:
                        client_socket.close()
                        client_socket_list.remove(client_socket)

if __name__ == '__main__':
    try:
        os.chdir('/Users/cx/Desktop')
        main()
    except:
        print('服务器连接错误!!!')
