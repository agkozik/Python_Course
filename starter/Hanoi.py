import functools


@functools.lru_cache(maxsize=None)
def hanoi(n, a, b, c):
    if n != 0:
        hanoi(n-1, a, c, b)
        if a != c:
            print("Move a ring from ", a, "to", c)
        hanoi(n-1, b, a, c)


hanoi(5, 'A', 'B', 'C')