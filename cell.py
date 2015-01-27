import pygame, random

class LivingCell(object):
    """Cells should contain life"""
    def __init__(self, xCoord, yCoord):
        super(LivingCell, self).__init__()
        self.xCoord = xCoord
        self.yCoord = yCoord
        self.color = pygame.Color(255, 255, 255)
        self.hasLife = False
        self.willHaveLife = False
    def get_neighbors(self, cellList, position):
        pass
    def draw(self, window_object, width):
        pygame.draw.rect(window_object, self.color,
                (self.xCoord * width + self.xCoord + 1,
                self.yCoord * width + self.yCoord + 1, width, width))
        """pygame.draw.rect(mainWindow, colors['black'], (i * choice + i + 1,
                    j * choice + j + 1, choice, choice))"""
    def change_color(self, color):
        self.color = color
