def fib(num):
    a = 0
    b = 1
    for i in range(num-1):
        yield a
        temp = a
        a = b
        b += temp


for x in fib(20):
    print(x)
