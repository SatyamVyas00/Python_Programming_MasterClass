#this import copy module which can be used  to create deep copy
import copy

#.copy() function only creates a shallow copy
lion_list = ["scary","big","cat"]
elephant_list = ["big","grey","wrinkled"]
teddy_list = ["cuddly","stuffed"]

animals = {
    "lion" : lion_list,
    "elephant" : elephant_list,
    "teddy" : teddy_list,
}
print(".copy() or shallow copy:-")
#Shallow Copy:-
things = animals.copy()
print(id(things["teddy"]),things["teddy"])
print(id(animals["teddy"]),animals["teddy"])

print()

teddy_list.append("toy")
print(id(things["teddy"]),things["teddy"])
print(id(animals["teddy"]),animals["teddy"])
print()

print()
print("copy.deepcopy() or deep copy:-")
#deep copy
things = copy.deepcopy(animals)
print(id(things["teddy"]),things["teddy"])
print(id(animals["teddy"]),animals["teddy"])

print()

teddy_list.append("toy")
print(id(things["teddy"]),things["teddy"])
print(id(animals["teddy"]),animals["teddy"])
print()