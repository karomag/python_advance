from datetime import datetime
from functools import wraps, lru_cache


def time_stamped(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print()
        print('Completed in time:', datetime.now() - start)
        return result

    return wrapper


@time_stamped
def my_pow(*args, k_pow=2):
    return [x ** k_pow for x in args]


def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


@time_stamped
def type_number(lst, _type='even'):
    if _type == 'even':
        return [x for x in lst if x % 2 == 0]
    elif _type == 'odd':
        return [x for x in lst if x % 2 == 1]
    elif _type == 'simple':
        return [x for x in lst if isPrime(x)]


def trace(line):
    """
    Trace calls made to the decorated function.
    @trace("____")
    def fib(n):
        ....
    >>> fib(3)
     --> fib(3)
    ____ --> fib(2)
    ________ --> fib(1)
    ________ <-- fib(1) == 1
    ________ --> fib(0)
    ________ <-- fib(0) == 1
    ____ <-- fib(2) == 2
    ____ --> fib(1)
    ____ <-- fib(1) == 1
     <-- fib(3) == 3
    """

    def deco_func(func):
        # func.indent = 0
        indent = 0

        @wraps(func)
        def wrapper(n):
            nonlocal indent
            print(line * indent, '-->', '{0}({1})'.format(func.__name__, n))
            indent += 1
            val = func(n)
            indent -= 1
            print(line * indent, '<--', '{0}({1}) == {2}'.format(
                func.__name__, n, val)
                  )
            # indent -= 1
            return val

        return wrapper

    return deco_func


@lru_cache(1024)
@trace('____')
def fib(n):
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    print('Result my_pow with default k_pow:', *my_pow(1_000, 2_555, 5_123, 60))
    print('Result my_pow with k_pow=3:', *my_pow(1_000, 2_555, 5, 6, k_pow=3))
    print('Only even from list:', type_number([11, 22, 33, 44, 55], 'even'))
    print('Only odd from list:', type_number([111, 222, 354, 456, 555], 'odd'))
    print('Only simple from list:', type_number([11, 12, 30, 44, 5, 3], 'simple'))
    print()
    print()
    fib(5)
