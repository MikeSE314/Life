import pygame
import random


class LivingCell(object):
    """Cells should contain life"""

    def __init__(self, xCoord, yCoord, color=pygame.Color(255, 255, 255)):
        super(LivingCell, self).__init__()
        self.xCoord = xCoord
        self.yCoord = yCoord
        self.color = color
        self.hasLife = False
        self.willHaveLife = False

    def give_to_neighbors(self):
        return(self.color, [(self.xCoord - 1, self.yCoord - 1),
                            (self.xCoord, self.yCoord - 1),
                            (self.xCoord + 1, self.yCoord - 1),
                            (self.xCoord - 1, self.yCoord),
                            (self.xCoord + 1, self.yCoord),
                            (self.xCoord - 1, self.yCoord + 1),
                            (self.xCoord, self.yCoord + 1),
                            (self.xCoord + 1, self.yCoord + 1)])

    def draw(self, dirtyList, window_object, width, xScale=1, yScale=1):
        dirtyList.append(pygame.draw.rect(window_object, self.color,
                                          ((self.xCoord * width + self.xCoord
                                            + 1) * xScale,
                                           (self.yCoord * width + self.yCoord
                                            + 1) * yScale, width * xScale,
                                           width * yScale)))
        """pygame.draw.rect(mainWindow, colors['black'],
            (i * choice + i + 1, j * choice + j + 1, choice, choice))"""
    def change_color(self, color):
        self.color = color

    def get_coordinates(self):
        return((self.xCoord, self.yCoord))
