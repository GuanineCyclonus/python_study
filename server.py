import server_functions
import multiprocessing


def main():
    server_socket, pool = server_functions.server_init()
    while True:
        print('-----已经开始循环-----')
        new_client_socket, new_client_addr = server_socket.accept()
        with open('./files/socket_list.txt', 'a+') as write_socket:
            write_socket.write(str(new_client_socket))
            write_socket.write('\n')

        print(new_client_addr)
        serve_p = multiprocessing.Process(target=server_functions.disponse_messages,
                                          args=(new_client_socket, new_client_addr))
        serve_p.start()
        # pool.apply_async(server_functions.disponse_massages(new_client_socket))
        # server_functions.disponse_massages(new_client_socket)


if __name__ == '__main__':
    main()
