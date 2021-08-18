farm_animals = {"sheep","cow","hen"}
print(farm_animals)

for animal in farm_animals:
    print(animal)

print("*"*40)

wild_animals = set(["lion","tiger","panther","elephant","hare"])
print(wild_animals)

for animal in wild_animals:
    print(animal)

farm_animals.add("horse")
wild_animals.add("horse")

print(farm_animals)
print(wild_animals)
#sets are unordered
print()
empty_set = set()
print(type(empty_set))

even = set(range(0,40,2))
print(even)

square_tuples = (4,6,9,16,25)
squares = set(square_tuples)
print(sorted(squares))
# print(len(squares))
# print()
# #union operation
# print(even.union(squares))
# print(len(even.union(squares)))
# print(squares.union(even))
#
# print("*"*40)
# print(even.intersection(squares))
# print(even & squares)
# print(squares.intersection(even))
# print(squares & even)
#
# #difference or subrtaction operation
# print("*"*40)
# print("even - squares:")
# print(sorted(even.difference(squares)))
# print(sorted(even-squares))
# print()
# print(sorted(even))
# print(squares)
# even.difference_update(squares)
# print(sorted(even))

# print("*"*40)
# print("symmetric even - squares:")
# print(sorted(even.symmetric_difference(squares)))
# print("symmetric squares - even:")
# print(sorted(squares.symmetric_difference(even)))

# print("*"*40)
# squares.discard(4)
# squares.remove(16)
# squares.discard(8) # no error
# print(squares)
#
# try:
#     squares.remove(8)  # gives error if doesn't exsist
# except KeyError:
#     print("The item 8 is not a member of set")

# print("*"*40)
# a = set(range(0,10))
# b = set(range(0,5))
# if b.issubset(a):
#     print("b is subset of a")
#
# if a.issuperset(b):
#     print("a is superset of b")
#
# forzen sets are immutable sets
even = frozenset(range(0,100,2))
print(even)
#even.add(3)  gives error