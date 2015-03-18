import pygame
import math


class Timer(object):
    """time the game"""
    def __init__(self, color):
        super(Timer, self).__init__()
        self.color = color
        self.portion = 0.

    def draw(self, windowObject, rect):
        pygame.draw.arc(windowObject, self.color, rect, 0, self.portion)

    def update_portion(self, updateAmount):
        self.portion += updateAmount
        if self.portion > 2 * math.pi:
            self.portion -= 2 * math.pi
            return True
        return False
