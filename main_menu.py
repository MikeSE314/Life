"""main_menu.py
originally created by Micheal Erickson on the 8th of April, 2015
"""

import pygame
import variables
import sys

def menu():
    global my_color
    background = pygame.image.load("resources/squares.png").convert()
    if background.get_size()[0] < variables.window_dimensions[0]:
        background = pygame.transform.scale(background, \
                (variables.window_dimensions[0], background.get_size()[1] * \
                (variables.window_dimensions[0] / background.get_size()[0])))
    if background.get_size()[1] < variables.window_dimensions[1]:
        background = pygame.transform.scale(background, \
                (background.get_size()[0] * (variables.window_dimensions[1] / \
                background.get_size()[1]), variables.window_dimensions[1]))
    words = pygame.image.load("resources/Conway's War.png")
    has_started = False
    my_color = ""
    my_name = ""
    variables.color_msg_rect.topleft = (variables.window_dimensions[0] / 2 - \
            words.get_size()[0] / 2, variables.window_dimensions[1] / 2 + \
            words.get_size()[1] / 2 - 10)
    det_color = False
    while True:
        variables.main_window.blit(background, (0, 0, \
                variables.window_dimensions[0], \
                variables.window_dimensions[1]))
        variables.main_window.blit(words, (variables.window_dimensions[0] / 2 \
                - words.get_size()[0] / 2, variables.window_dimensions[1] / 2 \
                - words.get_size()[1] / 2))
        if det_color:
            variables.color_msg = variables.font_obj.render("color: " + \
                    str(my_color), True, variables.colors["beige"])
            variables.color_msg_rect = variables.color_msg.get_rect()
            variables.main_window.blit(variables.color_msg, \
                    (variables.window_dimensions[0] / 2 - words.get_size()[0] \
                    / 2 + 20, variables.window_dimensions[1] / 2 + \
                    words.get_size()[1] / 2 - 20))
            if str(my_color) in variables.colors.keys():
                pygame.draw.rect(variables.main_window, \
                        variables.colors[str(my_color)], \
                        (variables.window_dimensions[0] / 2 - \
                        words.get_size()[0] / 2 + 20, \
                        variables.window_dimensions[1] / 2 + \
                        words.get_size()[1] / 2 + 20, 100, 30))
        else:
            variables.color_msg = variables.font_obj.render("name: " + \
                    str(my_name), True, variables.colors["beige"])
            variables.color_msg_rect = variables.color_msg.get_rect()
            variables.main_window.blit(variables.color_msg, \
                    (variables.window_dimensions[0] / 2 - words.get_size()[0] \
                    / 2 + 20, variables.window_dimensions[1] / 2 + \
                    words.get_size()[1] / 2 - 20))
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.locals.USEREVENT:
                if event.code == "exit_menu":
                    if det_color:
                        if my_color in variables.colors.keys():
                            variables.main_window.fill(\
                                    variables.colors["black"])
                            return (my_color, my_name)
                    else:
                        det_color = True
            elif event.type == pygame.locals.KEYDOWN:
                if event.key == pygame.locals.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.locals.QUIT))
                elif event.key == pygame.locals.K_RETURN:
                    pygame.event.post(pygame.event.Event(\
                            pygame.locals.USEREVENT, code="exit_menu"))
                elif event.key == pygame.locals.K_BACKSPACE:
                    if det_color:
                        if len(my_color) > 0:
                            my_color = my_color[:-1]
                    else:
                        if len(my_name) > 0:
                            my_name = my_name[:-1]
                elif event.key == pygame.locals.K_LSHIFT or event.key == \
                        pygame.locals.K_RSHIFT:
                    pass
                else:
                    if det_color:
                            my_color += pygame.key.name(event.key) if not \
                                    event.key == 32 else " "
                    else:
                        if pygame.key.get_mods() & pygame.locals.KMOD_SHIFT:
                            my_name += pygame.key.name(event.key).upper() if \
                                    not event.key == 32 else " "
                        else:
                            my_name += pygame.key.name(event.key) if not \
                                    event.key == 32 else " "
        pygame.display.flip()
