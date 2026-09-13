import random

emojis = {'r':'🪨','p':'📃','s':'✂️'}
choices = ('r','p','s')
while True:
    useer_choice =input("choose your choice (r/p/s): ").lower()
    if useer_choice not in choices:
        print("invalid choice")
        continue

    computer_choice = random.choice(choices)

    print(f"you chose {emojis[useer_choice]}")
    print(f"computer chose {emojis[computer_choice]}")

    if useer_choice == computer_choice:
        print("Tie!")
    elif(
        (useer_choice == 'r' and computer_choice == 's') or
        (useer_choice == 's' and computer_choice == 'p') or
        (useer_choice == 'p' and computer_choice == 'r')
    ):
        print("You win!")
    else:
        print("You lose!")

    should_continue = input("continue? (y/n): ").lower()
    if should_continue == 'n':
        break

