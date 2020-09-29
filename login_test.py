import socket
import re


# import time

def client_socket_init():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client_socket.connect(('192.168.1.5', 8000))
    client_socket_addr = client_socket.getsockname()

    return client_socket, client_socket_addr


def email_check():
    while True:
        print('请输入你要注册的邮箱😊:')
        e_mail = input()
        success = re.match(r'^(.+)@(.+\.com)$', e_mail)
        if success is None:
            print('邮箱地址无效，请重新输入.')
        else:
            print('邮箱地址创建成功!')
            break

    return e_mail


def password_check():
    while True:
        print('请输入你的密码😊:')
        print('要求:6-16个字符，必须有小写字母和数字(推荐添加特殊符号)')
        password = input()
        success = re.match(r'^.{6,16}$', password)
        if success is None:
            print('密码格式错误，请重新设置密码.')
        else:
            success = success.group()
            word_in_alphabet = 0
            for i in success:
                if i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    word_in_alphabet = 1
                    break

            if word_in_alphabet != 1:
                print('密码格式错误，请重新设置密码.')

            else:
                print('密码设置成功!')
                break

    return password


def set_new_user(e_mail, password):
    with open('files/developer.txt', 'r') as user_list:
        user_list = user_list.readlines()
        last_user = user_list[-1]
        last_user = last_user.split(' ')
        last_user_account = last_user[0]
        new_user_account = int(last_user_account) + 1
        new_user = str(new_user_account) + ' ' + password + ' ' + e_mail + '\n'

        return new_user_account, new_user


def register(client_socket):
    while True:
        print('是否现在注册?(y/n)')
        choose = input()
        # print(choose)
        if choose == 'y':
            # print(choose)
            e_mail = email_check()
            password = password_check()

            new_user = set_new_user(e_mail, password)

            client_socket.send((new_user[1] + '%usercheck').encode('utf-8'))

            print('good! 你的账号为%d.' % new_user[0])
            print('快去登录吧!')

            return str(new_user[0])

        elif choose == 'n':
            # print(choose)
            return 'noneed'

        else:
            print('无此选项，请再输一遍.')


def Login(client_socket, delivery_queue):
    print("You 're welcome!!!")
    # time.sleep(1)

    while True:
        print("请输入你的账号😀(若没有，请输入r来注册):")
        account = '100000'
        # account = input()

        if account == 'r':
            account = register(client_socket)
            if account == 'noneed':
                # print('noneed!')
                continue

        print("请输入你的密码😀:")
        password = '070208'
        # password = input()

        user = account + ' ' + password + ' %login'
        client_socket.send(user.encode('utf-8'))
        data = client_socket.recv(1024)
        data = data.decode('utf-8')
        data_list = data.split('&')
        main_data = data_list[0]
        data_suffix = data_list[-1]
        if data_suffix == 'N':
            print(main_data)
            continue
        elif data_suffix == 'Y':
            print(main_data)
            delivery_queue.put(data_suffix)
            return
