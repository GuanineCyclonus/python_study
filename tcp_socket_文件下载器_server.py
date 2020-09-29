import socket
def send_file_2_client(new_client_socket, client_addr):
    file_content = None
    # 5. 接收客户发送过来的文件名
    file_name = new_client_socket.recv(1024).decode('utf-8')
    print('客户(%s)发送过来的文件名是:%s' % (str(client_addr), file_name))
    print('请回复:')
    try:
        f = open(file_name,'rb')
        file_content = f.read()
        f.close()
    except Exception as ret:
        print('没有要下载的文件(%s)' % file_name)

    if file_content:
        new_client_socket.send(file_content)


def main():
    # 1.买个手机（创建套接字）
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 2.插上电话卡（绑定本地地址）
    tcp_server_socket.bind(('' , 12345))

    # 3.将手机设置为正常的响铃模式（让主动套接字变为被动套接字）
    tcp_server_socket.listen(128)

    while True:
        #print('-----1-----')
        print('等待一个新的客户端的到来...')
        # 4.等待电话到来（等待客户端的链接）
        new_client_socket, client_addr = tcp_server_socket.accept()
        #print('-----2-----')
        print('一个新的客户端已到来:用户地址 %s' % (str(client_addr)))

        send_file_2_client(new_client_socket, client_addr)
        # 7. 挂断（关闭套接字）
        new_client_socket.close()
        print('已经完成服务.')
    tcp_server_socket.close()

if __name__ == '__main__':
    main()