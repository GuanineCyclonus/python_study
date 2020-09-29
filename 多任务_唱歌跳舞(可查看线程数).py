import time
import threading

def sing():
    '''正在唱歌'''
    for i in range (5):
        print('awawawawawa---%d' % i)
        time.sleep(1)

def dance():
    '''正在跳舞'''
    for i in range (5):
        print('哒哒哒哒哒哒---%d' % i)
        time.sleep(1)

def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)

    t1.start()
    t2.start()
    while True:
        print(threading.enumerate())
        time.sleep(1)


if __name__ == '__main__':
    main()