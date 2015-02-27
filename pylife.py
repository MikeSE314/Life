import pygame
from pygame.locals import *
from constants import *
import sys
import os
import random
import math
import types
import cell
import time


prefix = ""
with open("debugFile.txt", "w") as debugFile:
    debugFile.writelines(time.strftime('%c') + "\n")

with open("debugFile.txt", "a") as debugFile:
    debugFile.writelines(prefix + str(None) + "\n")

timeIndex = time.time()
ultimateIndex = time.time()

t_is_cell_at = [0, 0]
t_make_cell_at = [0, 0]
t_assure_cell_at = [0, 0]
t_remove_cell_at = [0, 0]
t_determine_variables = [0, 0]
t_deal_w_game_time = [0, 0]
t_deal_w_making_deleting_cells = [0, 0]
t_care_for_cells = [0, 0]
t_generation = [0, 0]
t_boring_beginning_of_loop_stuff = [0, 0]
t_boring_end_of_loop_stuff = [0, 0]
t_draw_grid = [0, 0]
t_draw_cells = [0, 0]
t_draw_views = [0, 0]
t_check_events = [0, 0]


def is_cell_at(x_coord, y_coord=None):
    """return whether or not a cell with given coordinates exists."""
    global t_is_cell_at, prefix
    with open("debugFile.txt", "a") as debugFile:
        debugFile.writelines(prefix + str("Entering is_cell_at!") + "\n")
    prefix += "  "
    timeIndex = time.time()
    if y_coord != None:
        for i in range(len(living_cells)):
            if living_cells[i].get_coordinates() == (x_coord, y_coord):
                prefix = prefix[:-2]
                with open("debugFile.txt", "a") as debugFile:
                    debugFile.writelines(prefix + "is_cell_at(%s, %s) took %s seconds\n"
                                         % (x_coord, y_coord, time.time() -
                                            timeIndex))
                t_is_cell_at[0] += time.time() - timeIndex
                t_is_cell_at[1] += 1
                return i
    else:
        for i in range(len(living_cells)):
            if living_cells[i].get_coordinates() == (x_coord[0], x_coord[1]):
                prefix = prefix[:-2]
                with open("debugFile.txt", "a") as debugFile:
                    debugFile.writelines(prefix + "is_cell_at(%s, %s) took %s seconds\n"
                                         % (x_coord[0], x_coord[1], time.time()
                                            - timeIndex))
                t_is_cell_at[0] += time.time() - timeIndex
                t_is_cell_at[1] += 1
                return i
    prefix = prefix[:-2]
    with open("debugFile.txt", "a") as debugFile:
        debugFile.writelines(prefix + "is_cell_at(%s, %s) took %s seconds\n"
                             % (x_coord, y_coord, time.time() - timeIndex))
    t_is_cell_at[0] += time.time() - timeIndex
    t_is_cell_at[1] += 1
    return None


def make_cell_at(color, x_coord, y_coord=None):
    global t_make_cell_at, prefix
    with open("debugFile.txt", "a") as debugFile:
        debugFile.writelines(prefix + str("Entering make_cell_at!") + "\n")
    prefix += "  "
    timeIndex = time.time()
    if y_coord != None:
        with open("debugFile.txt", "a") as debugFile:
            debugFile.writelines(prefix + str("added cell at %s, %s" %
                                              (x_coord, y_coord)) + "\n")
        dirty_rects.append(Rect((x_coord, y_coord), (choice, choice)))
        living_cells.append(cell.LivingCell(x_coord, y_coord, color))
        prefix = prefix[:-2]
        with open("debugFile.txt", "a") as debugFile:
            debugFile.writelines(prefix + "make_cell_at() took %s seconds\n"
                                 % (time.time() - timeIndex))
        t_make_cell_at[0] += time.time() - timeIndex
        t_make_cell_at[1] += 1
        return
    else:
        with open("debugFile.txt", "a") as debugFile:
            debugFile.writelines(prefix + str("added cell at %s, %s" %
                                              (x_coord[0], x_coord[1])) + "\n")
        dirty_rects.append(Rect((x_coord[0], x_coord[1]), (choice, choice)))
        living_cells.append(cell.LivingCell(x_coord[0], x_coord[1], color))
        prefix = prefix[:-2]
        with open("debugFile.txt", "a") as debugFile:
            debugFile.writelines(prefix + "added_cell_at() took %s seconds\n"
                                 % (time.time() - timeIndex))
        t_make_cell_at[0] += time.time() - timeIndex
        t_make_cell_at[1] += 1


