import pygame
from pygame.locals import *
from variables import *
import sys
import os
import random
import math
import types
import cell


def is_cell_at(coordinate_key):
    """return whether or not a cell with given coordinates exists."""
    for cell_key in living_cells.keys():
        if cell_key == coordinate_key:
            return cell_key
    return None


def make_cell_at(color, coordinate_key):
    global t_make_cell_at, prefix
    dirty_rects.append(Rect(coordinate_key, (choice, choice)))
    living_cells[coordinate_key] = cell.LivingCell(coordinate_key, color)
    return


def assure_cell_at(color, coordinate_key):
    """Make certain a cell exists in the list with the coordinates."""
    if is_cell_at(coordinate_key):
        return
    make_cell_at(color, coordinate_key)


def remove_cell_at(coordinate_key):
    """remove the cell at given coordinates"""
    index_key = is_cell_at(coordinate_key)
    if index_key:
        dirty_rects.append(Rect(coordinate_key, (choice, choice)))
        del(living_cells[index_key])


def determine_variables():
    global choice, grid_width, grid_height, mousex_coord, mousey_coord
    global population, check_needs, living_cells
    if check_needs["population"]:
        population = len(living_cells) - 1
        check_needs["population"] = False
    grid_width = (window_dimensions[0] - grid_main[0] - 1) / float(grid_main[0])
    grid_height = (window_dimensions[1] - grid_main[1] - 1) / float(grid_main[1])
    choice = max(grid_width, grid_height)
    mousex_coord = int(mousex / (choice + 1))
    mousey_coord = int(mousey / (choice + 1))


def deal_w_game_time():
    "update the timer, and tell if the game is ready to generate"
    global check_needs, game_timer
    check_needs["generate"] = game_timer.update_portion(math.pi / 10)
    dirty_rects.append(Rect((values_view.get_width() - 60, values_view.get_height() - 60), (50, 50)))
    game_timer.draw(values_view, (values_view.get_width() - 60, values_view.get_height() - 60), 50)


def deal_w_making_deleting_cells():
    "deal with the users' making or deleting of cells"
    global check_needs
    if mouse_is_down:
        if removing_cells:
            remove_cell_at((mousex_coord, mousey_coord))
            check_needs["population"] = True
        else:
            assure_cell_at(mouse_color, ((int(mousex / (choice + 1)), int(mousey / (choice + 1)))))
            check_needs["population"] = True


def care_for_cells():
    global living_cells
    if len(living_cells) > 1:
        xMin = living_cells.keys()[0]
        xMax = xMin
        yMin = living_cells.keys()[1]
        yMax = yMin
        for cell_key in living_cells.keys():
            if cell_key == ", ":
                continue
            xMin = min(xMin, int(cell_key[0]))
            xMax = min(xMax, int(cell_key[0]))
            yMin = min(yMin, int(cell_key[1]))
            yMax = min(yMax, int(cell_key[1]))
        if xMin < 0:
            if yMin < 0:
                for cell_key in living_cells.keys():
                    if cell_key == ", ":
                        continue
                    living_cells[cell_key].set_coordinates((cell_key[0] - xMin, cell_key[1] - yMin))
                living_cells = {(key[0] - xMin, key[1] - yMin) if not key == ", " else key : value for key, value in living_cells.items()}
            else:
                for cell_key in living_cells.keys():
                    if cell_key == ", ":
                        continue
                    living_cells[cell_key].set_coordinates((cell_key[0] - xMin, cell_key[1]))
                living_cells = {(key[0] - xMin, key[1]) if not key == ", " else key : value for key, value in living_cells.items()}
        elif yMin < 0:
            for cell_key in living_cells.keys():
                if cell_key == ", ":
                    continue
                living_cells[cell_key].set_coordinates((cell_key[0], cell_key[1] - yMin))
            living_cells = {(key[0], key[1] - yMin) if not key == ", " else key : value for key, value in living_cells.items()}
        if xMax > choice:
            pass


