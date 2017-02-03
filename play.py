import os
import sys
import time
import random

# TODO use a module to import common functions
# TODO use lists
# TODO do not use global variables
# TODO remove empty prints

session_dungeon = "--"
session_room = "--"
session_player_name = "PLAYER"
session_player_hp = 0
session_player_ap = 0
session_player_dp = 0
session_player_gp = 0
session_monster_name = "MONSTER"
session_monster_hp = 0
session_monster_ap = 0
session_monster_dp = 0
session_monster_gp = 0

def room_1():
    global session_dungeon, session_room
    session_dungeon = "01"
    session_room = "01"
    clear_screen()
    print_general_screen()
    print_room_description(
        "You wake up in a dark and dry room. You look around and it's looks\n"
        "like a cell. Right in front of you, close to the cell bars, there is\n"
        "a guard, drop dead..."
    )
    print_room_options([
        "Scream for help",
        "Check the guard's body"
    ])

    option = ""
    while option != "q":
        option = raw_input("Choose an option (q to quit): ")
        if option == "1":
            print_room_notice("No one listens to you, you are on your own.")
            room_1()
        elif option == "2":
            print_room_notice(
                "You find the cell key in his pocket. You leave the cell"
            )
            room_2()
        elif option == "q":
            game_over()
        else:
            print "Choose a valid option"

def room_2():
    global session_dungeon, session_room
    session_dungeon = "01"
    session_room = "02"
    clear_screen()
    print_general_screen()
    print_room_description(
        "This look like a corridor full of cells. There is an open door on\n"
        "the right and a long corridor on the left"
    )
    print_room_options([
        "Enter the open door on the right",
        "Run through the corridor on the left"
    ])

    option = ""
    while option != "q":
        option = raw_input("Choose an option (q to quit): ")
        if option == "1":
            room_3()
        elif option == "2":
            room_4()
        elif option == "q":
            game_over()
        else:
            print "Choose a valid option"

def room_3():
    global session_dungeon, session_room
    session_dungeon = "01"
    session_room = "03"
    clear_screen()
    print_general_screen()
    print_room_description(
        "You enter a messy and dry room, there are a interesting desk in the\n"
        "corner, covered with papers and a shiny drawer"
    )
    print_room_options([
        "Check the drawer",
        "Leave the room"
    ])

    option = ""
    while option != "q":
        option = raw_input("Choose an option (q to quit): ")
        if option == "1":
            global session_player_gp
            session_player_gp += 2
            print_room_notice("You found 2GP")
            room_3()
        elif option == "2":
            room_2()
        elif option == "q":
            game_over()
        else:
            print "Choose a valid option"

def room_4():
    global session_dungeon, session_room
    session_dungeon = "01"
    session_room = "04"
    clear_screen()
    print_general_screen()
    print_room_description(
        "You enter the main hall. You fell a huge shade coming from nowhere\n"
        "weaving a big axe at you, time to battle"
    )
    battle_1()

def room_5():
    global session_dungeon, session_room
    session_dungeon = "01"
    session_room = "05"
    clear_screen()
    print_general_screen()
    print_room_description(
        "After a heat battle, you still have energy to run. At the end of the\n"
        "hall, there is a dark corridor. When you enter it, you notice that\n"
        "part of the floor looks different"
    )
    print_room_options([
        "Check for traps",
        "Run like there is no tomorrow"
    ])

    option = ""
    while option != "q":
        option = raw_input("Choose an option (q to quit): ")
        if option == "1":
            print_room_notice(
                "You find a trap, a clumsy deep hole full of pythons. You jump "
                "over it."
            )
            game_over()
        elif option == "2":
            print_room_notice(
                "You fall in a deep hole and get bitten by the pythons."
            )
            game_over()
        elif option == "q":
            game_over()
        else:
            print "Choose a valid option"