def assure_cell_at(color, x_coord, y_coord=None):
    """Make certain a cell exists in the list with the coordinates."""
    global t_assure_cell_at, prefix
    with open("debugFile.txt", "a") as debugFile:
        debugFile.writelines(prefix + str("Entering assure_cell_at!") + "\n")
    prefix += "  "
    timeIndex = time.time()
    if is_cell_at(x_coord, y_coord):
        prefix = prefix[:-2]
        with open("debugFile.txt", "a") as debugFile:
            debugFile.writelines(prefix + "assure_cell_at() took %s seconds\n"
                                 % (time.time() - timeIndex))
        t_assure_cell_at[0] += time.time() - timeIndex
        t_assure_cell_at[1] += 1
        return
    make_cell_at(color, x_coord, y_coord)
    prefix = prefix[:-2]
    with open("debugFile.txt", "a") as debugFile:
        debugFile.writelines(prefix + str("assure_cell_at() took %s seconds" %
                                          (time.time() - timeIndex)) + "\n")


def remove_cell_at(x_coord, y_coord=None):
    """remove the cell at given coordinates"""
    global t_remove_cell_at, prefix
    with open("debugFile.txt", "a") as debugFile:
        debugFile.writelines(prefix + str("Entering remove_cell_at!") + "\n")
    prefix += "  "
    timeIndex = time.time()
    index = is_cell_at(x_coord, y_coord)
    if index:
        dirty_rects.append(Rect(living_cells[index].get_coordinates(),
                                (choice, choice)))
        del(living_cells[index])
    prefix = prefix[:-2]
    with open("debugFile.txt", "a") as debugFile:
        debugFile.writelines(prefix + str("remove_cell_at() took %s seconds" %
                                          (time.time() - timeIndex)) + "\n")
    t_remove_cell_at[0] += time.time() - timeIndex
    t_remove_cell_at[1] += 1


def determine_variables():
    global choice, grid_width, grid_height, mousex_coord, mousey_coord
    global population, check_needs, living_cells
    global t_determine_variables, prefix
    with open("debugFile.txt", "a") as debugFile:
        debugFile.writelines(prefix + "Entering determine_variables!\n")
    prefix += "  "
    timeIndex = time.time()
    if check_needs["population"]:
        population = len(living_cells) - 1
        check_needs["population"] = False
    grid_width = (window_dimensions[0] -
                  grid_main[0] - 1) / float(grid_main[0])
    grid_height = (window_dimensions[1] -
                   grid_main[1] - 1) / float(grid_main[1])
    #print(grid_width, grid_height)
    choice = max(grid_width, grid_height)
    mousex_coord = int(mousex / (choice + 1))
    mousey_coord = int(mousey / (choice + 1))
    prefix = prefix[:-2]
    with open("debugFile.txt", "a") as debugFile:
        debugFile.writelines(prefix + "determine_variables() took %s seconds\n"
                             % (time.time() - timeIndex))
    t_determine_variables[0] += time.time() - timeIndex
    t_determine_variables[1] += 1


def deal_w_game_time():
    global ready_to_generate, game_timer
    global t_deal_w_game_time, prefix
    with open("debugFile.txt", "a") as debugFile:
        debugFile.writelines(prefix + "Entering deal_w_game_time!\n")
    prefix += "  "
    timeIndex = time.time()
    ready_to_generate = game_timer.update_portion(math.pi / 10)
    dirty_rects.append(Rect((values_view.get_width() - 60,
                                  values_view.get_height() - 60), (50, 50)))
    game_timer.draw(values_view, (values_view.get_width() - 60,
                                  values_view.get_height() - 60), 50)
    prefix = prefix[:-2]
    with open("debugFile.txt", "a") as debugFile:
        debugFile.writelines(prefix + "deal_w_game_time() took %s seconds\n"
                             % (time.time() - timeIndex))
    t_deal_w_game_time[0] += time.time() - timeIndex
    t_deal_w_game_time[1] += 1


