import timeit

setup="""\
text = "The Big Blue sky"

def char_comp():
    capitals = [char.upper() for char in text]
    #print(capitals)


# use  map
def char_map():
    map_capital = list(map(str.upper, text))
    #print(map_capital)


def word_comp():
    words = [word.upper() for word in text.split(' ')]
    #print(words)

# use map
def word_map():
    map_word = list(map(str.upper, text.split(' ')))
    #print(map_word)
"""

print("char_comp(): "+str(timeit.timeit("x = char_comp()", setup, number=100000)))
print("char_map(): "+str(timeit.timeit("x = char_map()", setup, number=100000)))
print("word_comp(): "+str(timeit.timeit("x = word_comp()", setup, number=100000)))
print("word_map(): "+str(timeit.timeit("x = word_map()", setup, number=100000)))
