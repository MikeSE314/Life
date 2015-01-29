import pygame, random

class LivingCell(object):
    """Cells should contain life"""
    def __init__(self, xCoord, yCoord):
        super(LivingCell, self).__init__()
        self.xCoord = xCoord
        self.yCoord = yCoord
        self.color = pygame.Color(255, 127, 255)
        self.hasLife = False
        self.willHaveLife = False
    def give_to_neighbors(self, cellList, position):
        return([(xCoord - 1, yCoord - 1), (xCoord, yCoord - 1),
                (xCoord + 1, yCoord - 1), (xCoord - 1, yCoord),
                (xCoord + 1, yCoord), (xCoord - 1, yCoord + 1),
                (xCoord, yCoord + 1), (xCoord + 1, yCoord + 1)])
    def draw(self, window_object, width, scale = 1):
        pygame.draw.rect(window_object, self.color,
                ((self.xCoord * width + self.xCoord + 1) * scale,
                (self.yCoord * width + self.yCoord + 1) * scale, width * scale,
                width * scale))
        """pygame.draw.rect(mainWindow, colors['black'], (i * choice + i + 1,
                    j * choice + j + 1, choice, choice))"""
    def change_color(self, color):
        self.color = color
    def get_coordinates(self):
        return([self.xCoord, self.yCoord])
