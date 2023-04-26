def function_sum(a=0, b=0):
    total = a + b
    return total


result = function_sum()
print(result)


def power(base, exponent=0):
    total = base ** exponent
    return total


result = power(5)
print(result)


def product(a, *args):
    total = a
    for x in args:
        total = total * x
    return total


result = product(5, 2, 3, 1)
print(result)


def addition(a, b, c, d):
    total = a + b + c + d
    return total


result = addition(b=5, a=2, d=3, c=4)
print(result)

result = addition(3, 4, d=5, c=2)
print(result)


# force keywords arguments
def addition_2(*, a, b, c):
    total = a + b + c
    return total


result = addition_2(b=2, a=3, c=5)
print(result)


# Positional-only args
def func(x, y, /):
    total = x * y
    return total


# error => result = func(x=3, y=2)

result = func(5, 5)
print(result)


def quotient(a=float, b=float):
    """
    Compute the quotient between two numbers
    :param a: float
    :param b: float, different from zero
    :return: float
    """

    if b != 0:
        total = a / b
        return total
    else:
        print("b must be different from zero")


result = quotient(4, 5)
print(result)