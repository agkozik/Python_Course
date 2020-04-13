# import functools
#
#
# @functools.lru_cache(maxsize=None)
# def fib(n):
#     if n ==1 or n == 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
#
#
# for i in range(1, 100):
#     print(fib(i))

# non-recursion:
n = 100
fibs = [1, 1]
for i in range(n - 2):
    fibs.append(fibs[i] + fibs[i + 1])
for i in fibs:
    print(i)
