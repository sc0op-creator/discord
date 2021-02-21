import random
import time 

class Goblin:
    gb_power = 15
    gb_hp = 5
class Warrior:
    wr_power = 30
    wr_hp = 10
class Dragon:
    dr_power = 60
    dr_hp = 15
while True:
    user_input = input("Do you wish to play the game : (y / n) --> ")
    if user_input.lower() == 'y':
        user_troop = Warrior()
        rndNo = random.randint(1,2)
        if rndNo == 1:
            comp_choice = Goblin()
            numGoblins = random.randint(3,7)
            chance_of_warrior = random.randint(3,14)
            def fight_with_goblin():
                print(f"You are a brave warrior and are fighting against {numGoblins} bad goblins...")
                time.sleep(2.5)
                while True:
                    user_input = input("Do you want to ?\n(a) Attack\n(b) Defend\n--> ")
                    if user_input == 'a':
                        print(f"You are fighting against {numGoblins} goblins...")
                        time.sleep(2)
                        if ((comp_choice.gb_power*numGoblins) - (user_troop.wr_hp*chance_of_warrior)) > 0:
                            print("The warrior lost...")
                        elif ((comp_choice.gb_power*numGoblins) - (user_troop.wr_hp*chance_of_warrior)) <= 0:
                            print("The Warrior won...")
                        break

                    elif user_input == 'b':
                        print(f"{numGoblins} goblins are attacking on the warrior...")
                        time.sleep(2)
                        print("The warrior is surrounded by the goblins...")
                        time.sleep(2)
                        if (user_troop.wr_power - (comp_choice.gb_hp * numGoblins)) > 0:
                            print("The warrior won...")
                        else:
                            print("The warrior losed...")
                        break
                    else:
                        print("\nEnter a correct a answer...")

            fight_with_goblin()
            break
        elif rndNo == 2:
            comp_choice = Dragon()
            chance_of_warrior = random.randint(4,7)
            numWarriors = random.randint(1,5)
            def fight_with_dragon():
                print(f"You are a brave warrior and are fighting bad dragons...")
                time.sleep(2.5)
                while True:
                    user_input = input("Do you want to ?\n(a) Attack\n(b) Defend\n--> ")
                    if user_input == 'a':
                        print(f"The warroir is having {chance_of_warrior} chanches to kill the dragon")
                        time.sleep(2)
                        print("The warrior is fighting with the dragon")
                        time.sleep(2)
                        if (comp_choice.dr_power - (user_troop.wr_hp * chance_of_warrior)) > 0:
                            print("The Warrior losed...")
                        else:
                            print("The warrior won...")
                        break
                    elif user_input == 'b':
                        print("The warrior is defending against the dragon...")
                        time.sleep(2)
                        if ((chance_of_warrior*user_troop.wr_power) / comp_choice.dr_hp) > 2:
                            print("The warrior is dead and the evil won...")
                        else:
                            print("The warrion won and the dragon is dead...")
                        break
                    else:
                        print("\nPlease enter a valid option...")
            fight_with_dragon()
            break
    elif user_input.lower() == 'n':
        print("Okay no problem...")
        break
    else: 
        print("Enter a valid option...")




