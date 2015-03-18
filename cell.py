import pygame
import random


class LivingCell(object):
    """Cells should contain life"""

    def __init__(self, coordinate_key, color=pygame.Color(255, 255, 255)):
        super(LivingCell, self).__init__()
        self.xCoord, self.yCoord = coordinate_key
        self.color = color
        self.hasLife = False
        self.willHaveLife = False

    def give_to_neighbors(self):
        return [(self.xCoord - 1, self.yCoord - 1), (self.xCoord, self.yCoord - 1), (self.xCoord + 1, self.yCoord - 1), (self.xCoord - 1, self.yCoord), (self.xCoord + 1, self.yCoord), (self.xCoord - 1, self.yCoord + 1), (self.xCoord, self.yCoord + 1), (self.xCoord + 1, self.yCoord + 1)]

    def get_color(self):
        return self.color

    def draw(self, window_object, width, grid_extremities, xScale=1, yScale=1):
        pygame.draw.rect(window_object, self.color, (((self.xCoord + grid_extremities[0][0]) * width + (self.xCoord + grid_extremities[0][0]) + 1) * xScale, ((self.yCoord + grid_extremities[0][1]) * width + (self.yCoord + grid_extremities[0][1]) + 1) * yScale, width * xScale, width * yScale))

    def change_color(self, color):
        self.color = color

    def get_coordinates(self):
        print "HEEEY!!!~~!~!~!~!"
        return((self.xCoord, self.yCoord))

    def set_coordinates(self, coordinate_pair):
        self.xCoord, self.yCoord = coordinate_pair
