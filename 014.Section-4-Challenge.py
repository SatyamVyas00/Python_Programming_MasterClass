choice = None
print("Please choose your option from the list below")
while choice != 0:
    print()
    print("1.Learn Python")
    print("2.Learn Java")
    print("3.Learn C")
    print("4.Learn C++")
    print("0.Exit")

    choice=int(input())

    if(choice == 1):
        print("Lets Learn Python")
    elif(choice == 2):
        print("Lets Learn Java")
    elif(choice == 3):
        print("Lets Learn C")
    elif(choice == 4):
        print("Lets Learn C++")
else:
    print("You have Choose to Exit")