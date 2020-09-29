# import time
import re


def show_help():
    with open('./files/command.txt') as help_file:
        help_file_list = help_file.readlines()
        return help_file_list
        # for helps in help_file_list:
        # print(helps)


def disponse_commands(command, delivery_queue, exit_queue):
    # print(command)
    suffix = ''
    if command == '':
        delivery_queue.put('Y')
        return None
    elif command == 'help':
        help_file_list = show_help()
        for helps in help_file_list:
            print(helps, end='')
        delivery_queue.put('Y')
        return None
    elif command == 'exit':
        # print('----exit----')
        exit_queue.put('exit')
        # print('----exiting----')
        return 'exit'

    command_part = command.split(' ')
    main_command = command_part[0]

    try:
        minor_command = command_part[1]
    except IndexError:
        help_file_list = show_help()
        for helps in help_file_list:
            if main_command in helps:
                print(helps, end='')

        delivery_queue.put('Y')
        return None

    try:
        suffix = command_part[2]
        # print('----have suffix')
    except IndexError:
        # print('----have no suffix')
        if minor_command == 'friends':
            suffix = ' -on'
            # print(suffix)
        elif minor_command in ['friend', 'groups', 'group']:
            suffix = ''
            # print(suffix)
        else:
            pass
            # print('---error---')

    command = main_command + ' ' + minor_command + suffix

    main_pattern = re.compile(r'help|show|goto|exit')
    minor_pattern = re.compile(r'friend|friends|group|groups')

    main_success = re.match(main_pattern, main_command)
    minor_success = re.match(minor_pattern, minor_command)
    # print(main_success is None)

    if main_success is None:
        delivery_queue.put('Y')
        return False
    elif minor_success is None:
        if main_command == 'goto':
            return command + '%cmd'
        else:
            delivery_queue.put('Y')
            return False
    else:
        # print(command)
        return command + '%cmd'


def return_messages(client_socket, delivery_queue, exit_queue):
    help_show = True
    print('输入help获得指令帮助')
    while True:
        if delivery_queue.get() == 'Y':
            if not help_show:
                # print(help_show)
                help_show = True
                help_file_list = show_help()
                for helps in help_file_list:
                    print(helps, end='')

            # time_now = time.ctime()
            command = 'exit'
            # command = input(time_now + ' ~￥>>>')
            command = disponse_commands(command, delivery_queue, exit_queue)
            # print(command)

            if command is None:
                continue
            elif command is False:
                print('格式错误, 请重新输入')
                continue
            elif command == 'exit':
                client_socket.send('exit%exit'.encode('utf-8'))
                # client_socket.shutdown(2)
                # client_socket.close()
                return
            else:
                client_socket.send(command.encode('utf-8'))


def open_new_window(new_client_addr, new_client_socket):
    # for i in range(5):
    # print()

    with open('./files/connect_logfile.txt', 'w') as init:
        init.write('\n')
        init.write('-' * 15)
        init.write('\n')
    # print('-' * 15)
    while True:
        with open('./files/connect_logfile.txt', 'r') as log_file:
            log_file = log_file.read()
            print('\r' + log_file, end='')
        data = input()
        with open('./files/connect_logfile.txt', 'a+') as log_file:
            log_file.write(' ' * 15 + ('%s:%s' % (data, new_client_addr)))
            log_file.write('\n')
            with open('./files/connect_logfile.txt', 'r') as log_data:
                log_data = log_data.read()
            print(log_data)
            new_client_socket.send((log_data + '%chat').encode('utf-8'))


def receive_data(client_socket, delivery_queue, exit_queue, new_client_addr, new_client_socket):
    while True:
        # print(exit_queue.empty())

        if not exit_queue.empty():
            exit_data = exit_queue.get()
            # print(exit_data)
            # print('----exit----')
            if exit_data == 'exit':
                # print('----exit----')
                client_socket.close()
                # print('----closed----')
                return

        # print('----receiving----')
        data = client_socket.recv(1024).decode('utf-8')
        # print('----已收到数据----')
        data_list = data.split('&')
        main_data = data_list[0]
        data_suffix = data_list[-1]

        if data_suffix == 'N':
            print(main_data)
        elif data_suffix == 'Y':
            print(main_data)
            delivery_queue.put('Y')
        elif data_suffix == 'goto':
            open_new_window(new_client_addr, new_client_socket)
        elif data_suffix == 'exit':
            continue
