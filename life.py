import pygame
from pygame.locals import *
from variables import *
import sys
import os
import random
import math
import types
import socket
import cell
import perimiter


def setup_socket(name, HOST_IP):
    global client_socket, data
    print socket.gethostbyname(socket.gethostname())
    try:
        client_socket.connect((HOST_IP, 8001))
    except Exception as error:
        print("Could not connect to the server: %s" % error)
    data = client_socket.recv(4096)
    client_socket.send("NAME|%s", name)


def set_color(color):
    mouse_color = colors[color]
    player1_area.change_color(mouse_color)
    living_cells[", "].change_color(mouse_color)


def is_cell_at(coordinate_key):
    """return whether or not a cell with given coordinates exists."""
    for cell_key in living_cells.keys():
        if cell_key == coordinate_key:
            return cell_key
    return None


def make_cell_at(color, coordinate_key):
    dirty_rects.append(Rect(coordinate_key, (choice, choice)))
    living_cells[coordinate_key] = cell.LivingCell(coordinate_key, color)
    return True


def assure_cell_at(color, coordinate_key):
    """Make certain a cell exists in the list with the coordinates."""
    return make_cell_at(color, coordinate_key) if not is_cell_at(coordinate_key) else False


def remove_cell_at(coordinate_key, remove_color=None):
    """remove the cell at given coordinates"""
    index_key = is_cell_at(coordinate_key)
    if index_key:
        if remove_color in (None, living_cells[index_key].get_color()):
            dirty_rects.append(Rect(coordinate_key, (choice, choice)))
            del(living_cells[index_key])
            return True
    return False


def determine_variables():
    global choice, grid_width, grid_height, mouse_coords, mouse_pos, keys_down, population, check_needs, living_cells, pop_msg, pop_msg_rect, color_msg, color_msg_rect, points_msg, points_msg_rect, grid_dimensions, mouse_color, points, grid_extremities, mouse_use_coords, pause, cells_is_True_and_append_is_False
    choice = max(grid_dimensions[0], grid_dimensions[1])
    mouse_coords = int(mouse_pos[0] / (choice + 1)), int(mouse_pos[1] / (choice + 1))
    mouse_use_coords = (mouse_coords[0] - grid_extremities[0][0], mouse_coords[1] - grid_extremities[0][1])
    if "up" in keys_down:
        change_view_by["pan_up"] = True
    if "down" in keys_down:
        change_view_by["pan_down"] = True
    if "left" in keys_down:
        change_view_by["pan_left"] = True
    if "right" in keys_down:
        change_view_by["pan_right"] = True
    if "m4" in keys_down:
        change_view_by["zoom_out"] = True
    if "m5" in keys_down:
        change_view_by["zoom_in"] = True
    if check_needs["button_toggles"]:
        check_needs["button_toggles"] = False
        for button in buttons:
            if button.rect.collidepoint((mouse_pos[0] - values_view_rect.left, mouse_pos[1] - values_view_rect.top)) and "m1" in keys_down:
                button.toggle()
                if button.raw_message == "append":
                    cells_is_True_and_append_is_False = False
                elif button.raw_message == "cells":
                    cells_is_True_and_append_is_False = True
                elif button.raw_message == "cheat":
                    points += 500
                    check_needs["points"] = True
                elif button.raw_message == "quit":
                    pygame.event.post(pygame.event.Event(QUIT))
                elif button.raw_message == "pause":
                    pause = not pause
            else:
                button.untoggle()
        if pause:
            for button in menu_buttons:
                if button.rect.collidepoint((mouse_pos[0] - menu_view_rect.left, mouse_pos[1] - menu_view_rect.top)) and "m1" in keys_down:
                    button.toggle()
                    if button.raw_message == "quit":
                        pygame.event.post(pygame.event.Event(QUIT))
                    elif button.raw_message == "unpause":
                        pause = not pause
                else:
                    button.untoggle()
    if check_needs["generate"]:
        check_needs["generate"] = False
        generation()
        check_needs["population"] = True
    if check_needs["points"]:
        check_needs["points"] = False
        points_msg = font_obj.render("points: " + str(points), True, colors["charcoal"])
        # points_msg_rect = points_msg.get_rect()
        # points_msg_rect.topleft = (10, 375)
    if check_needs["mouse_color"]:
        check_needs["mouse_color"] = False
        mouse_color = living_cells[is_cell_at(mouse_use_coords) if is_cell_at(mouse_use_coords) else ", "].get_color()
        check_needs["mouse_color_title"] = True
    if check_needs["mouse_color_title"]:
        check_needs["mouse_color_title"] = False
        color_msg = font_obj.render("color: " + str(reverse_colors[mouse_color]), True, mouse_color)
        color_msg_rect = color_msg.get_rect()
        color_msg_rect.topleft = (10, 75)
    if change_view_by["pan_up"]:
        change_view_by["pan_up"] = False
        grid_extremities[0][1] += 1
        grid_extremities[1][1] += 1
        check_needs["grid_dimensions"] = True
    if change_view_by["pan_down"]:
        change_view_by["pan_down"] = False
        grid_extremities[0][1] -= 1
        grid_extremities[1][1] -= 1
        check_needs["grid_dimensions"] = True
    if change_view_by["pan_left"]:
        change_view_by["pan_left"] = False
        grid_extremities[0][0] += 1
        grid_extremities[1][0] += 1
        check_needs["grid_dimensions"] = True
    if change_view_by["pan_right"]:
        change_view_by["pan_right"] = False
        grid_extremities[0][0] -= 1
        grid_extremities[1][0] -= 1
        check_needs["grid_dimensions"] = True
    if change_view_by["zoom_in"]:
        change_view_by["zoom_in"] = False
        print "hello"
        grid_extremities[0][0] -= 1
        grid_extremities[0][1] -= 1
        grid_extremities[1][0] -= 1
        grid_extremities[1][1] -= 1
    if change_view_by["zoom_out"]:
        change_view_by["zoom_out"] = False
        print "heyo"
        grid_extremities[1][0] += 1
        grid_extremities[1][1] += 1
    if check_needs["append_cell"]:
        check_needs["append_cell"] = False
        if points >= 27:
            player1_area.append_cell(mouse_use_coords[0], mouse_use_coords[1])
            points -= 27
            check_needs["perimiter"] = True
            check_needs["points"] = True
    if check_needs["grid_dimensions"]:
        check_needs["grid_dimensions"] = False
        grid_dimensions = (grid_view_dimensions[0] - grid_main[0] - 1) / float(grid_main[0]), (grid_view_dimensions[1] - grid_main[1] - 1) / float(grid_main[1])
        check_needs["perimiter"] = True
    if check_needs["perimiter"]:
        check_needs["perimiter"] = False
        player1_area.determine_drawn_perimiter()
    if check_needs["population"]:
        check_needs["population"] = False
        population = len(living_cells) - 1
        pop_msg = font_obj.render("population: " + str(population), True, colors["black"])
        pop_msg_rect = pop_msg.get_rect()
        pop_msg_rect.topleft = (10, 25)


