name = input("Please Enter Your Name ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

#if else
if age >= 18 :
    print("You are old Enough to Vote")
else:
    print("Please come back in {0} years".format(18-age))

#elif
if age<18:
    print("Please come back in {0} years".format(18-age))
elif age == 900:
    print("Sorry, Yoda, you die in Return of Jedi")
else:
    print("You are old Enough to Vote")