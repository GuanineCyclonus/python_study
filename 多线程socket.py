import socket
import threading

def send_msg(udp_socket):

    print('请输入对方的ip:')
    op_ip = (input())
    print('请输入对方的port:')
    op_port = int(input())

    while True:
        print('请输入要发送的messages:  （输入exit以关闭）')
        send_to = input()
        Return = '(系统):对方已停止向你发送数据'
        udp_socket.sendto(send_to.encode('utf-8'), (op_ip, op_port))

def recv_msg(udp_socket):
    while True:
        recv_from = udp_socket.recvfrom(1024)
        recv_msg = recv_from[0]
        recv_addr = recv_from[1]
        print('%s:%s' % (str(recv_addr), recv_msg.decode('utf-8')))




def main():
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    localaddr = (('', 12345))
    udp_socket.bind(localaddr)

    t1 = threading.Thread(target=send_msg, args=(udp_socket,))
    t2 = threading.Thread(target=recv_msg, args=(udp_socket,))

    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
