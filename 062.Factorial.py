def fact(n):
    """ calculate n! iteratively """
    result = 1
    if n > 1:
        for f in range(2,n+1):
            result *= f
    return result


def factorial(n):
    """ n! calculation using recursion """
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)


for i in range(1,6):
    print(i,fact(i))
print()
for i in range(1,6):
    print(i,factorial(i))