import sys, random, math

import pygame
import cell
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

windowDimensions = (0, 0)

mainWindow = pygame.display.set_mode(windowDimensions, pygame.FULLSCREEN)
windowDimensions = (mainWindow.get_size())
miniView = pygame.Surface((windowDimensions[0] / 6, windowDimensions[1] / 6))
pygame.display.set_caption('Lyfe')

colors = {
'darkRed': pygame.Color(127, 0, 0),
'red': pygame.Color(255, 0, 0),
'lightRed': pygame.Color(255, 127, 127),

'darkGreen': pygame.Color(0, 127, 0),
'green': pygame.Color(0, 255, 0),
'lightGreen': pygame.Color(127, 255, 127),

'darkYellow': pygame.Color(127, 127, 0),
'yellow': pygame.Color(255, 255, 0),
'lightYellow': pygame.Color(255, 255, 127),

'darkBlue': pygame.Color(0, 0, 127),
'blue': pygame.Color(0, 0, 255),
'lightBlue': pygame.Color(127, 127, 255),

'darkMagenta': pygame.Color(127, 0, 127),
'magenta': pygame.Color(255, 0, 255),
'lightMagenta': pygame.Color(255, 127, 255),

'darkCyan': pygame.Color(0, 127, 127),
'cyan': pygame.Color(0, 255, 255),
'lightCyan': pygame.Color(127, 255, 255),

'black': pygame.Color(0, 0, 0),
'grey': pygame.Color(127, 127, 127),
'white': pygame.Color(255, 255, 255)
}

mousex, mousey = 0, 0

gridMain = [20, 20]
livingCells = []
livingCells.append(cell.LivingCell(0, 0))
livingCells.append(cell.LivingCell(0, 1))
livingCells.append(cell.LivingCell(0, 2))
livingCells.append(cell.LivingCell(1, 2))
livingCells.append(cell.LivingCell(2, 1))
portion_of_step = 0.

while True:
    mainWindow.fill(colors['grey'])
    miniView.fill(colors['black'])
    portion_of_step += math.pi / 10 * random.random()
    if portion_of_step > 2 * math.pi:
        portion_of_step = 0
    width = (windowDimensions[0] - gridMain[0] - 1) / float(gridMain[0])
    height = (windowDimensions[1] - gridMain[1] - 1) / float(gridMain[1])
    choice = min(width, height)
    for i in range(gridMain[0]):
        for j in range(gridMain[1]):
            pygame.draw.rect(mainWindow, colors['black'], (i * choice + i + 1,
                    j * choice + j + 1, choice, choice))
            pygame.draw.rect(miniView, colors['darkCyan'],
                    ((i * choice + i + 1) / 6 , (j * choice + j + 1) / 6,
                    choice / 6, choice / 6))
    mainWindow.blit(miniView, (windowDimensions[0] * .9, 10))

    pygame.draw.arc(mainWindow, colors['green'], pygame.Rect(choice * 9,
            choice * 9, choice, choice), 0, portion_of_step,
            int(0))

    for livingCell in livingCells:
        livingCell.draw(mainWindow, choice)
        livingCell.draw(miniView, choice / 6)

    '''gridMain[int(random.random() * len(gridMain))][int(random.random() * len(
                        gridMain[0]))].change_color(colors[random.choice(colors.keys())])
            '''
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            gridMain[random.choice([0, 1])] += 1
        elif event.type == KEYDOWN:
            if event.key in (K_LEFT, K_RIGHT, K_UP, K_DOWN):
                pass
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
    pygame.display.flip()
    #pygame.display.update()
    fpsClock.tick(30)
