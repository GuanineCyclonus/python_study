import threading
import time


def test1(temp):
    temp.append(33)
    print('-----in test1----temp = %s-----' % str(temp))

def test2(temp):
    print('-----in test2----temp = %s-----' % str(temp))

F_num = [11,22]

def main():
    t1 = threading.Thread(target = test1, args=(F_num,))
    t2 = threading.Thread(target = test2, args=(F_num,))

    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)

    print('-----in main----temp = %s-----' % str(F_num))

if __name__ == '__main__':
    main()