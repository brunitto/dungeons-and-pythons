import battles
import screen
import session
import utils

def render_room_1():
    session.dungeon = "01"
    session.room = "01"
    screen.clear_screen()
    screen.print_general_screen()
    screen.print_room_description(
        "You wake up in a dark and dry room. You look around and it's looks\n"
        "like a cell. Right in front of you, close to the cell bars, there is\n"
        "a guard, drop dead..."
    )
    screen.print_room_options([
        "Scream for help",
        "Check the guard's body"
    ])

    option = ""
    while option != "q":
        option = raw_input("Choose an option (q to quit): ")
        if option == "1":
            screen.clear_screen()
            screen.print_room_notice("No one listens to you, you are on your own.")
            render_room_1()
        elif option == "2":
            screen.clear_screen()
            screen.print_room_notice(
                "You find the cell key in his pocket. You leave the cell"
            )
            render_room_2()
        elif option == "q":
            screen.print_game_over()
        else:
            screen.print_error("Choose a valid option")

def render_room_2():
    session.dungeon = "01"
    session.room = "02"
    screen.clear_screen()
    screen.print_general_screen()
    screen.print_room_description(
        "This look like a corridor full of cells. There is an open door on\n"
        "the right and a long corridor on the left"
    )
    screen.print_room_options([
        "Enter the open door on the right",
        "Run through the corridor on the left"
    ])

    option = ""
    while option != "q":
        option = raw_input("Choose an option (q to quit): ")
        if option == "1":
            render_room_3()
        elif option == "2":
            render_room_4()
        elif option == "q":
            screen.print_game_over()
        else:
            screen.print_error("Choose a valid option")

def render_room_3():
    session.dungeon = "01"
    session.room = "03"
    screen.clear_screen()
    screen.print_general_screen()
    screen.print_room_description(
        "You enter a messy and dry room, there are an interesting desk in the\n"
        "corner, covered with papers and a shiny drawer"
    )
    screen.print_room_options([
        "Check the drawer",
        "Leave the room"
    ])

    option = ""
    while option != "q":
        option = raw_input("Choose an option (q to quit): ")
        if option == "1":
            screen.clear_screen()
            if session.player_found_gp_in_room_2:
                screen.print_room_notice("The drawer is empty")
            else:
                session.player_gp = session.player_gp + 2
                session.player_found_gp_in_room_2 = True
                screen.print_room_notice("You found 2GP")
            render_room_3()
        elif option == "2":
            render_room_2()
        elif option == "q":
            screen.print_game_over()
        else:
            screen.print_error("Choose a valid option")

def render_room_4():
    session.dungeon = "01"
    session.room = "04"
    screen.clear_screen()
    screen.print_general_screen()
    screen.print_room_description(
        "You enter the main hall. You fell a huge shade coming from nowhere\n"
        "weaving a big axe at you. TIME TO BATTLE!"
    )
    raw_input("Press any key to continue...")
    battles.render_battle_1()

def render_room_5():
    session.dungeon = "01"
    session.room = "05"
    screen.clear_screen()
    screen.print_general_screen()
    screen.print_room_description(
        "After a heat battle, you still have energy to run. At the end of the\n"
        "hall, there is a dark corridor. When you enter it, you notice that\n"
        "part of the floor looks different"
    )
    screen.print_room_options([
        "Check for traps",
        "Run like there is no tomorrow"
    ])

    option = ""
    while option != "q":
        option = raw_input("Choose an option (q to quit): ")
        if option == "1":
            screen.clear_screen()
            screen.print_room_notice(
                "You find a trap, a clumsy deep hole full of pythons. You jump "
                "over it."
            )
            screen.print_game_over()
        elif option == "2":
            screen.clear_screen()
            screen.print_room_notice(
                "You fall in a deep hole and get bitten by the pythons."
            )
            screen.print_game_over()
        elif option == "q":
            screen.print_game_over()
        else:
            screen.print_error("Choose a valid option")
