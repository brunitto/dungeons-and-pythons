import os
import session
import sys
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_general_screen():
    print (
        "DUNGEONS AND PYTHONS\n"
        "--------------------------------------------------------------------------------\n"
        "Dungeon: %s, Room: %s\n"
        "Player: %s, HP: %s, AP: %s, DP: %s, GP: %s"
    ) % (
        session.dungeon,
        session.room,
        session.player_name,
        session.player_hp,
        session.player_ap,
        session.player_dp,
        session.player_gp
    )
    print

def print_battle_screen():
    print (
        "Monster: %s, HP: %s, AP: %s, DP: %s, GP: %s"
    ) % (
        session.monster_name,
        session.monster_hp,
        session.monster_ap,
        session.monster_dp,
        session.monster_gp
    )
    print

def print_game_over():
    print "GAME OVER!"
    print
    exit(1)

def print_room_description(description):
    print_smoothly(description)
    print

def print_room_options(options):
    options_counter = 1
    for option in options:
        print "%s - %s" % (options_counter, option)
        options_counter += 1
    print

def print_room_notice(notice):
    clear_screen()
    print_smoothly(notice)
    raw_input("Press any key to continue...")

def print_smoothly(message):
    for offset in range(0, len(message)):
        time.sleep(0.04)
        sys.stdout.write(message[offset])
        sys.stdout.flush()
    print

def print_error(error):
    print error
    print

def print_battle_info(info):
    print info
    print

def print_battle_options(options):
    options_counter = 1
    for option in options:
        print "%s - %s" % (options_counter, option)
        options_counter += 1
    print
