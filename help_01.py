# import random
# import time 

# class Goblin:
#     gb_power = 15
#     gb_hp = 5
# class Warrior:
#     wr_power = 30
#     wr_hp = 10
# class Dragon:
#     dr_power = 60
#     dr_hp = 15
# user_input = input("Do you wish to play the game : (y / n) --> ")
# if user_input.lower() == 'y':
#     user_troop = Warrior()
#     rndNo = random.randint(1,2)
#     if rndNo == 1:
#         comp_choice = Goblin()
#         numGoblins = random.randint(3,7)
#         chance_of_warrior = random.randint(3,14)
#         def fight_with_goblin():
#             print(f"You are a brave warrior and are fighting against {numGoblins} bad goblins...")
#             time.sleep(2.5)
#             while True:
#                 user_input == input("Do you want to ?\n(a) Attack\n(b) Defend\n--> ")
#                 if user_input == 'a':
#                     print(f"You are fighting against {numGoblins} goblins...")
#                     time.sleep(2)
#                     if ((comp_choice.gb_power*numGoblins) - (user_troop.wr_hp*chance_of_warrior)) > 0:
#                         print("The warrior lost...")
#                     elif ((comp_choice.gb_power*numGoblins) - (user_troop.wr_hp*chance_of_warrior)) <= 0:
#                         print("The Warrior won...")

#                 elif user_input == 'b':
#                     print(f"{numGoblins} goblins are attacking on the warrior...")
#                     time.sleep(2)
#                     print("The warrior is surrounded by the goblins...")
#                     time.sleep(2)
#                     if (user_troop.wr_power - (comp_choice.gb_hp * numGoblins)) > 0:
#                         print("The warrior won...")
#                     else:
#                         print("The warrior losed...")

#         fight_with_goblin()
#     elif rndNo == 2:
#         comp_choice = Dragon()
#         chance_of_warrior = random.randint(4,7)
#         def fight_with_dragon():
#             print(f"You are a brave warrior and are fighting bad dragons...")
#             time.sleep(2.5)
#             print(f"The warroir is having {chance_of_warrior} chanches to kill the dragon")
#             time.sleep(2)
#             print("The warrior is fighting with the dragon")
#             time.sleep(2)
#             if (comp_choice.dr_power - (user_troop.wr_hp * chance_of_warrior)) > 0:
#                 print("The Warrior losed...")
#             else:
#                 print("The warrior won...")
#         fight_with_dragon()
# elif user_input.lower() == 'b':
#     print("Okay no problem...")
# else: 
#     print("Enter a valid option...")


# import turtle
# import random
# from turtle import*

# tim = turtle.Turtle()
# tim.speed(0)
# tim.width(3)
# tim.shape('triangle')
# ht()
# def up():
#     tim.setheading(90)
#     tim.forward(50)

# def down():
#     tim.setheading(270)
#     tim.forward(50)

# def left():
#     tim.setheading(180)
#     tim.forward(50)

# def right():
#     tim.setheading(0)
#     tim.forward(50)

# ###############################

# turtle.listen()
# turtle.onkey(up, 'w')
# turtle.onkey(down, 's')
# turtle.onkey(left, 'a')
# turtle.onkey(right, 'd')


# turtle.mainloop()

import keyboard
while True:
    try:
        if keyboard.is_pressed('q'): 
            print('You Pressed A Key!')
            break  
    except:
        break  
