import socket
import multiprocessing


def server_init():
    """初始化服务器套接字设置"""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('', 8000))
    server_socket.listen(128)
    serve_more_client_pool = multiprocessing.Pool()
    return server_socket, serve_more_client_pool


def write_new_user(new_user):
    with open('files/developer.txt', 'a') as write_user:
        write_user.write(new_user)


def read_user_list(login_message):
    with open('./files/developer.txt') as users:
        login_message = login_message.split(' ')
        login_message = login_message[0] + login_message[1]
        user_message = users.readlines()
        success = False

        return login_message, user_message, success


def check_login_users(new_client_socket, login_message, new_client_addr):
    login_message, user_message, success = read_user_list(login_message)
    for i in range(len(user_message)):
        # print(user_message[i])
        check_user = user_message[i]
        check_user = check_user.split(' ')
        # print(check_user)

        if login_message == check_user[0] + check_user[1]:
            new_client_socket.sendto('欢迎来到TICS.&Y'.encode('utf-8'), new_client_addr)
            # new_client_socket.send('欢迎!!🍺🍺🍺&Y'.encode('utf-8'))
            success = True
            with open('./files/developer.txt') as user_form:
                user_list = user_form.readlines()

            for user in user_list:
                # print(user)
                # print(login_message[:6])
                if login_message[:6] in user:
                    # print('----pass----')
                    return user
            # break

    if not success:
        new_client_socket.send('账号或密码错误。请重新输入‼️&N'.encode('utf-8'))


def disponse_show(command, new_client_addr, new_client_socket):
    new_client_addr = new_client_addr[0]
    command_list = command.split(' ')
    minor_command = command_list[1]
    # print(minor_command)
    if minor_command == 'friends':
        data = '你还没有好友哦😯&Y'
        try:
            open('./files/' + new_client_addr + '.txt')
        except FileNotFoundError:
            f = open('./files/' + new_client_addr + '.txt', 'w')
            f.close()
            new_client_socket.send(data.encode('utf-8'))

        else:
            with open('./files/' + new_client_addr + '.txt', 'r') as friendlist:
                friends = friendlist.read()
                # print(friends)
                if not friends == '':
                    # print('----have friends----')
                    new_client_socket.send((friends+'&Y').encode('utf-8'))
                elif friends == '':
                    # print('----have no friend----')
                    new_client_socket.send(data.encode('utf-8'))
    else:
        data = '功能尚未开放，尽请期待🙂!&Y'
        new_client_socket.send(data.encode('utf-8'))


def disponse_goto(command, new_client_addr, new_client_socket):
    pass
    command_list = command.split(' ')
    user_name = command_list[-1]
    with open('./files/' + new_client_addr[0] + '.txt', 'r') as friend_list:
        friend_list = friend_list.readlines()
        for friend in friend_list:
            # print(friend)
            if user_name in friend:
                friend_addr = friend.split(' ')
                friend_account = str(friend_addr[1])
                friend_addr = friend_addr[0]
                new_client_socket.send((friend_addr + '&goto').encode('utf-8'))
                return friend_account

            else:
                new_client_socket.sendto('----test----'.encode('utf-8'), ('192.168.1.4', 13000))
                new_client_socket.send('您没有该好友!&Y'.encode('utf-8'))
                return None


def disponse_commands(command, new_client_addr, new_client_socket):
    command_list = command.split(' ')
    main_command = command_list[0]
    if main_command == 'show':
        disponse_show(command, new_client_addr, new_client_socket)
    elif main_command == 'goto':
        account = disponse_goto(command, new_client_addr, new_client_socket)
        print(account)
        if account is None:
            return
        with open('./files/online_users.txt') as users:
            # new_client_socket.send('----test----&N'.encode('utf-8'))
            user_list = users.readlines()
            for i in user_list:
                if account in i:
                    print('----friends----')
                    break

                # new_client_socket.send('好友未在线.&N'.encode('utf-8'))


def del_offline_users(new_client_addr):
    with open('./files/online_users.txt') as online_user_list:
        online_user_list = online_user_list.readlines()

    with open('./files/online_users.txt', 'w') as del_offline_user:
        for i in online_user_list:
            # print('\r' + i, end='')
            # print(str(new_client_addr[1]))
            # print(not str(new_client_addr[1]) in online_user_list)
            # print(i)
            # print(str(new_client_addr[1]) in online_user_list[0])
            if not str(new_client_addr[-1]) in i:
                del_offline_user.write(i)


def disponse_chat(data, sender_account, receiver_account, new_client_socket):
    with open('./files/data_transmission/' + sender_account + ' and ' + receiver_account + '.txt', 'a+') as save_data:
        save_data.write(data)
        save_data.write('\n')
        with open('./files/online_users.txt') as users:
            user_list = users.readlines()
            recv_addr = None
            for i in user_list:
                # print(i)
                if sender_account in i:
                    # print('----sender in----')
                    user_addr = i.split(' ')
                    user_addr = user_addr[0] + user_addr[1]
                if receiver_account in i:
                    print(i)
                    # print('----receiver in----')
                    recv_addr = i.split(' ')
                    print(recv_addr)
                    # recv_addr = recv_addr[0] + recv_addr[1]

            if recv_addr is None:
                # print('----None----')
                return

            else:
                return recv_addr[0], int(recv_addr[1])

                # addr = (recv_addr[0], int(recv_addr[1]))
                # addr = (recv_addr[0], int(recv_addr[1])
                # data = (user_addr + ':' + data + '&chat')
                # (user_addr + ':' + data + '&chat')
                # print(addr)
                # print(data)
                # new_client_socket.sendto(data.encode('utf-8'), addr)


def disponse_messages(new_client_socket, new_client_addr):

    while True:
        login_message = new_client_socket.recv(1024)
        if not login_message:
            # new_client_socket.shutdown(2)
            del_offline_users(new_client_addr)
            new_client_socket.close()
            return
        login_message = login_message.decode('utf-8')
        # print(login_message)

        message = login_message.split('%')
        user_message = message[0]
        # print(user_message)
        suffix = message[-1]
        # print(suffix)

        if suffix == 'usercheck':
            write_new_user(user_message)
        elif suffix == 'login':
            online_user = check_login_users(new_client_socket, user_message, new_client_addr)

            if online_user is not None:
                with open('./files/online_users.txt', 'a+') as write_user:
                    for i in range(len(new_client_addr)):
                        write_user.write(str(new_client_addr[i]))
                        write_user.write(' ')

                    write_user.write(online_user)
                    # write_user.write('\n')

        elif suffix == 'cmd':
            disponse_commands(user_message, new_client_addr, new_client_socket)
        elif suffix == 'exit':
            new_client_socket.send('exit&exit'.encode('utf-8'))
            del_offline_users(new_client_addr)

        # elif suffix == 'chat':
        # print(user_message)
        # udp_addr, udp_port = disponse_chat(user_message, new_client_addr[0], '100001', new_client_socket)
        # new_client_socket.send((udp_addr + ' ' + str(udp_port) + '&create_new_socket').encode('utf-8'))
