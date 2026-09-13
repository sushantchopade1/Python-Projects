secret_word = "Sushant"
guess = ""
guess_count = 0
guess_limit = 4
out_of_guess = False

while guess != secret_word and not(out_of_guess):
    if guess_count < guess_limit:
        guess_count += 1
        guess = input("Enter a word")
    else:
        out_of_guess = True

if out_of_guess:
    print("Out of the game")
else:
    print("You win ,you  guessed the word")

