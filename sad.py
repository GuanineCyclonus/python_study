import threading
import time
e = 0
d = 0
def Time1():
    i = 1
    while e <= 19:
        t =  i * (i+1)
        i = i+1
        if e == 20:
            print(t)

def Time2():
    i = 1
    while d <= 19:
        f =  i * (i+1)
        i = i+1
        if d == 20:
            print(f)

def run1():
    global e
    for i in range(20):
        e += 1
        time.sleep(1)


def run2():
    global d
    for i in range(20):
        d += 1
        time.sleep(1)

def main():
    t1 = threading.Thread(target=Time1)
    t2 = threading.Thread(target=run1)
    t3 = threading.Thread(target=Time2)
    t4 = threading.Thread(target=run2)

    t1.start()
    t3.start()
    t2.start()
    t4.start()

    while e <= 20:
        print(e)
        time.sleep(1)
        if e == 20:
            print(e)
            break

if __name__ == '__main__':
    main()