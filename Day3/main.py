print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇
step0 = True

while step0:
    response = input("Where would you like to go? left or right?")
    if response.lower() == "right":
        print("HAHA you fell into a hole gg Game Over")
        step0 = False
    elif response.lower() == "left":
        step1 = True
        print("You have gone left and taken a turn into a lake.")

        while step1:
            response = input("What would you like to do Swim or Wait? ")
            if response.lower() == "swim":
                print("You swam in the river and were attacked by a trout! GG Game Over")
                step0 = False
                step1 = False
            elif response.lower() == "wait":
                step2 = True
                print("You have waited and magically the water has formed a tunnel you can walk through, at the end "
                      "you see three doors Red, Yellow, and Blue ")

                while step2:
                    response = input("Which door are you going to take? ")
                    if response.lower() == "red":
                        print(
                            "You opened the doors to hell and were burned by fire, Ultimately killing you GG Game Over")
                        step2 = False
                        step1 = False
                        step0 = False
                    elif response.lower() == "blue":
                        print(
                            "You opened the door and were attacked by wild beasts, Ultimately killing you GG Game Over")
                        step2 = False
                        step1 = False
                        step0 = False
                    elif response.lower() == "yellow":
                        print("You made it to the end and found the treasure! GG You Win!")
                        step2 = False
                        step1 = False
                        step0 = False
