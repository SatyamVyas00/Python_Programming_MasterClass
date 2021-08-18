# if function doesnt return anything then by default it will return None
def mutiply(x,y):
    result = x * y
    return result

answer = mutiply(10.5,4)
print(answer)

answer2 = mutiply(5,7)
print(answer2)

print()

for val in range(1,6):
    two_times = mutiply(val,2)
    print(two_times)

#palindrome
def is_palindrome(string):
    # backwards = string[::-1]
    # return  backwards == string
    return string[::-1].casefold() ==  string.casefold()

word = input("Please enter a word to check: ")
if is_palindrome(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))

#palindrome setence
def is_palindrome_sentence(sentence):
    string = ""
    for alphabet in sentence:
        # if alphabet.casefold() in "abcdefghijklmoopqrstuvwxyz":
        if alphabet.isalpha():
            string = string+alphabet
    #return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)


sentence = input("Please Enter a sentence to check: ")
if is_palindrome_sentence(sentence):
    print("'{}' is a palindrome".format(sentence))
else:
    print("'{}' is not a palindrome".format(sentence))