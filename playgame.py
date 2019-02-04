from easymode_game import Person
from Magic import Magic

print("This is the instruction")

#magic
fire = Magic("Fire",10,30,"red")
water = Magic("Water",20,10,"nocolor")
magic_list = [fire,water]

player=Person("Edward",500,100,50,magic_list)
enemy=Person("Vampire",1000,100,20,magic_list)

player.get_stats()
enemy.get_stats()

running=True
while running:

    #PLAYER TURN
    print(player.name)
    print("Choose your action")
    player.choose_action()

    try:
        choice=int(input(">>>:"))
    except ValueError:
        print("Choose a proper number!")
        continue

    action_index=choice - 1

    if action_index == 0 :
        dmg=player.generate_atk_damage()
        enemy.take_damage(dmg)

        print("You attacked {} and dealt {} damage".format(enemy.name,dmg))

    if action_index == 1:
        player.choose_magic()
        try :
            magic_choice = int(input(">>>: "))
        except ValueError:
            print("Incorrect choice")
            continue
        dmg2 = player.generate_magic_damage()
        enemy.take_damage(dmg2)

    else :
        print("Choose correctly")
        continue

    #ENEMY TURN
    enemy_choice=0
    if enemy_choice == 0:
        enemy_damage=enemy.generate_atk_damage()
        player.take_damage(enemy_damage)

        print("{} attacked {} and dealt {} damage".format(enemy.name,player.name,enemy_damage))

print("---------------------------")
player.get_stats()
enemy.get_stats()

if player.hp == 0:
    print("You lost ! Game Over")
    running = False
if enemy.hp == 0:
    print("You won")
    running = False
