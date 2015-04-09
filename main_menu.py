"""main_menu.py
originally created by Micheal Erickson on the 8th of April, 2015
"""

import pygame
import variables
import sys

def menu():
    global main_window, my_color
    has_started = False
    my_color = ""
    variables.color_msg_rect.topleft = (10, 75)
    while True:
        variables.main_window.fill(variables.colors["royal blue"])
        variables.color_msg = variables.font_obj.render("color: " + str(my_color), True, variables.colors["beige"])
        variables.color_msg_rect = variables.color_msg.get_rect()
        variables.main_window.blit(variables.color_msg, variables.color_msg_rect)
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.locals.USEREVENT:
                if event.code == "exit_menu":
                    if my_color in variables.colors.keys():
                        return my_color
            elif event.type == pygame.locals.KEYDOWN:
                if event.key == pygame.locals.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.locals.QUIT))
                elif event.key == pygame.locals.K_RETURN:
                    pygame.event.post(pygame.event.Event(pygame.locals.USEREVENT, code="exit_menu"))
                elif event.key == pygame.locals.K_BACKSPACE:
                    if len(my_color) > 0:
                        my_color = my_color[:-1]
                else:
                    my_color += pygame.key.name(event.key) if not event.key == 32 else " "
        pygame.display.flip()
