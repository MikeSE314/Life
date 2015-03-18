import pygame
import random


class PlaceholdingClass(object):
    """this just needs to hold a place for a cell. I think."""
    def __init__(self, *args):
        super(PlaceholdingClass, self).__init__()
        if len(args) > 1 and args[0] == True:
            self.coords = (args[1], args[2])
        if len(args) == 1:
            self.color = args[0]


    def get_coordinates(self):
        return self.coords

    def draw(self, *args):
        pass

    def give_to_neighbors(self):
        return

    def get_color(self):
        return self.color

    def get_borders(self, scale):
        pass

    def change_coordinates(self, change):
        self.coords = (self.coords[0] + change[0], self.coords[1] + change[1])
