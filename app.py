# Dr. Yu's 100 days of code day 3, Treasure Island! 
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')


print(f'''Welcome To Treasure Island!
\nYour mission is to find the treasure!''')
choice = input('''You\'re at at cross road. Where do you want to go?
left or right? 
Choice left or right: ''').lower()
if choice == 'right':
    print("You fell into a hole! Game Over :( Play again!")
else:
    choice = input('''You come to a lagoon. You path takes you to the other side.
How do you want to get there? Do you want to swim across, or wait for a boat?
choice wait or swim: ''').lower()
    if choice ==  'swim':
        print('''A shark has eaten you! Game Over :( Try again!''')
    else:
        choice = input('''You make it a across! Your last objective is to pickk
the correct door in front of you! There is a red, yellow, and a blue door.
Choice yellow, blue, or red: ''').lower()
        if choice == 'red':
            print('''An ancient curse awakens and burns you! Game Over!''')
        elif choice == 'yellow':
            print("You have found the treasure! You win!")
        elif choice =='blue':
            print("An ancient beast awakens and attacks you! Game Over!")
        else:
            print('''A proper door was not choose, the island does not take
kindly to that!''')