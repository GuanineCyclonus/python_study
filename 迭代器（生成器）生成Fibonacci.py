from numba import jit


@jit()
def create_Fibonacci(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        yield a
        a, b = b, a+b
        current_num += 1

print('请输入斐波那契数的个数:')
num = int(input())
obj = create_Fibonacci(num)
while True:
    try:
        ret = next(obj)
        print(ret)
    except StopIteration:
        break
