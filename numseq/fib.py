def fib(n):
    result = [0]
    a, b = 0, 1
    for unused_i in range(n):
        result.append(b)
        a, b = b, a+b
    return result[-1]