def battle_1():
    global session_player_hp, session_player_ap, session_player_dp, \
        session_player_gp, session_monster_hp, session_monster_ap, \
        session_monster_dp, session_monster_gp
    turn = "player"
    player_defense = 0
    monster_defense = 0
    while session_monster_hp > 0 and session_player_hp > 0:
        clear_screen()
        print_general_screen()
        print_battle_screen()
        if turn == "player":
            dice = rolls_dice()
            option = ""
            while option != "q":
                print
                print "1 - Attack"
                print "2 - Defend"
                print
                option = raw_input("Choose an option (q to quit): ")
                if option == "1":
                    if monster_defense > 0:
                        damage = (dice + session_player_ap) - (session_monster_dp + monster_defense)
                    else:
                        damage = (dice + session_player_ap) - session_monster_dp
                    if damage < 0:
                        damage = 0
                    print "Player attacks, rolls %s, dealing %s of damage" % (dice, damage)
                    raw_input("Press any key to continue...")
                    session_monster_hp = session_monster_hp - damage
                    player_defense = 0
                    turn = "monster"
                    break
                elif option == "2":
                    player_defense = dice + session_player_dp
                    print "Player defends, rolls %s, getting %s of defense" % (dice, player_defense)
                    raw_input("Press any key to continue...")
                    turn = "monster"
                    break
                else:
                    print "Choose a valid option"
        elif turn == "monster":
            print "monster turn"
            dice = rolls_dice()
            option = random.choice(["1", "2"])
            if option == "1":
                if player_defense > 0:
                    damage = (dice + session_monster_ap) - (session_player_dp + player_defense)
                else:
                    damage = (dice + session_monster_ap) - session_player_dp
                if damage < 0:
                    damage = 0
                print "Monster attacks, rolls %s, dealing %s of damage" % (dice, damage)
                raw_input("Press any key to continue...")
                session_player_hp = session_player_hp - damage
                monster_defense = 0
                turn = "player"
            elif option == "2":
                monster_defense = dice + session_monster_dp
                print "Monster defends, rolls %s, getting %s of defense" % (dice, monster_defense)
                raw_input("Press any key to continue...")
                turn = "player"
            else:
                bug("Unknown monster action")
        else:
            bug("Unknown turn")

        if session_monster_hp <= 0:
            print "You won!"
            raw_input("Press any key to continue...")
            session_player_gp = session_player_gp + session_monster_gp
            room_5()
        elif session_player_hp <= 0:
            print "You died!"
            raw_input("Press any key to continue...")
            game_over()
        else:
            continue

def print_general_screen():
    print (
        "DUNGEONS AND PYTHONS\n"
        "--------------------------------------------------------------------------------\n"
        "Dungeon: %s, Room: %s\n"
        "Player: %s, HP: %s, AP: %s, DP: %s, GP: %s"
    ) % (
        session_dungeon,
        session_room,
        session_player_name,
        session_player_hp,
        session_player_ap,
        session_player_dp,
        session_player_gp
    )

def print_battle_screen():
    print (
        "Monster: %s, HP: %s, AP: %s, DP: %s, GP: %s"
    ) % (
        session_monster_name,
        session_monster_hp,
        session_monster_ap,
        session_monster_dp,
        session_monster_gp
    )

def game_over():
    print
    print "GAME OVER!"
    print
    exit(1)

def bug(message):
    print message
    exit(1)

def rolls_dice():
    return random.randint(1, 6)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_room_description(description):
    print
    print_smoothly(description)
    print

def print_room_options(options):
    print
    options_counter = 1
    for option in options:
        print "%s - %s" % (options_counter, option)
        options_counter += 1
    print

def print_room_notice(notice):
    clear_screen()
    print_smoothly(notice)
    print
    raw_input("Press any key to continue...")

def print_smoothly(message):
    print message
    # for offset in range(0, len(message)):
    #     time.sleep(0.04)
    #     sys.stdout.write(message[offset])
    #     sys.stdout.flush()

def start():
    global session_player_name, session_player_hp, session_player_ap, \
        session_player_dp, session_player_gp, session_monster_name, \
        session_monster_hp, session_monster_ap, session_monster_dp, \
        session_monster_gp
    print "Welcome to Dungeons and Pythons\n"
    session_player_name = raw_input("What's your name? ")
    session_player_hp = 8
    session_player_ap = 2
    session_player_dp = 2
    session_player_gp = 0
    session_monster_name = "Ugly Orc"
    session_monster_hp = 4
    session_monster_ap = 1
    session_monster_dp = 1
    session_monster_gp = 2
    room_1()

start()