def deal_w_making_deleting_cells():
    global check_needs
    global t_deal_w_making_deleting_cells, prefix
    with open("debugFile.txt", "a") as debugFile:
        debugFile.writelines(prefix + "Entering deal_w_making_deleting_cells!\n")
    prefix += "  "
    timeIndex = time.time()
    if mouse_is_down:
        if removing_cells:
            remove_cell_at(mousex_coord, mousey_coord)
            check_needs["population"] = True
        else:
            assure_cell_at(mouse_color, int(mousex / (choice + 1)),
                           int(mousey / (choice + 1)))
            check_needs["population"] = True
    prefix = prefix[:-2]
    with open("debugFile.txt", "a") as debugFile:
        debugFile.writelines(prefix + "deal_w_making_deleting_cells() took %s seconds"
                             % (time.time() - timeIndex))
    t_deal_w_making_deleting_cells[0] += time.time() - timeIndex
    t_deal_w_making_deleting_cells[1] += 1


def care_for_cells():
    global t_care_for_cells, prefix
    with open("debugFile.txt", "a") as debugFile:
        debugFile.writelines(prefix + str("Entering care_for_cells!") + "\n")
    prefix += "  "
    timeIndex = time.time()
    if len(living_cells) > 1:
        xMin = living_cells[1].get_coordinates()[0]
        xMax = xMin
        yMin = living_cells[1].get_coordinates()[1]
        yMax = yMin
        for i in range(len(living_cells) - 1):
            xMin = min(xMin, living_cells[i + 1].get_coordinates()[0])
            xMax = max(xMax, living_cells[i + 1].get_coordinates()[0])
            yMin = min(yMin, living_cells[i + 1].get_coordinates()[1])
            yMax = max(yMax, living_cells[i + 1].get_coordinates()[1])
        if xMin < 0:
            if yMin < 0:
                for i in range(len(living_cells) - 1):
                    living_cells[i + 1].set_coordinates(living_cells[i + 1].
                                                        get_coordinates()[0] -
                                                        xMin, living_cells[i +
                                                        1].get_coordinates()[1]
                                                        - yMin)
            else:
                for i in range(len(living_cells) - 1):
                    living_cells[i + 1].set_coordinates(living_cells[i + 1].
                                                        get_coordinates()[0] -
                                                        xMin, living_cells[i +
                                                        1].
                                                        get_coordinates()[1])
        elif yMin < 0:
            for i in range(len(living_cells) - 1):
                living_cells[i + 1].set_coordinates(living_cells[i + 1].
                                                    get_coordinates()[0],
                                                    living_cells[i + 1]
                                                    .get_coordinates()[1] -
                                                    yMin)
        if xMax > choice:
            pass
    prefix = prefix[:-2]
    with open("debugFile.txt", "a") as debugFile:
        debugFile.writelines(prefix + str("care_for_cells() took %s seconds" %
                                          (time.time() - timeIndex)) + "\n")
    t_care_for_cells[0] += time.time() - timeIndex
    t_care_for_cells[1] += 1


def generation():
    global ready_to_generate, check_needs
    global t_generation, prefix
    with open("debugFile.txt", "a") as debugFile:
        debugFile.writelines(prefix + str("Entering generation!") + "\n")
    count_remove = 0
    count_make = 0
    prefix += "  "
    timeIndex = time.time()
    ready_to_generate = False
    check_needs["population"] = True
    generation_dict = {}
    for living_cell in living_cells:
        if living_cell.give_to_neighbors():
            color = living_cell.give_to_neighbors()[0]
            for coordinate_pair in living_cell.give_to_neighbors()[1]:
                if coordinate_pair in generation_dict.keys():
                    generation_dict[coordinate_pair].append(color)
                else:
                    generation_dict[coordinate_pair] = [color]
            if not living_cell.get_coordinates() in generation_dict.keys():
                generation_dict[living_cell.get_coordinates()] = []
    with open("debugFile.txt", "a") as debugFile:
        debugFile.writelines(prefix + str("Halfway generated at %s seconds!" %
                                          (time.time() - timeIndex)) + "\n")
    for coordinate_pair in generation_dict.keys():
        len_gen_dict = len(generation_dict[coordinate_pair])
        if len_gen_dict < 2 or len_gen_dict > 3:
            count_remove += 1
            remove_cell_at(coordinate_pair)
        elif len_gen_dict == 3:
            count_make += 1
            count = generation_dict[coordinate_pair].count(
                max(generation_dict[coordinate_pair], key=generation_dict[
                    coordinate_pair].count))
            if count > 1:
                color = max(
                    generation_dict[coordinate_pair], key=generation_dict[
                        coordinate_pair].count)
            else:
                color = random.choice(generation_dict[coordinate_pair])
            with open("debugFile.txt", "a") as debugFile:
                debugFile.writelines(prefix + str("Made it to here!") + "\n")
            assure_cell_at(color, coordinate_pair)
    prefix = prefix[:-2]
    with open("debugFile.txt", "a") as debugFile:
        debugFile.writelines(prefix + "generation() took %s seconds; remove: %s, make: %s\n"
                             % (time.time() - timeIndex, count_remove,
                                count_make))
    t_generation[0] += time.time() - timeIndex
    t_generation[1] += 1


