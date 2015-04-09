import life
import main_menu

def menu():
    return main_menu.menu()

def game(r_color):
    life.set_color(r_color)
    while True:
        life.boring_beginning_of_loop_stuff()
        life.determine_variables()
        life.draw_grid()
        life.draw_other_things()
        life.deal_w_game_time()
        life.care_for_cells()
        life.draw_views()
        life.check_events()
        life.deal_w_making_deleting_cells()
        life.boring_end_of_loop_stuff()

if __name__ == "__main__":
    game(menu())
