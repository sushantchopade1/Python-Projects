import random

number_to_guess = random.randint(1,100)
while True:
    try:
        guess = int(input("Guess the number: "))

        if guess < number_to_guess:
            print("Too low! ")

        elif guess > number_to_guess:
            print("Too high! ")

        else:
            print("Good! you guessed the number!")
            break

    except ValueError:
        print("Please enter a number!")

