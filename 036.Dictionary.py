#Each key in a dictionary is unique
Consoles = {
    'Sony': 'PS-1',
    'MICROSOFT': 'X-BOX',
    'NITENDO': 'NES',
    'NVIDIA':'SHEILD',
}
My_Console = {"WINDOWS":"LAPTOP"}

print(Consoles)
#ways to access items in dictionary
#.get() is used when we are sure that the member exsits or else the program will crash
#dictonary_name["key"] is used to find an item if the item does not exsists then it will just give an error
#and it will also tell us where the error occured

sony_console = Consoles['Sony']
print(sony_console)
microsoft_console = Consoles['MICROSOFT']
print(microsoft_console)

print()

nitendo_console = Consoles.get("NITENDO")
print(nitendo_console)

print()
print("Printing dictionary using loop:")
#printing the list both methods are same
for console in Consoles:
    print(console,Consoles[console],sep=": ")
print()
print("Printing using .items() in a loop:")
for company,console in Consoles.items():
    print(company,console,sep=": ")

print()
print("Adding an Item:")
#adding items to dictionary
Consoles["Sega"]="Dreamcast"
for console in Consoles:
    print(console,Consoles[console],sep=": ")

print()
print("Changing Value:")
#changing values in a Dictonary
#Update the Virago
Consoles["Sony"]="PS-5"
for console in Consoles:
    print(console,Consoles[console],sep=": ")

print()
print("Deleting an Item using del")
#deleting an item from dictionary
del Consoles['Sega']
for console in Consoles:
    print(console,Consoles[console],sep=": ")

print()
print("Deleting using .pop():")
# del Consoles['Sega']  deleting a key which does not exist will crash the program
#Consoles.pop("Samsung")poping the value which does not exist will rasie an error with the error location
result = Consoles.pop("Samsung",None) # it will remove the item if it exist and will return the value
                                 # and if it does not exsist it will return the value we provided in this case None
print(result)
console1 = Consoles.pop("NITENDO")
print(console1)
console2 = Consoles.pop("NVIDIA","not present") #since tenere exsist in dictionary it returned the value of tenere
print(console2)

print()
print("Combining Two Dictionary:")
#Combining values of two dictionary into one
All_Console = Consoles.copy()
print(All_Console)
All_Console.update(My_Console)
print(All_Console)
print(Consoles)
print(My_Console)

print()
print("Update Dictionary:")
#Updating value of dictionary to another
print(Consoles.update(My_Console))
print(Consoles)

print()
print("Clearing an Dictionary .clear()")
#.clear() will remove all items from dictionary
Consoles.clear()
print(Consoles)