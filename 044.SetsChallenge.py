vowels = frozenset({"a","e","i","o","u"})
text = input("Please Enter your text:")
non_vowels = set()
for alpha in text:
    if alpha.casefold() not in vowels:
        non_vowels.add(alpha)
print(sorted(non_vowels))