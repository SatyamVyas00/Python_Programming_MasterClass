parrot = "Norwegian Blue"

#for loop
for character in parrot:
    print(character)

print("*"*80)
#range
for i in range(0,10,2):
    print("i is now {}".format(i))

print("*"*80)

for i in range(10,0,-2):
    print("i is now {}".format(i))

print("*"*80)
#nested for loop

for i in range(1,11):
    for j in range(1,11):
        print("{0} X {1} = {2}".format(i,j,i*j))
    print("--------------")