def boring_beginning_of_loop_stuff():
    global ready_to_generate, dirty_rects, sound_obj, ultimateIndex
    global t_boring_beginning_of_loop_stuff, prefix, pop_msg, pop_msg_rect
    with open("debugFile.txt", "a") as debugFile:
        debugFile.writelines(prefix + str("Entering boring_beginning_of_loop_stuff!")
                             + "\n")
    prefix += "  "
    timeIndex = time.time()
    with open("debugFile.txt", "a") as debugFile:
        debugFile.writelines(prefix + str(time.time() - ultimateIndex) +
                             "\n\n")
    ultimateIndex = time.time()
    dirty_rects = []#pop_msg_rect]
    grid_view.fill(grid_view_colors[0])
    mini_view.fill(mini_view_colors[0])
    values_view.fill(values_view_colors[0])
    if ready_to_generate:
        generation()
    prefix = prefix[:-2]
    with open("debugFile.txt", "a") as debugFile:
        debugFile.writelines(prefix + "boring_beginning_of_loop_stuff() took %s seconds\n"
                             % (time.time() - timeIndex))
    t_boring_beginning_of_loop_stuff[0] += time.time() - timeIndex
    t_boring_beginning_of_loop_stuff[1] += 1


def boring_end_of_loop_stuff():
    global t_boring_end_of_loop_stuff, prefix, dirty_rects
    with open("debugFile.txt", "a") as debugFile:
        debugFile.writelines(prefix + str("Entering boring_end_of_loop_stuff!")
                                          + "\n")
    prefix += "  "
    timeIndex = time.time()
    if dirty_rects != []:
        with open("debugFile.txt", "a") as debugFile:
            debugFile.writelines(prefix + str(dirty_rects) + "\n")
    dirty_rects = [Rect(1, 1, 1, 1)]
    pygame.display.update(dirty_rects)
    fps_clock.tick(30)
    prefix = prefix[:-2]
    with open("debugFile.txt", "a") as debugFile:
        debugFile.writelines(prefix + "boring_end_of_loop_stuff() took %s seconds\n"
                             % (time.time() - timeIndex))
    t_boring_end_of_loop_stuff[0] += time.time() - timeIndex
    t_boring_end_of_loop_stuff[1] += 1


def draw_grid():
    global t_draw_grid, prefix
    with open("debugFile.txt", "a") as debugFile:
        debugFile.writelines(prefix + str("Entering draw_grid!") + "\n")
    prefix += "  "
    timeIndex = time.time()
    for i in range(grid_main[0]):
        for j in range(grid_main[1]):
            pygame.draw.rect(grid_view, grid_view_colors[1],
                             (i * choice + i + 1, j * choice + j + 1, choice,
                              choice))
            pygame.draw.rect(mini_view, mini_view_colors[1],
                             ((i * choice + i + 1) * coef, (j * choice + j + 1)
                              * coef, choice * coef, choice * coef))
    prefix = prefix[:-2]
    with open("debugFile.txt", "a") as debugFile:
        debugFile.writelines(prefix + str("draw_grid() took %s seconds" %
                                          (time.time() - timeIndex)) + "\n")
    t_draw_grid[0] += time.time() - timeIndex
    t_draw_grid[1] += 1


