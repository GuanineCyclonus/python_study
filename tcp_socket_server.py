import socket

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

        while True:
            # 5. 接收客户发送过来的请求
            new_client_socket.send('请输入恁要办理的服务:'.encode('utf-8'))
            recv_msg = new_client_socket.recv(1024)
            print('客户发送过来的请求是:%s' % recv_msg.decode('gbk'))
            print('请回复:')
            send_msg = input()
            # 6.1 应答客户端
            new_client_socket.send(send_msg.encode('utf-8'))
            # 6.2 询问对方是否还有请求

            new_client_socket.send('请问您是否还有别的请求?如没有请断开连接'.encode('utf-8'))
            print('已向对方发送再次服务请求')
            sd_recv_msg = new_client_socket.recv(1024)
            if not str(sd_recv_msg.decode('gbk')) :
                break
        # 7. 挂断（关闭套接字）
        new_client_socket.close()
        print('已经完成服务.')
    tcp_server_socket.close()

if __name__ == '__main__':
    try:
        main()
    except:
        print('服务器连接错误!!!')