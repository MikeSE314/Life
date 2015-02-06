import pyLife

pyLife._game_init_()

while True:
    pyLife.boring_beginning_of_loop_stuff()
    pyLife.determine_variables()
    pyLife.draw_grid()
    pyLife.deal_w_game_time()
    pyLife.draw_cells()
    pyLife.draw_mini_view()
    pyLife.check_events()
    pyLife.deal_w_making_deleting_cells()
    pyLife.boring_end_of_loop_stuff()
