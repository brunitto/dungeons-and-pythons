import rooms
import screen
import session
import utils

def render_battle_1():
    session.monster_name = "Ugly Orc"
    turn = "player"
    player_defense = 0
    monster_defense = 0
    time_to_battle = session.monster_hp > 0 and session.player_hp > 0
    while time_to_battle:
        screen.clear_screen()
        screen.print_general_screen()
        screen.print_battle_screen()
        if turn == "player":
            dice = utils.rolls_dice()
            option = ""
            while option != "q":
                screen.print_battle_options([
                    "Attack",
                    "Defend"
                ])
                option = raw_input("Choose an option (q to quit): ")
                if option == "1":
                    if monster_defense > 0:
                        damage = (dice + session.player_ap) - (session.monster_dp + monster_defense)
                    else:
                        damage = (dice + session.player_ap) - session.monster_dp
                    if damage < 0:
                        damage = 0
                    screen.clear_screen()
                    screen.print_general_screen()
                    screen.print_battle_screen()
                    screen.print_battle_info(
                        "Player attacks, rolls %s, dealing %s of damage" % (dice, damage)
                    )
                    raw_input("Press any key to continue...")
                    session.monster_hp = session.monster_hp - damage
                    player_defense = 0
                    turn = "monster"
                    break
                elif option == "2":
                    player_defense = dice + session.player_dp
                    screen.clear_screen()
                    screen.print_general_screen()
                    screen.print_battle_screen()
                    screen.print_battle_info(
                        "Player defends, rolls %s, getting %s of defense" % (dice, player_defense)
                    )
                    raw_input("Press any key to continue...")
                    turn = "monster"
                    break
                else:
                    screen.print_error("Choose a valid option")
        elif turn == "monster":
            dice = utils.rolls_dice()
            option = utils.choose_one(["1", "2"])
            if option == "1":
                if player_defense > 0:
                    damage = (dice + session.monster_ap) - (session.player_dp + player_defense)
                else:
                    damage = (dice + session.monster_ap) - session.player_dp
                if damage < 0:
                    damage = 0
                screen.clear_screen()
                screen.print_general_screen()
                screen.print_battle_screen()
                screen.print_battle_info(
                    "Monster attacks, rolls %s, dealing %s of damage" % (dice, damage)
                )
                raw_input("Press any key to continue...")
                session.player_hp = session.player_hp - damage
                monster_defense = 0
                turn = "player"
            elif option == "2":
                monster_defense = dice + session.monster_dp
                screen.clear_screen()
                screen.print_general_screen()
                screen.print_battle_screen()
                screen.print_battle_info(
                    "Monster defends, rolls %s, getting %s of defense" % (dice, monster_defense)
                )
                raw_input("Press any key to continue...")
                turn = "player"
            else:
                screen.print_error("Unknown monster action")
        else:
            screen.print_error("Unknown turn")

        if session.monster_hp <= 0:
            screen.print_room_notice("You won!")
            screen.print_room_notice("You found %sGP" % session.monster_gp)
            session.player_gp = session.player_gp + session.monster_gp
            rooms.render_room_5()
        elif session.player_hp <= 0:
            screen.print_room_notice("You died!")
            screen.print_game_over()
        else:
            continue
