def fizz_buzz(no: int) -> str:
    """
    This function is for the game fizz buzz
    if the number is divisible by 3 it returns 3 or if the number is divisible by 5 it returns buzz
    and if the number is divisible by both 3 and 5 it will return fizz buzz
    :param no: the number by player
    :return:it will return a String
    """
    if(no % 3 ==0) and (no % 5 ==0):
        return "fizz buzz"
    elif (no % 3 ==0):
        return "fizz"
    elif (no % 5 ==0):
        return "buzz"
    else:
        return str(no)

# for i in range(1,101):
#    print("{}: {}".format(i,fizz_buzz(i)))

input("Play Fizz Buzz.  Press Enter to Start")
print()

next_number = 0
while next_number <99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    players_answer = input("Your go: ")
    if players_answer != correct_answer:
        print("You Loose, The Correct answer was {}".format(correct_answer))
        break
else:
    print("Well Done, you reached {}".format(next_number))