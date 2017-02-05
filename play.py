import battles
import rooms
import screen
import session
import utils

def start():
    screen.clear_screen()
    print "Welcome to Dungeons and Pythons\n"
    session.player_name = raw_input("What's your name? ")
    rooms.render_room_1()

start()
