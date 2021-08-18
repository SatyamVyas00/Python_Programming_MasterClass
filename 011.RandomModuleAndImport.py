import random

highest = 10
answer = random.randint(1,highest)
print(answer)        # TODO: Remove after Testing

guess = 0
while guess != answer:
    print("Please guess a number between 1 and {} or 0 to quit".format(highest))
    guess = int(input())
    if guess == 0:
        break
    if guess>answer:
        print("please enter a lower number ")
    if guess<answer:
        print("please enter a higher number ")


if guess == answer:
    print("You have guessed the correct answer({})".format(guess))
else:
    print("You have Exited the correct answer was {}".format(answer))