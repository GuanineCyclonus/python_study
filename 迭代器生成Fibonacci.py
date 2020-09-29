class Fibonacci(object):
    def __init__(self, all_num):
        self.all_num = all_num
        self.num = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num < self.all_num:
            ret = self.a
            self.a, self.b = self.b, self.a + self.b
            self.num += 1
            return ret
        else:
            raise StopIteration


print('请输入您想生成的斐波那契数的个数:')
num = int(input())
fibo = Fibonacci(num)
for Num in fibo:
    print('\r',Num, end='')
