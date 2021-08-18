print(__file__)

numbers = [1, 2, 3, 4, 5, 6]

squares = [ number ** 2 for number in numbers]
# for number in numbers:
#     squares.append(number**2)

print(squares)

text = "The Big Blue sky"
capitals = [char.upper() for char in text]
print(capitals)
words = [word.upper() for word in text.split(' ')]
print(words)
