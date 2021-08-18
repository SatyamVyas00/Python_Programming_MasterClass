# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n*factorial(n-1)
#
#
# try:
#     print(factorial(1000))
# except RecursionError:
#     print("This Program cannot Calculate factorial that large")
#
# print("Program Terminating")


def div(a, b):
    print(int(a)/int(b))


f = input("Please Enter the First Number: ")
s = input("Please Enter the Second Number: ")

try:
    div(f, s)
except(Exception):
    print("Exception Occured")
