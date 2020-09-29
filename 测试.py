import time


for i in range(0,10):
    print('\r',10-i,end='')
    time.sleep(1)

a = 0
b = 1

for i in range(1000):
    a, b = b, a+b
    print(a)
    time.sleep(0.01)


