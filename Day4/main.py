import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
validResponse = False
response = ""
while not validResponse:
    try:
        response = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
    except ValueError:
        pass
    if 2 >= int(response) >= 0:
        validResponse = True
    else:
        print("Invalid response try again ")

AiChoice = random.randint(0, 2)

if response == "0":
    print(f"You chose {rock} ")
    print("Computer chose:")
    if AiChoice == 0:
        print(rock)
        print("Its a tie!")
    elif AiChoice == 1:
        print(paper)
        print("You Lose")
    else:
        print(scissors)
        print("You win!")
elif response == "1":
    print(f"You chose{paper} ")
    print("Computer chose:")
    if AiChoice == 0:
        print(rock)
        print("You win!")
    elif AiChoice == 1:
        print(paper)
        print("Its a tie!")
    else:
        print(scissors)
        print("You lose")
else:
    print(f"You chose{scissors} ")
    print("Computer chose:")
    if AiChoice == 0:
        print(rock)
        print("You lose")
    elif AiChoice == 1:
        print(paper)
        print("You win!")
    else:
        print(scissors)
        print("Its a tie!")
