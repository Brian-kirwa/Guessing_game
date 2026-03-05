import random

lowest_num=1

highest_num=100

answer=random.randint(lowest_num,highest_num)

guesses=0

is_running= True

print("Python Guessing game")

print(f"Enter a number between {lowest_num} and {highest_num}: ")

while is_running:

    guess=input("Enter your Guess: ")

    if guess.isdigit():

        guess=int(guess)

        guesses=guesses+1

        if guess <lowest_num or guess > highest_num:

            print("That number is out of range")

        elif guess < answer:

            print("Your guess is too low!Too low")

        elif guess > answer:

            print("Your guess is too high!Too high")
        else:

            print(f"CORRECT!The  answer was{answer}")

            print(f"Number of guesses is {guess} ")

            is_running=False

    else:
        print("Invalid input")

        print(f"Enter a number between {lowest_num} and {highest_num}: ")




