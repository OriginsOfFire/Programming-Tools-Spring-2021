b = 15


def test_fib(num):
    if num == 0:
        return 0
    if num == 1 or num == 2:
        return 1
    return test_fib(num-1) + test_fib(num-2)


def test_func(num):
    return (num ** 2) * b


def test_func_2(num):
    return num * test_func(num)


def test_another_func_1(num):
    return num ** 2


def test_another_func_2(num):
    return num * 3


def test_another_func(num):
    ans = 1
    while ans < 10:
        ans *= test_another_func_1(num) * test_another_func_2(num)
    return ans
