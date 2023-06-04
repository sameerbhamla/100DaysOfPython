import random
import hangman_art
import hangman_words


def checkifwon(display, chosenWord):
    checkword = ""
    for letter in display:
        checkword += letter

    if checkword == chosenWord:
        return True
    else:
        return False


print(hangman_art.logo)
lives = 6
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)
guessed_letters = []
display = []
gameNotOver = True

# Creating display
for letter in chosen_word:
    display.append('_')

# Printing initial displays
print(hangman_art.stages[lives])
print(display)

# Starting game
while gameNotOver:
    # Ask user to guess
    guess = input("Take a guess: ").lower()
    # if guess is unique, add it to the already guessed letter list
    if guess not in guessed_letters:
        guessed_letters.append(guess)

        # Update display to fill in the guessed letter
        for i in range(0, len(chosen_word)):
            if guess == chosen_word[i]:
                display[i] = guess

            # If the user has won end the game
            if checkifwon(display, chosen_word):
                gameNotOver = False
                print("You Win")
                quit()
        # If the guess is wrong reduce lives and notify them
        if guess not in chosen_word:
            lives -= 1
            print(f"Letter {guess} was not a letter in the word")

            # If the lives become 0 print the display and exit game because the user lost
            if lives == 0:
                print(hangman_art.stages[lives])
                print(display)
                print("You Lose")
                quit()

            # If lives is not zero print the updated hangman stage and the display again
            print(hangman_art.stages[lives])
            print(display)

        else:
            # if guess is in the word reprint the stage and display with updated values
            print(hangman_art.stages[lives])
            print(display)

    else:
        # If the guess already exists then notify the user to try again
        print(f"Letter {guess} has already been guessed")

