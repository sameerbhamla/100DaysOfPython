############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

# Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
import random


def deal_card(cards):
    return random.choice(cards)


# Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
def calculate_score(player_cards):
    sum_score = sum(player_cards)
    # Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10)
    # and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if sum_score == 21 and len(player_cards) == 2:
        return 0
    # Inside calculate_score() check for an 11 (ace). If the score is already over 21,
    # remove the 11 and replace it with a 1. You might need to look up append() and remove().

    if sum_score > 21 and 11 in player_cards:
        player_cards.remove(11)
        player_cards.append(1)

    return sum(player_cards)


# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user
# both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user
# has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score
# is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(score1, score2):
    if score1 == score2:
        print("Its a Draw!")
    elif score2 == 0:
        print("Computer wins")
    elif score1 == 0:
        print("User win! ")
    elif score1 > 21:
        print('Computer wins')
    elif score2 > 21:
        print("You win!")
    elif score1 > score2:
        print("You win!")
    else:
        print("Computer wins")


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print(deal_card(cards))
# Deal the user and computer 2 cards each using deal_card() and append().
user_cards = []
computer_cards = []
user_cards.append(deal_card(cards))
user_cards.append(deal_card(cards))

computer_cards.append(deal_card(cards))
computer_cards.append(deal_card(cards))

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack
#
def play_game():
    game_is_on = True
    while game_is_on:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your cards {user_cards}, current score: {user_score}")
        print(f" Computers first card {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_is_on = False
        else:
            response = input("do you want to hit or stay?: ")
            if response.lower() == 'hit':
                user_cards.append(deal_card(cards))
            else:
                game_is_on = False

    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card(cards))
        computer_score = calculate_score(computer_cards)

    print(f"Final result")
    print(f"Your cards {user_cards} with a final score of {user_score}")
    print(f"Computer cards {computer_cards} with a final score of {computer_score}")
    compare(user_score, computer_score)

game_continues = True

while game_continues:
    play_game()
    response = input("Would you like to play again?(y/n): ")
    if response.lower() == 'y':
        user_cards = []
        computer_cards = []
    else:
        quit()

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.


# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
