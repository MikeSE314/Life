import pygame
import os
import random
from used_colors import *
import PlaceholdingClass
import timer
import perimiter
import button
import socket


# some important variables
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
data = None
cells_is_True_and_append_is_False = True
pause = False
music_enabled = False
grid_extremities = [[0, 0], [20, 20]]
mouse_is_down = False
removing_cells = False
music_index_var = 0
MUSIC_HAS_ENDED = 18
population = 0
points = 300
coef = 1. / 4.
mouse_pos, mouse_coords = (0, 0), (0, 0)
mouse_use_coords = (mouse_coords[0] - grid_extremities[0][0], mouse_coords[1] - grid_extremities[0][1])
mouse_color = colors[random.choice(colors.keys())]
grid_points_start = [(x + 5, y + 8) for x in range(12) for y in range(12)]
dirty_rects = []
grid_main = [60, 40]
living_cells = {}
living_cells[", "] = PlaceholdingClass.PlaceholdingClass(mouse_color)
# some convenient dictionaries
keys_down = set()
yesterday_down = keys_down
check_needs = {
    "population": True,
    "entire_grid": True,
    "generate": False,
    "grid_dimensions": True,
    "perimiter": True,
    "mouse_color": True,
    "mouse_color_title": True,
    "button_toggles": False,
    "points": True,
    "append_cell": False
}
change_view_by = {
    "zoom_out": False,
    "zoom_in": False,
    "pan_up": False,
    "pan_down": False,
    "pan_right": False,
    "pan_left": False
}
# then initialise pygame
pygame.init()
pygame.display.set_caption("Lyfe")
fps_clock = pygame.time.Clock()
# differing views for the main function of the game
window_dimensions = (0, 0)
main_window = pygame.display.set_mode(window_dimensions, pygame.FULLSCREEN)
window_dimensions = (main_window.get_size())
grid_view = pygame.Surface((window_dimensions[0] * (1 - coef), window_dimensions[1]))
grid_view_dimensions = (grid_view.get_size())
grid_view_rect = grid_view.get_rect()
grid_view_colors = (colors["black"], colors["charcoal"])
mini_view = pygame.Surface((window_dimensions[0] * coef, window_dimensions[1] * coef))
mini_view_dimensions = (mini_view.get_size())
mini_view_rect = pygame.Rect((window_dimensions[0] - mini_view_dimensions[0], 0), mini_view_dimensions)
mini_view_colors = (colors["grey"], colors["black"])
values_view = pygame.Surface((window_dimensions[0] * coef, window_dimensions[1] * (1 - coef)))
values_view_dimensions = (values_view.get_size())
values_view_rect = values_view.get_rect(size=values_view_dimensions, topleft=(window_dimensions[0] - values_view_dimensions[0], window_dimensions[1] - values_view_dimensions[1]))
values_view_colors = (colors["steel blue"], colors["amber"])
menu_view = pygame.Surface((grid_view_dimensions[0] / 2, grid_view_dimensions[1] / 2))
menu_view.set_alpha(230)
menu_view_dimensions = (menu_view.get_size())
menu_view_rect = menu_view.get_rect(size=menu_view_dimensions, topleft=(grid_view_dimensions[0] / 4, grid_view_dimensions[1] / 4))
menu_view_colors = (colors["steel blue"], colors["peach"])
# for the music
music_directory = "music/The Caledonian Club/"
songs = [(music_directory + song) for song in os.listdir(music_directory) if song[-3:] in ("mp3", "ogg")]
song_order = random.sample(songs, len(songs))
music_index_var += 1
# for the font and messages
font_obj = pygame.font.Font("freesansbold.ttf", 32)
pop_msg = font_obj.render("population: " + str(population), True, colors["light blue"])
pop_msg_rect = pop_msg.get_rect()
pop_msg_rect.topleft = (10, 25)
color_msg = font_obj.render("color: " + str(reverse_colors[mouse_color]), True, colors["light blue"])
color_msg_rect = color_msg.get_rect()
color_msg_rect.topleft = (10, 75)
points_msg = font_obj.render("points: " + str(points), True, colors["charcoal"])
points_msg_rect = points_msg.get_rect()
points_msg_rect.topleft = (10, 375)
# then the buttons
menu_buttons = [button.Button((colors["green"], colors["grey"], colors["pink"]), (10, 25), (80, 40), "quit"), button.Button((colors["green"], colors["grey"], colors["pink"]), (10, 75), (160, 40), "unpause")]
buttons = [button.Button((colors["green"], colors["grey"], colors["pink"]), (10, 125), (140, 40), "append"), button.Button((colors["green"], colors["grey"], colors["pink"]), (10, 175), (140, 40), "cells"), button.Button((colors["green"], colors["grey"], colors["pink"]), (10, 225), (140, 40), "pause"), button.Button((colors["green"], colors["grey"], colors["pink"]), (10, 275), (140, 40), "quit"), button.Button((colors["green"], colors["grey"], colors["pink"]), (10, 325), (140, 40), "cheat")]
# these will needs be defined a lot throughout the code
grid_dimensions = (grid_view_dimensions[0] - grid_main[0] - 1) / float(grid_main[0]), (grid_view_dimensions[1] - grid_main[1] - 1) / float(grid_main[1])
choice = max(grid_dimensions[0], grid_dimensions[1])
# define a perimiter
player1_area = perimiter.Perimiter(mouse_color)
for x, y in grid_points_start:
    player1_area.append_cell_no_check(x, y)
# and a timer
game_timer = timer.Timer(colors["dark green"])
