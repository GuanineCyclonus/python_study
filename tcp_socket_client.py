import socket
def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    localaddr = ('',7777)
    tcp_socket.bind(localaddr)

    print('请输入需要链接服务器的ip:')
    server_ip = input()
    print('请输入需要链接服务器的port:')
    server_port = int(input())
    server_addr = (server_ip, server_port)
    tcp_socket.connect(server_addr)

    while True:
        print('请输入要发送的message:(输入exit以终止)')
        send_msg = input()
        if send_msg == 'exit':
            tcp_socket.send('0'.encode('gbk'))
            break
        else:
            tcp_socket.send(send_msg.encode('gbk'))


    tcp_socket.close()

if __name__ == '__main__':
    main()

