def factorial(num: int) -> int:
    """
    This function returns the factorial of the given number
    :param num: The num of which factorial is to be calculated
    :return: factorial value
    """
    if num == 0:
        return 1

    if num>0:
        return num*factorial(num-1)


for i in range (10):
    print("{}: {}".format(i, factorial(i)))
