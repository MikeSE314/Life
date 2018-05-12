import life
import main_menu
import sys
import socket
import variables

def menu():
    return main_menu.menu()

def game((r_color, name), HOST_IP):
    life.set_color(r_color)
    if HOST_IP == None:
        my_ip = socket.gethostbyname(socket.gethostname())
        variables.server_socket = socket.socket(socket.AF_INET, \
                socket.SOCK_STREAM)
        try:
            variables.server_socket.bind((my_ip, 8001))
        except socket.error as error:
            print("except . . .")
            # Server is already running on port 8001, or PORT
            print('Bind failed. Error Code : %s\nMessage : %s' % (error[0], \
                    error[1]))
            sys.exit()
        life.setup_socket(name, my_ip)
    else:
        print("else . . .")
        life.setup_socket(name, HOST_IP)
    while True:
        print("while . . .")
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
    game(menu(), sys.argv[1] if len(sys.argv) > 1 else None)

