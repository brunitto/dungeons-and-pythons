from sys import exit

# TODO use a module to import common functions
# TODO use lists

def room_1():
    print_general_screen()
    print """
    DM: You wake up in a dark and dry room. You look around and it's looks like
    a cell. Right in front of you, close to the cell bars, there is a guard,
    drop dead...

    1 - Scream for help
    2 - Check the guard body
    """

    option = ""
    while option != "q":
        option = raw_input("Choose an option (\"q\" to quit): ")
        if option == "1":
            print "No one listens to you, you are on your own."
        elif option == "2":
            print "You find the cell key in his pocket. You leave the cell."
            room_2()
        else:
            print "Choose a valid option"

def room_2():
    print_general_screen()
    print """
    DM: This look like a corridor full of cells. There is an open door on the
    right and a long corridor on the left...

    1 - Enter the open door on the right
    2 - Run through the corridor on the left
    """

    option = ""
    while option != "q":
        option = raw_input("Choose an option (\"q\" to quit): ")
        if option == "1":
            room_3()
        elif option == "2":
            room_4()
        else:
            print "Choose a valid option"

def room_3():
    print_general_screen()
    print """
    DM: You enter a messy and dry room, there are a interesting desk in the
    corner, covered with papers and a shiny drawer...

    1 - Check the drawer
    2 - Leave the room
    """

    option = ""
    while option != "q":
        option = raw_input("Choose an option (\"q\" to quit): ")
        if option == "1":
            print "You found 2GP."
        elif option == "2":
            room_2()
        else:
            print "Choose a valid option"

def room_4():
    print_general_screen()
    print """
    DM: You enter the main hall. You fell a huge shade coming from nowhere,
    weaving a big axe at you, time to battle...
    """

    print "The battle system is not available"

    room_5()

def room_5():
    print_general_screen()
    print """
    DM: After a heat battle, you still have energy to run. At the end of the
    hall, there is a dark corridor. When you enter it, you notice that part of
    the floor looks different...

    1 - Check for traps
    2 - Run like there is no tomorrow
    """

    option = ""
    while option != "q":
        option = raw_input("Choose an option (\"q\" to quit): ")
        if option == "1":
            print "You find a trap, a clumsy deep hole full of pythons. You jump over it."
        elif option == "2":
            print "You fall in a deep hole and get bitten by the pythons."
        else:
            print "Choose a valid option"

def print_general_screen():
    print """
    DUNGEONS AND PYTHONS
    ----------------------------------------------------------------------------
    Dungeon: --, Room: --
    Player: PLAYER NAME, HP: --, AP: --, DP: --, GP: --
    """

def game_over():
    print "GAME OVER"
    exit(1)

def start():
    room_1()

start()
