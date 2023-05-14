#I added a limitation to the number of guesses (7) and print the counter to show the user the number of tries left until the end of the game.

hidden_word = "pathway"
counter = 0
print("Welcome to the word guessing game!\n")

for i in range(7):
    counter += 1
    user_guess = input("What is your guess? ")
    hint = ''
    
    if len(user_guess) != len(hidden_word):
        print(f"Your guess must be the same length ({len(hidden_word)}) as the hidden word. Try again.")
        continue
    
    if user_guess.lower() == hidden_word:
        print(f"\nCongratulations! You guessed it!\nIt took you {counter} guesses.")
        break

    elif user_guess.lower() != hidden_word and counter >= 7:
        print("Your guesses were not correct. You already used your 7 guesses!")
        break    

    else:
        print(f"Your guess was not correct. Try again!\nYou already used {counter} of 7 guesses.")

        for i, letter in enumerate(hidden_word):
            if i < len(user_guess) and letter.lower() == user_guess[i]:
                hint += letter.upper()
            elif letter.lower() in user_guess:
                hint += letter.lower()
            else:
                hint += "_ "
        print(f'Your hint is: {hint}\n')