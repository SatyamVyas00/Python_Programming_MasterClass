#                     1111
#           01234567890123
sentence = "Python Strings"
print(sentence)
print(sentence[0])
print(sentence[1])
print(sentence[2])
print(sentence[3])
print(sentence[4])
print(sentence[5])
print(sentence[6])
print(sentence[7])
print(sentence[8])
print(sentence[9])
print(sentence[10])
print(sentence[11])
print(sentence[12])
print(sentence[13])

#
print()
print("#Negative Indexing")
# Negative Indexing
print(sentence[-1])  #13-14
print(sentence[-2])  #12-14
print(sentence[-3])  #11-14
print(sentence[-4])  #10-14
print(sentence[-5])  #9-14
print(sentence[-6])  #8-14
print(sentence[-7])  #7-14
print(sentence[-8])  #6-14
print(sentence[-9])  #5-14
print(sentence[-10]) #4-14
print(sentence[-11]) #3-14
print(sentence[-12]) #2-14
print(sentence[-13]) #1-14
print(sentence[-0])  #14-14

#
print()
print("#Slicing")
#Slicing
print(sentence[0:6])    #From sentence[0](P) upto sentence[6] but not including sentence[6]( ) so till sentencce[5](n)
print(sentence[7:13])   #Becuase s is the 13th charcater it will not print
print(sentence[:6])     #From Start till the Specified
print(sentence[7:])     #From Specified till the last character

print(sentence[:])      #From Starting till End

#
print()
print("#Slicing in Steps")
#Slicing in Steps
print(sentence[0:6:2])  #Pto['P(0)' y 't(2)' h 'o(4)' n]
print(sentence[0:6:3])  #Pto['P(0)' yt 'h(3)' on]

number="0,123;123:123 123,123;123"
seperators=number[1::4]
print(seperators)

#
print()
print("#Slicing Backwards")
#Slicing Backwards
letters = "abcdefghijlkmopqrstuvwxyz"
backwards = letters[25::-1]
print(backwards)

#
print()
print("#String Operators")
#String Operators
string1="he's "
string2="probably "
string3="pinning "
string4="for the "
string5="fjords"
print(string1+string2+string3+string4+string5)
print("he's "+"probably "+"pinning "+"for the "+"fjords ")

print("Hello " *5)
today = "Sunday"
print("day" in today)
print("sun" in today)
print("Sun" in today)
print("fri" in today)
print("good" in "weather")

#
print()
print("#String Replacements")
#String Replacements
age=24
print("My age is {0} years".format(age))

print("There are {0} days in  {1}, {2}, {3}, {4}, {5}, {6} and {7}".format(31,"Jan","Mar","May","Jul","Aug","Oct","Dec"))
print("Jan: {0}, Feb: {2}, Mar: {0}, Apr: {1}, May: {0}, Jun: {1}, Jul: {0}, Aug: {0}, Sep: {1}, Oct: {0}, Nov: {1}, Dec: {0}".format(31,30,28))

#
print()
print("#String Formatting")
#String Formatting
for i in range(1,13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i,i**2,i**3))

print()
for i in range(1,13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i,i**2,i**3))

print()
print("Pi is approximately {0:12}".format(22/7))
print("Pi is approximately {0:12f}".format(22/7))
print("Pi is approximately {0:12.50f}".format(22/7))
print("Pi is approximately {0:52.50f}".format(22/7))
print("Pi is approximately {0:<62.50f}".format(22/7))
print("Pi is approximately {0:<72.56f}".format(22/7))

print()
for i in range(1,13):
    print("No. {} squared is {:} and cubed is {:4}".format(i,i**2,i**3))


#
print()
print("#f-String")
#f-string
name="Satyam"
age=20
print(name+ f" is {age} years old")
print(type(age))

print(f"Pi is approximately {22/7:12.50f}")
pi=22/7
print(f"Pi is approximately {pi:12.50f}")

