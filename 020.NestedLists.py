even = [2,4,6,8]
odd = [1,3,5,7,9]

numbers = [even,odd]

print(numbers)

for number_list in numbers:
    print(number_list)

    for value in number_list:
        print(value)

print()

menu = [
    ["eggs","bacon"],
    ["eggs","sausage","bacon"],
    ["eggs","spam"],
    ["eggs","spam","bacon"],
    ["eggs","sausage","spam","bacon"],
    ["eggs","sausage","spam","bacon","spam","tomato","spam"],
    ["spam","egg","spam","spam","bacon","spam"],
]

for meal in menu:
    if "spam" not in meal:
        print(meal)

        for item in meal:
            print(item)
    else:
        print("{0} has spam core of {1}".format(meal,meal.count("spam")))

print()
for meal in menu:
    for item in meal:
        if item != "spam":
            print(item,end=' ')
    print()

print()
for meal in menu:
    print(meal)
for index in range(len(meal)-1,-1,-1):
    if meal[index]== "spam":
        del meal[index]

print("new meal")
print(menu)

