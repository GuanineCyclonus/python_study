import socket

def main():
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


    localaddr = ('',11111)
    udp_socket.bind(localaddr)

    while True:
        recv_from = udp_socket.recvfrom(1024)
        recv_msg = recv_from[0]
        recv_addr = recv_from[1]
        print('%s:%s' % (str(recv_addr),recv_msg.decode('gbk')))




if __name__ == '__main__':
    main()