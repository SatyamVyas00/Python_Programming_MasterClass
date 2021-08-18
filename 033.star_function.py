# *variable_name is used to unpack any sequence type
numbers = (0,1,2,3,4,5)

print(numbers,sep=";")
print(*numbers,sep=";")
print(0,1,2,3,4,5,sep=";")
print()

def test_star(*args):
    print(args)
    for x in args:
        print(x)

test_star(0,1,2,3,4,5)
print()
test_star()
#check 029.PrintColors program for changes and use of *