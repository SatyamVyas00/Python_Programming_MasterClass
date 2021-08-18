#functiona annotations or type hints
# def function_name(variable : data_type) -> return_type:
def fibonacci(n:int = 0) -> None:
    """ Print the the Fibonacci numbers till `n` th digit, for positive `n` """
    if 0 <= n <= 1:
        print(n)
        return None

    n_minus1 = 0
    n_minus2 = 1

    print("Fibonacci series till {}".format(n))
    print(n_minus1)
    print(n_minus2)
    while(n-2 != 0):
        temp = n_minus1+n_minus2
        n_minus1=n_minus2
        n_minus2=temp
        n = n-1
        print(temp)

fibonacci(10)
print()
fibonacci()