def menu():
    global colors
    pygame.draw.rect(grid_view, colors["pink"], (30, 30, 30, 30))


def deal_w_game_time():
    "update the timer, and tell if the game is ready to generate"
    global check_needs, game_timer, pause
    if not pause:
        check_needs["generate"] = game_timer.update_portion(math.pi / 10)
        # dirty_rects.append(Rect((values_view.get_width() - 60, values_view.get_height() - 60), (50, 50)))
        # timer_rect = Rect(values_view_dimensions[0] - 60, values_view_dimensions[1] - 60, 50, 50)
        game_timer.draw(values_view, Rect(values_view.get_width() - 60, values_view.get_height() - 60, 50, 50))


def deal_w_making_deleting_cells():
    "deal with the users' making or deleting of cells"
    global check_needs, points, pause, cells_is_True_and_append_is_False
    if not pause:
        if "m1" in keys_down:
            if cells_is_True_and_append_is_False:
                if grid_view_rect.collidepoint(mouse_pos) and mouse_use_coords in player1_area.get_coords() and mouse_color == player1_area.get_color():
                    check_needs["population"] = True
                    if removing_cells:
                        if remove_cell_at(mouse_use_coords, mouse_color):
                            points += 13
                            check_needs["points"] = True
                    else:
                        if grid_view_rect.collidepoint(mouse_pos):
                            if points >= 17:
                                if assure_cell_at(mouse_color, mouse_use_coords):
                                    points -= 17
                                    check_needs["points"] = True
            else:
                if grid_view_rect.collidepoint(mouse_pos) and mouse_use_coords not in player1_area.get_coords() and mouse_color == player1_area.get_color():
                    check_needs["append_cell"] = True



