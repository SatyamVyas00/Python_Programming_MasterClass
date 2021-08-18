def sum_numbers(*numbers:float) -> float:
    """
    This function returns the sum of all passed arguments
    :param numbers:arguments or number to calculate sum of
    :return:int(sum of number)
    """
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum

print(sum_numbers(1,2,3))
print(sum_numbers(80,22,2))
print(sum_numbers(12.5,3.127,98.1))
print(sum_numbers(1.1,2.2,5.5))