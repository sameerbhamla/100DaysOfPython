import random
import art
import game_data


def format_accounts(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"


def compare_accounts(account1, account2):
    account1_followers = account1["follower_count"]
    account2_followers = account2["follower_count"]
    if account1_followers > account2_followers:
        return 'A'
    else:
        return 'B'


score = 0
print(art.logo)
game_is_on = True
while game_is_on:
    account_a = random.choice(game_data.data)
    account_b = random.choice(game_data.data)

    print("Compare A: " + format_accounts(account_a))
    print(art.vs)
    print("B: " + format_accounts(account_b))
    user_answer = input("Who has more followers A or B?: ")
    actual_answer = compare_accounts(account_a, account_b)

    if user_answer == actual_answer:
        score += 1
        print(f"Correct! Current score: {score}\n")

    else:
        print("Wrong! Game Over!")
        exit()