def care_for_cells():
    global living_cells
    # if len(living_cells) > 1:
    #     xMin = living_cells.keys()[0]
    #     xMax = xMin
    #     yMin = living_cells.keys()[1]
    #     yMax = yMin
    #     for cell_key in living_cells.keys():
    #         if cell_key == ", ":
    #             continue
    #         xMin = min(xMin, int(cell_key[0]))
    #         xMax = min(xMax, int(cell_key[0]))
    #         yMin = min(yMin, int(cell_key[1]))
    #         yMax = min(yMax, int(cell_key[1]))
    #     if xMin < 0:
    #         if yMin < 0:
    #             for cell_key in living_cells.keys():
    #                 if cell_key == ", ":
    #                     continue
    #                 living_cells[cell_key].set_coordinates((cell_key[0] - xMin, cell_key[1] - yMin))
    #             living_cells = {(key[0] - xMin, key[1] - yMin) if not key == ", " else key : value for key, value in living_cells.items()}
    #             player1_area.change_coordinates((-xMin, -yMin), choice)
    #         else:
    #             for cell_key in living_cells.keys():
    #                 if cell_key == ", ":
    #                     continue
    #                 living_cells[cell_key].set_coordinates((cell_key[0] - xMin, cell_key[1]))
    #             living_cells = {(key[0] - xMin, key[1]) if not key == ", " else key : value for key, value in living_cells.items()}
    #             player1_area.change_coordinates((-xMin, 0), choice)
    #     elif yMin < 0:
    #         for cell_key in living_cells.keys():
    #             if cell_key == ", ":
    #                 continue
    #             living_cells[cell_key].set_coordinates((cell_key[0], cell_key[1] - yMin))
    #         living_cells = {(key[0], key[1] - yMin) if not key == ", " else key : value for key, value in living_cells.items()}
    #         player1_area.change_coordinates((0, -yMin), choice)
    #     if xMax > choice:
    #         pass
    pass


def generation():
    global check_needs, points, pause
    if not pause:
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
                if remove_cell_at(cell_key):
                    points -= 2
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
                if assure_cell_at(color, cell_key):
                    points += 3
                    check_needs["points"] = True
            # if it's exactly two, it doesn't change


def boring_beginning_of_loop_stuff():
    global check_needs, dirty_rects, sound_obj, ultimateIndex
    dirty_rects = []
    menu_view.fill(menu_view_colors[0])
    grid_view.fill(grid_view_colors[0])
    mini_view.fill(mini_view_colors[0])
    values_view.fill(values_view_colors[0])


def boring_end_of_loop_stuff():
    dirty_rects = [Rect(1, 1, 1, 1)]
    pygame.display.flip()
    fps_clock.tick(30)


def draw_grid():
    for j in range(grid_main[1] + 1):
        pygame.draw.line(grid_view, grid_view_colors[1], (0, j * choice + j), (grid_view_dimensions[0], j * choice + j))
    for i in range(grid_main[0] + 1):
        pygame.draw.line(grid_view, grid_view_colors[1], (i * choice + i, 0), (i * choice + i, grid_view_dimensions[1]))


def draw_other_things():
    global population, font_obj, pop_msg, pop_msg_rect, color_msg, color_msg_rect, buttons, menu_buttons, points_msg, points_msg_rect, grid_extremities
    for cell_key in living_cells.keys():
        living_cells[cell_key].draw(grid_view, choice, grid_extremities)
        living_cells[cell_key].draw(mini_view, choice, grid_extremities, coef, coef)
    player1_area.draw(grid_view, grid_extremities, choice)
    for button in buttons:
        button.draw(values_view)
    for button in menu_buttons:
        button.draw(menu_view)
    values_view.blit(pop_msg, pop_msg_rect)
    values_view.blit(color_msg, color_msg_rect)
    values_view.blit(points_msg, points_msg_rect)


def draw_views():
    global pause
    if pause:
        grid_view.blit(menu_view, menu_view_rect)
    main_window.blit(grid_view, (0, 0))
    main_window.blit(mini_view, mini_view_rect)
    main_window.blit(values_view, values_view_rect)


def check_events():
    global mouse_pos, removing_cells, mouse_color, music_index_var, keys_down
    data = client_socket.recv(RECV_BUFFER)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mouse_pos = event.pos
        elif event.type == MOUSEBUTTONDOWN:
            keys_down.add("m" + str(event.button))
            if event.button == 4:
                change_view_by["zoom_out"] = True
            if event.button == 5:
                change_view_by["zoom_in"] = True
                print "yolo"
            mouse_pos = event.pos
            check_needs["button_toggles"] = True
            removing_cells = bool(is_cell_at(mouse_use_coords))
        elif event.type == MOUSEBUTTONUP:
            keys_down.remove("m" + str(event.button))
            mouse_pos = event.pos
            check_needs["button_toggles"] = True
        elif event.type == KEYDOWN:
            keys_down.add(pygame.key.name(event.key))
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
        elif event.type == KEYUP:
            if pygame.key.name(event.key) in keys_down:
                keys_down.remove(pygame.key.name(event.key))
        elif event.type == MUSIC_HAS_ENDED:
            pygame.mixer.music.queue(song_order[music_index_var % len(song_order)])
            music_index_var += 1
