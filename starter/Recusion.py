def non_recursion(n):
    result = 1
    for multiplayer in range(n):
        result *= multiplayer
    return result


def recursive_fact(n):
    if n == 0:
        return 1
    else:
        return n * recursive_fact(n-1)


print(recursive_fact(100))

print(non_recursion(100))