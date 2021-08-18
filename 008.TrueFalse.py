if 0:       #0->false
    print("True")
else:
    print("False")
name = input("Please Enter Your Name ")
if name:  #if string not empty then it is taken as true
    print("Hello {}".format(name))
else:
    print("Are you a man with no Name")