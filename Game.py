import pygame
from pygame.locals import *

import colors

class Game:
    def __init__(self, width=0, height=0, title="Pygame"):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((width, height), RESIZABLE)
        pygame.display.set_caption(title)
        self.colors = colors.colors
        self.mouse_pos = (0, 0)
        self.running = False
        self.mouse_buttons = set()
        self.keys = set()
        self.game_objects = []

    def run(self):
        self.running = True
        while self.running:
            self.input()
            self.update()
            self.draw()
            self.clock.tick(30)

    def input(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == MOUSEMOTION:
                self.mouse_pos = event.pos
            elif event.type == MOUSEBUTTONUP:
                self.mouse_pos = event.pos
                self.mouse_buttons.add(event.button)
            elif event.type == MOUSEBUTTONUP:
                self.mouse_pos = event.pos
                if event.button in self.mouse_buttons:
                    self.mouse_buttons.remove(event.button)
            elif event.type == KEYDOWN:
                self.keys.add(event.key)
            elif event.type == KEYUP:
                if event.key in self.keys:
                    self.keys.remove(event.key)

    def update(self):
        if K_ESCAPE in self.keys:
            self.running = False
        for game_object in self.game_objects:
            game_object.update()
        pygame.display.set_caption(str(self.mouse_pos))

    def draw(self):
        self.window.fill(self.colors["wheat"])
        for game_object in self.game_objects:
            game_object.draw(self.window)
        pygame.display.update()

    def cleanup(self):
        pygame.quit()

