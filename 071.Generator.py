def fibonacci():
    current, previous = 0, 1
    while True:
        yield current
        current, previous = current+previous, current


fib = fibonacci()

for i in range(10):
    print(next(fib))

print()


def odd_number():
    number = 1
    while True:
        yield number
        number += 2


odd = odd_number()

for i in range(10):
    print(next(odd))

print()


def pi_series():
    odds = odd_number()
    approximation = 0
    while True:
        approximation += (4/next(odds))
        yield approximation
        approximation -= (4/next(odds))
        yield approximation


pi = pi_series()

for i in range(10000000):
    next(pi)
print(next(pi))
