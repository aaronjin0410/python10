# def fib(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
#
#
# print(fib(12))

def fib(n):
    n1 = 1
    n2 = 1
    n3 = 0
    if n == 1:
        return n1
    elif n == 2:
        return n2
    else:
        while n - 2 > 0:
            n3 = n1 + n2
            n1 = n2
            n2 = n3
            n -= 1
        return n3


print(fib(-1))
