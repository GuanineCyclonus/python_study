import threading
import time

R_num = 100
def test1():
    global R_num
    R_num += 1
    print('-----in test1----R_num = %d-----' % R_num)

def test2():
    print('-----in test2----R_num = %d-----' % R_num)

def main():
    t1 = threading.Thread(target = test1)
    t2 = threading.Thread(target = test2)

    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)

    print('-----in main----R_num = %d-----' % R_num)

if __name__ == '__main__':
    main()