def generation():
    global check_needs
    check_needs["generate"] = False
    check_needs["population"] = True
    generation_dict = {}
    for cell_key in living_cells.keys():
        if cell_key == ", ":
            continue
        # color of current cell
        color = living_cells[cell_key].get_color()
        for coordinate_pair in living_cells[cell_key].give_to_neighbors():
            # use the color as a counter; more colors means more adjacent cells
            if coordinate_pair in generation_dict.keys():
                generation_dict[coordinate_pair].append(color)
            else:
                generation_dict[coordinate_pair] = [color]
        if not cell_key in generation_dict.keys():
            # make sure there is a place for the last cells
            generation_dict[cell_key] = []
    # then loop back through them
    for cell_key in generation_dict.keys():
        # find how many are adjacet
        len_gen_dict_at_key = len(generation_dict[cell_key])
        # 0 -- 1 or 4 -- 9, kill it
        if len_gen_dict_at_key < 2 or len_gen_dict_at_key > 3:
            remove_cell_at(cell_key)
        # if it's exactly three, it must live
        elif len_gen_dict_at_key == 3:
            # count the number of colors at the coordinates
            count = generation_dict[cell_key].count(max(generation_dict[cell_key], key=generation_dict[cell_key].count))
            # if the count is greater than one, the color is the most amount of colors
            if count > 1:
                color = max(generation_dict[cell_key], key=generation_dict[cell_key].count)
            # otherwise select randomly
            else:
                color = random.choice(generation_dict[cell_key])
            # make a cell there
            assure_cell_at(color, cell_key)
        # if it's exactly two, it doesn't change


def boring_beginning_of_loop_stuff():
    global check_needs, dirty_rects, sound_obj, ultimateIndex
    global t_boring_beginning_of_loop_stuff, prefix, pop_msg, pop_msg_rect
    dirty_rects = []#pop_msg_rect]
    grid_view.fill(grid_view_colors[0])
    mini_view.fill(mini_view_colors[0])
    values_view.fill(values_view_colors[0])
    if check_needs["generate"]:
        generation()


def boring_end_of_loop_stuff():
    dirty_rects = [Rect(1, 1, 1, 1)]
    # pygame.display.update(dirty_rects)
    pygame.display.flip()
    fps_clock.tick(30)


def draw_grid():
    for i in range(grid_main[0]):
        for j in range(grid_main[1]):
            pygame.draw.rect(grid_view, grid_view_colors[1], (i * choice + i + 1, j * choice + j + 1, choice, choice))
            pygame.draw.rect(mini_view, mini_view_colors[1], ((i * choice + i + 1) * coef, (j * choice + j + 1) * coef, choice * coef, choice * coef))


def draw_cells():
    global population, font_obj, pop_msg_rect, color_msg_rect
    for cell_key in living_cells.keys():
        living_cells[cell_key].draw(grid_view, choice)
        living_cells[cell_key].draw(mini_view, choice, coef, coef)
    pop_msg = font_obj.render(str(population), False, colors["light blue"])
    color_msg = font_obj.render(str(reverse_colors[mouse_color]), False, colors["light blue"])
    pop_msg_rect = pop_msg.get_rect()
    color_msg_rect = color_msg.get_rect()
    pop_msg_rect.topleft = (0, 0)
    color_msg_rect.topleft = (0, 40)
    values_view.blit(pop_msg, pop_msg_rect)
    values_view.blit(color_msg, color_msg_rect)


def draw_views():
    main_window.blit(grid_view, (0, 0))
    main_window.blit(mini_view, (window_dimensions[0] - mini_view.get_width(), 0))
    main_window.blit(values_view, (window_dimensions[0] - mini_view.get_width(), mini_view.get_height()))


def check_events():
    global mousex, mousey, mouse_is_down, removing_cells, mouse_color, music_index_var
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
        elif event.type == MOUSEBUTTONDOWN:
            mouse_is_down = True
            removing_cells = bool(is_cell_at((int(mousex / (choice + 1)), int(mousey / (choice + 1)))))
        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            mouse_is_down = False
        elif event.type == KEYDOWN:
            if event.key == (K_y):
                mouse_color = colors["dried blood"]
            if event.key == (K_h):
                mouse_color = colors[random.choice(colors.keys())]
            if event.key == K_LEFT:
                grid_main[0] -= 1
            if event.key == K_RIGHT:
                grid_main[0] += 1
            if event.key == K_UP:
                grid_main[1] -= 1
            if event.key == K_DOWN:
                grid_main[1] += 1
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
        elif event.type == MUSIC_HAS_ENDED:
            pygame.mixer.music.queue(song_order[music_index_var % len(song_order)])
            music_index_var += 1
