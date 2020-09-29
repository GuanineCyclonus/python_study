import threading
import multiprocessing

from login_test import *
from client_functions_test import *


def main():

    client_socket, client_socket_addr = client_socket_init()

    delivery_queue = multiprocessing.Manager().Queue()
    exit_queue = multiprocessing.Manager().Queue()

    Login(client_socket, delivery_queue)

    return_thread = threading.Thread(target=return_messages, args=(client_socket, delivery_queue, exit_queue))
    receive_thread = threading.Thread(target=receive_data, args=(client_socket, delivery_queue,
                                                                 exit_queue, client_socket_addr, client_socket))

    return_thread.start()
    receive_thread.start()
    

if __name__ == '__main__':
    main()
