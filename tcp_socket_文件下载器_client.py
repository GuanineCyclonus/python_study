import socket


def main():
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print('请输入服务器的ip:')
    server_ip = input()
    print('请输入对方的port:')
    server_port = int(input())
    server_addr =(server_ip,server_port)
    tcp_socket.connect(server_addr)
    print('请输入要下载的文件名:')
    download_file_name = input()

    tcp_socket.send(download_file_name.encode('utf-8'))

    recv_file = tcp_socket.recv(1024)

    if recv_file:
        with open('[新]' + download_file_name, 'wb') as f:
            f.write(recv_file)

    tcp_socket.close()

if __name__ == '__main__':
    main()