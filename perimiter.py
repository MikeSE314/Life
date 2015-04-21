import pygame
import random


class Perimiter(object):
    """allow for a place to put a living cell with the mouse"""
    def __init__(self, color):
        super(Perimiter, self).__init__()
        self.cell_set = set() # to change rarely
        self.color = color # to remain constant, maybe. probably will change once.
        self.drawn_perimiter = {} # to change frequently

    def append_cell_no_check(self, x, y):
        self.cell_set.add((x, y))

    def remove_cell(self, x, y):
        if (x, y) in self.cell_set:
            self.cell_set.remove(x, y)


    def determine_with_single_cell_new_perimiter(self, x, y):
        x_coord, y_coord = x, y
        newx = x_coord
        newy = y_coord
        # for the sides
        s0 = str(x_coord) + "," + str(y_coord) + "0" # right
        s1 = str(x_coord) + "," + str(y_coord) + "1" # bottom
        s2 = str(x_coord - 1) + "," + str(y_coord) + "0" # left
        s3 = str(x_coord) + "," + str(y_coord - 1) + "1" # top

        if s3 in self.drawn_perimiter.keys(): # top
            self.drawn_perimiter.pop(s3)
        else:
            self.drawn_perimiter[s3] = ((newx, newy), (newx + 1, newy))

        if s0 in self.drawn_perimiter.keys(): # right
            self.drawn_perimiter.pop(s0)
        else:
            self.drawn_perimiter[s0] = ((newx + 1, newy), (newx + 1, newy + 1))

        if s1 in self.drawn_perimiter.keys(): # bottom
            self.drawn_perimiter.pop(s1)
        else:
            self.drawn_perimiter[s1] = ((newx, newy + 1), (newx + 1, newy + 1))

        if s2 in self.drawn_perimiter.keys(): # left
            self.drawn_perimiter.pop(s2)
        else:
            self.drawn_perimiter[s2] = ((newx, newy), (newx, newy + 1))


    def determine_drawn_perimiter(self):
        self.drawn_perimiter = {}
        for x_coord, y_coord in self.cell_set:
            newx = x_coord
            newy = y_coord
            # for the sides
            s0 = str(x_coord) + "," + str(y_coord) + "0" # right
            s1 = str(x_coord) + "," + str(y_coord) + "1" # bottom
            s2 = str(x_coord - 1) + "," + str(y_coord) + "0" # left
            s3 = str(x_coord) + "," + str(y_coord - 1) + "1" # top

            if s3 in self.drawn_perimiter.keys(): # top
                self.drawn_perimiter.pop(s3)
            else:
                self.drawn_perimiter[s3] = ((newx, newy), (newx + 1, newy))

            if s0 in self.drawn_perimiter.keys(): # right
                self.drawn_perimiter.pop(s0)
            else:
                self.drawn_perimiter[s0] = ((newx + 1, newy), (newx + 1, newy + 1))

            if s1 in self.drawn_perimiter.keys(): # bottom
                self.drawn_perimiter.pop(s1)
            else:
                self.drawn_perimiter[s1] = ((newx, newy + 1), (newx + 1, newy + 1))

            if s2 in self.drawn_perimiter.keys(): # left
                self.drawn_perimiter.pop(s2)
            else:
                self.drawn_perimiter[s2] = ((newx, newy), (newx, newy + 1))

    def append_cell(self, x, y):
        self.append_cell_no_check(x, y)
        self.determine_with_single_cell_new_perimiter(x, y)

    def get_color(self):
        return self.color

    def get_coords(self):
        return self.cell_set

    def draw(self, surface, grid_extremities, scale):
        for pair_of_coordinate_pairs in self.drawn_perimiter.values():
            pygame.draw.line(surface, self.color, (((pair_of_coordinate_pairs[0][0] + grid_extremities[0][0]) * scale + (pair_of_coordinate_pairs[0][0] + grid_extremities[0][0])), ((pair_of_coordinate_pairs[0][1] + grid_extremities[0][1]) * scale + (pair_of_coordinate_pairs[0][1] + grid_extremities[0][1]))), (((pair_of_coordinate_pairs[1][0] + grid_extremities[0][0]) * scale + (pair_of_coordinate_pairs[1][0] + grid_extremities[0][0])), ((pair_of_coordinate_pairs[1][1] + grid_extremities[0][1]) * scale + (pair_of_coordinate_pairs[1][1] + grid_extremities[0][1]))), 3)

    def change_coordinates(self, change):
        for cell in self.cell_set:
            cell = (cell[0] + change[0], cell[1] + change[1])
        self.determine_drawn_perimiter()

    def change_color(self, color_literal):
        self.color = color_literal
