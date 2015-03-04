import pygame
import os
import random
from colors import *
import PlaceholdingClass
import timer


music_enabled = False
music_index_var = 0
MUSIC_HAS_ENDED = 18
check_needs = {"population": False, "entire grid": True, "generate": False}
population = 0
dirty_rects = []
coef = 1. / 4.
pygame.init()
fps_clock = pygame.time.Clock()
window_dimensions = (0, 0)
main_window = pygame.display.set_mode(window_dimensions, pygame.FULLSCREEN)
window_dimensions = (main_window.get_size())
grid_view = pygame.Surface((window_dimensions[0] * (1 - coef), window_dimensions[1]))
mini_view = pygame.Surface((window_dimensions[0] * coef, window_dimensions[1] * coef))
values_view = pygame.Surface((window_dimensions[0] * coef, window_dimensions[1] - window_dimensions[1] * coef))
music_directory = "music/The Caledonian Club/"
songs = [(music_directory + song) for song in os.listdir(music_directory) if song[-3:] in ("mp3", "ogg")]
song_order = random.sample(songs, len(songs))
pygame.mixer.music.load(song_order[len(songs) - 1])
if music_enabled:
    pygame.mixer.music.play()
pygame.mixer.music.set_endevent(MUSIC_HAS_ENDED)
pygame.mixer.music.queue(song_order[music_index_var % 18])
music_index_var += 1
font_obj = pygame.font.Font("freesansbold.ttf", 32)
pop_msg = font_obj.render(str(population), False, colors["light blue"])
pop_msg_rect = pop_msg.get_rect()
pop_msg_rect.topleft = (0, 0)
mousex, mousey, mousex_coord, mousey_coord = 0, 0, 0, 0
mouse_color = colors[random.choice(colors.keys())]
color_msg = font_obj.render(str(mouse_color), False, colors["light blue"])
color_msg_rect = color_msg.get_rect()
color_msg_rect.topleft = (0, 40)
grid_main = [60, 40]
living_cells = {}
living_cells[", "] = PlaceholdingClass.PlaceholdingClass()
grid_view_colors = (colors["grey"], colors["dark grey"])
mini_view_colors = (colors["dark grey"], colors["grey"])
values_view_colors = (colors["light grey"], colors["burnt orange"])
mouse_is_down = False
removing_cells = False
pygame.display.set_caption("Lyfe")
game_timer = timer.Timer(colors["dark green"])
