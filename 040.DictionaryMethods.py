
d={
    0:"zero",
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
    "IV":"four"
}

d2 = {
    7:"lucky seven",
    10:"ten",
    3:"this is the new three",
}

pantry_items = ['chicken','spam','egg','bread','lemon']
#form keys from a list:-
# new_dict = dict.fromkeys(pantry_items,0)
# print(new_dict)

#old method to iteratre over keys:-
#keys = d.keys()
#print(keys)

#new method to iterate over keys:-
#for item in d.keys():
#    print(item)

#update method from one dictionary to another
# d.update(d2)
# print(d)
# print()
# d.update(enumerate(pantry_items))
# for key,value in d.items():
#     print(key,value)

#.values() method
v = d.values()
print(v)
d[10] = "ten"
print(v)

print("four" in v)
print("eleven" in  v)

# keys = list(d.keys())
# values = list(v)
# if "four" in values:
#     index = values.index("four")
#     key = keys[index]
#     print(f"{d[key]} was  found with the key {key}")
print()
for key, value in d.items():
    if value == "four":
        print(f"{d[key]} was  found with the key {key}")


