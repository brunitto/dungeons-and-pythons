from sys import exit
import os

# TODO use a module to import common functions
# TODO use lists
# TODO do not use global variables

def room_1():
    clear_screen()
    print_general_screen()
    print """DM: You wake up in a dark and dry room. You look around and it's
    looks like a cell. Right in front of you, close to the cell bars, there is a
    guard, drop dead...

    1 - Scream for help
    2 - Check the guard body
    """

    option = ""
    while option != "q":
        option = raw_input("Choose an option (q to quit): ")
        clear_screen()
        if option == "1":
            print """No one listens to you, you are on your own.
            """
            raw_input("Press any key to continue...")
            room_1()
        elif option == "2":
            print """You find the cell key in his pocket. You leave the cell.
            """
            room_2()
        elif option == "q":
            game_over()
        else:
            print """Choose a valid option!
            """

def room_2():
    clear_screen()
    print_general_screen()
    print """DM: This look like a corridor full of cells. There is an open door
    on the right and a long corridor on the left...

    1 - Enter the open door on the right
    2 - Run through the corridor on the left
    """

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
            print """Choose a valid option!
            """

def room_3():
    clear_screen()
    print_general_screen()
    print """DM: You enter a messy and dry room, there are a interesting desk in
    the corner, covered with papers and a shiny drawer...

    1 - Check the drawer
    2 - Leave the room
    """

    option = ""
    while option != "q":
        option = raw_input("Choose an option (q to quit): ")
        if option == "1":
            print """You found 2GP.
            """
            raw_input("Press any key to continue...")
            room_3()
        elif option == "2":
            room_2()
        elif option == "q":
            game_over()
        else:
            print """Choose a valid option!
            """

def room_4():
    clear_screen()
    print_general_screen()
    print """DM: You enter the main hall. You fell a huge shade coming from
    nowhere, weaving a big axe at you, time to battle...
    """

    print """The battle system is not available!
    """
    raw_input("Press any key to continue...")

    room_5()

def room_5():
    clear_screen()
    print_general_screen()
    print """DM: After a heat battle, you still have energy to run. At the end
    of the hall, there is a dark corridor. When you enter it, you notice that
    part of the floor looks different...

    1 - Check for traps
    2 - Run like there is no tomorrow
    """

    option = ""
    while option != "q":
        option = raw_input("Choose an option (q to quit): ")
        if option == "1":
            print """You find a trap, a clumsy deep hole full of pythons. You jump over it.
            """
            game_over()
        elif option == "2":
            print """You fall in a deep hole and get bitten by the pythons.
            """
            game_over()
        elif option == "q":
            game_over()
        else:
            print """Choose a valid option!
            """

def print_general_screen():
    print """
    DUNGEONS AND PYTHONS
    ----------------------------------------------------------------------------
    Dungeon: --, Room: --
    Player: PLAYER NAME, HP: --, AP: --, DP: --, GP: --
    """

def game_over():
    print """GAME OVER!
    """
    exit(1)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def start():
    room_1()

start()
