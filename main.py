import random

true_num = random.randint(1, 100)

guess_number = int(input("Enter your guess between 1 and 100: "))

print(guess_number)

while True:
    if guess_number == true_num:
        print('THAT IS CORRECT! GREAT JOB!')
        break
    elif guess_number < true_num:
        print('YOUR GUESS IS TOO LOW, TRY AGAIN!')
        guess_number = int(input("Enter your guess between 1 and 100: "))

    elif guess_number > true_num:
        print('YOUR GUESS IS TOO HIGH, TRY AGAIN!')
        guess_number = int(input("Enter your guess between 1 and 100: "))
