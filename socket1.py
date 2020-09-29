import socket

def main():
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    localaddr = (('',12345))
    udp_socket.bind(localaddr)

    while True:
        print('请输入要发送的messages:  （输入exit以关闭）')
        send_to = input()
        Return = '对方已停止向你发送数据'
        if send_to == 'exit':
            send_to = Return
            udp_socket.sendto(send_to.encode('utf-8'), ('192.168.1.5', 4488))
            break


        udp_socket.sendto(send_to.encode('utf-8'),('192.168.1.5', 4488))




    udp_socket.close()

if __name__ == '__main__':
    main()