def draw_cells():
    global population, font_obj, pop_msg_rect
    global t_draw_cells, prefix
    with open("debugFile.txt", "a") as debugFile:
        debugFile.writelines(prefix + str("Entering draw_cells!") + "\n")
    prefix += "  "
    timeIndex = time.time()
    for living_cell in living_cells:
        living_cell.draw(grid_view, choice)
        living_cell.draw(mini_view, choice, coef, coef)
    pop_msg = font_obj.render(str(population), False, colors["light blue"])
    pop_msg_rect = pop_msg.get_rect()
    pop_msg_rect.topleft = (0, 0)
    values_view.blit(pop_msg, pop_msg_rect)
    prefix = prefix[:-2]
    with open("debugFile.txt", "a") as debugFile:
        debugFile.writelines(prefix + str("draw_cells() took %s seconds" %
                                          (time.time() - timeIndex)) + "\n")
    t_draw_cells[0] += time.time() - timeIndex
    t_draw_cells[1] += 1


def draw_views():
    global t_draw_views, prefix
    with open("debugFile.txt", "a") as debugFile:
        debugFile.writelines(prefix + str("Entering draw_views!") + "\n")
    prefix += "  "
    timeIndex = time.time()
    main_window.blit(grid_view, (0, 0))
    main_window.blit(mini_view, (window_dimensions[0] -
                                 mini_view.get_width(), 0))
    main_window.blit(values_view, (window_dimensions[0] -
                                   mini_view.get_width(),
                                   mini_view.get_height()))
    prefix = prefix[:-2]
    with open("debugFile.txt", "a") as debugFile:
        debugFile.writelines(prefix + str("draw_views() took %s seconds" %
                                          (time.time() - timeIndex)) + "\n")
    t_draw_views[0] += time.time() - timeIndex
    t_draw_views[1] += 1


def check_events():
    # global mousex, mousey, removing_cells, mouse_is_down, colors, mouse_color
    # global song_order, music_index_var
    global mousex, mousey, mouse_is_down, removing_cells, mouse_color
    global t_check_events, prefix, music_index_var
    with open("debugFile.txt", "a") as debugFile:
        debugFile.writelines(prefix + str("Entering check_events!") + "\n")
    prefix += "  "
    timeIndex = time.time()
    for event in pygame.event.get():
        if event.type == QUIT:
            with open("debugFile.txt", "a") as debugFile:
                debugFile.writelines(prefix +
                                     str("totals:\nt_is_cell_at: %s\nt_assure_cell_at: %s\nt_remove_cell_at: %s\nt_determine_variables: %s\nt_deal_w_game_time: %s\nt_deal_w_making_deleting_cells: %s\nt_care_for_cells: %s\nt_generation: %s\nt_boring_beginning_of_loop_stuff: %s\nt_boring_end_of_loop_stuff: %s\nt_draw_grid: %s,\nt_draw_cells: %s\nt_draw_views: %s\nt_check_events: %s\n" %
                                         (t_is_cell_at, t_assure_cell_at,
                                          t_remove_cell_at,
                                          t_determine_variables,
                                          t_deal_w_game_time,
                                          t_deal_w_making_deleting_cells,
                                          t_care_for_cells, t_generation,
                                          t_boring_beginning_of_loop_stuff,
                                          t_boring_end_of_loop_stuff,
                                          t_draw_grid, t_draw_cells,
                                          t_draw_views, t_check_events) +
                                          "\n"))

            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
        elif event.type == MOUSEBUTTONDOWN:
            mouse_is_down = True
            removing_cells = bool(is_cell_at(int(mousex / (choice + 1)),
                                             int(mousey / (choice + 1))))
        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            mouse_is_down = False
        elif event.type == KEYDOWN:
            if event.key == (K_y):
                mouse_color = colors["green"]
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
            pygame.mixer.music.queue(song_order[music_index_var %
                                               len(song_order)])
            print song_order[music_index_var % len(song_order)]
            music_index_var += 1
            print song_order[music_index_var % len(song_order)]
    prefix = prefix[:-2]
    with open("debugFile.txt", "a") as debugFile:
        debugFile.writelines(prefix + str("check_events() took %s seconds" %
                                          (time.time() - timeIndex)) + "\n")
    t_check_events[0] += time.time() - timeIndex
    t_check_events[1] += 1
