even = [2,4,6,8]
odd = [1,3,5,7,9]

#min() and max()
print(min(even))
print(max(even))
print(min(odd))
print(max(odd))

print()
#len()
print(len(even))
print(len(odd))
#count
print()
print("mississippi".count("iss"))
#append
even.append(10)
print(even)

# .extend
print()
even.extend(odd)
print(even)
#sorting
print()
even.sort()
print(even)
# reverse sorting
print()
even.sort(reverse=True)
print(even)
