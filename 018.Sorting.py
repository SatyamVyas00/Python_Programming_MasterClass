# sorted()
pangram = "The quick brown fox jump over a lazy dog"

letters = sorted(pangram)
print(letters)

print()

numbers = [8.9,3.4,9.0,4.5,8,1,29,0,0.5]
sorted_numbers = sorted(numbers)
print(numbers)
print(sorted_numbers)

print()

numbers.sort()
print(numbers)

#case_Insensitive Sorting
print()
missing_letter = sorted("The quick brown fox jumped over a lazy dog",key=str.casefold)
print(missing_letter)