import pygame


class Button(object):
    """A button for toggling things"""
    def __init__(self, colors, position, dimensions, message):
        super(Button, self).__init__()
        font_obj = pygame.font.Font("freesansbold.ttf", 32)
        self.colors = colors
        self.position = position
        self.dimensions = dimensions
        self.rect = pygame.Rect(self.position, self.dimensions)
        self.message = font_obj.render(str(message), False, self.colors[0])
        self.msg_rect = self.message.get_rect()
        self.msg_rect.topleft = (self.position[0] + 10, self.position[1] + 3)
        self.toggled = False
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.colors[2] if self.toggled else self.colors[1], self.rect)
        surface.blit(self.message, self.msg_rect)

    def toggle(self):
        self.toggled = True

    def untoggle(self):
        self.toggled = False

