age = int(input("Enter Your age "))

#and Operator
if age >= 16 and age <= 65:
    print("Have a good day at work")

print("*"*80)
#Simplified
if  16 <= age <= 65:
    print("Have a good day at work")

print("*"*80)
#or Operator
if age < 16 or age > 65:
    print("Enjoy your free time")
else:
    print("Have a good day at work")

print("*"*80)

#in and not in
parrot = "Norwegian Blue"
letter = input("Enter a Character: ")

if letter in parrot:
    print("{} is in {}".format(letter,parrot))
else:
    print("Letter {} doesnt exsist in {}".format(letter,parrot))

activity = input("What would you like to do today? ")
if "cinema" not in activity.casefold():
    print("But i want to go to Cinema")