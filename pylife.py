import pygame
from pygame.locals import *
import sys, random, math, types
import cell, PlaceholdingClass

def assure_cell_at(color, xCoord, yCoord = None):
    """Make certain a cell exists in the list with the coordinates."""
    for livingCell in livingCells:
        if yCoord:
            if livingCell.get_coordinates() == (xCoord, yCoord):
                return True
        elif livingCell.get_coordinates() == (xCoord[0], xCoord[1]):
            return True
    if yCoord:
        livingCells.append(cell.LivingCell(xCoord, yCoord, color))
        return False
    else:
        livingCells.append(cell.LivingCell(xCoord[0], xCoord[1], color))
        return False

def is_cell_at(xCoord, yCoord = None):
    """return whether or not a cell with given coordinates exists."""
    for livingCell in livingCells:
        if yCoord:
            if livingCell.get_coordinates() == (xCoord, yCoord):
                return True
        elif livingCell.get_coordinates() == (xCoord[0], xCoord[1]):
                return True
    return False

def remove_cell_at(xCoord, yCoord = None):
    """remove the cell at given coordinates"""
    index = None
    for i in range(len(livingCells)):
        if yCoord:
            if livingCells[i].get_coordinates() == (xCoord, yCoord):
                index = i
        elif livingCells[i].get_coordinates() == (xCoord[0], xCoord[1]):
            index = i
    if index:
        del(livingCells[index])

def determine_variables():
    global choice, width, height, mousexCoord, mouseyCoord
    width = (windowDimensions[0] - gridMain[0] - 1) / float(gridMain[0])
    height = (windowDimensions[1] - gridMain[1] - 1) / float(gridMain[1])
    choice = max(width, height)
    mousexCoord = int(mousex / (choice + 1))
    mouseyCoord = int(mousey / (choice + 1))

def deal_w_game_time():
    global portion_of_step, readyToGenerate
    portion_of_step += math.pi / 10
    if portion_of_step > 2 * math.pi:
        readyToGenerate = True
        portion_of_step = 0
    pygame.draw.arc(mainWindow, colors['darkGreen'], pygame.Rect((
        windowDimensions[0] - 60, windowDimensions[1] - 60), (50, 50)),
        portion_of_step * 2, 3 * portion_of_step)

def deal_w_making_deleting_cells():
    if mouseIsDown:
        if removingCells:
            remove_cell_at(mousexCoord, mouseyCoord)
        else:
            color = colors['red']
            assure_cell_at(color, int(mousex / (choice + 1)), int(mousey / (
                choice + 1)))

def generation():
    global readyToGenerate
    readyToGenerate = False
    generationDict = {}
    for livingCell in livingCells:
        if livingCell.give_to_neighbors():
            color = livingCell.give_to_neighbors()[0]
            for coordinatePair in livingCell.give_to_neighbors()[1]:
                if coordinatePair in generationDict.keys():
                    generationDict[coordinatePair].append(color)
                else:
                    generationDict[coordinatePair] = [color]
            if not livingCell.get_coordinates() in generationDict.keys():
                generationDict[livingCell.get_coordinates()] = []
    for coordinatePair in generationDict.keys():
        if is_cell_at(coordinatePair):
            if(len(generationDict[coordinatePair]) < 2 or len(generationDict[
                coordinatePair]) > 3):
                remove_cell_at(coordinatePair)
        elif len(generationDict[coordinatePair]) == 3:
            count = generationDict[coordinatePair].count(max(generationDict[
                coordinatePair], key = generationDict[coordinatePair].count))
            if count > 1:
                color = max(generationDict[coordinatePair], key =
                    generationDict[coordinatePair].count)
            else:
                color = random.choice(generationDict[coordinatePair])
            assure_cell_at(color, coordinatePair)

def boring_beginning_of_loop_stuff():
    global readyToGenerate
    pygame.transform.flip(mainWindow, True, True)
    mainWindow.fill(mainWindowColors[0])
    miniView.fill(miniViewColors[0])
    if readyToGenerate:
        generation()

def boring_end_of_loop_stuff():
    pygame.transform.flip(mainWindow, True, True)
    pygame.transform.flip(miniView, True, True)
    pygame.display.update()
    fpsClock.tick(30)

def draw_grid():
    for i in range(gridMain[0]):
        for j in range(gridMain[1]):
            pygame.draw.rect(mainWindow, mainWindowColors[1], (i * choice + i +
                1, j * choice + j + 1, choice, choice))
            pygame.draw.rect(miniView, miniViewColors[1], ((i * choice + i + 1)
                * coef, (j * choice + j + 1) * coef, choice * coef, choice *
                coef))

def draw_cells():
    for livingCell in livingCells:
        livingCell.draw(mainWindow, choice)
        livingCell.draw(miniView, choice, coef, coef)

def draw_mini_view():
    mainWindow.blit(miniView, (windowDimensions[0] - miniView.get_width(), 0))

def check_events():
    global mousex, mousey, removingCells, mouseIsDown
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
        elif event.type == MOUSEBUTTONDOWN:
            mouseIsDown = True
            removingCells = is_cell_at(int(mousex / (choice + 1)), int(mousey /
                (choice + 1)))
        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            mouseIsDown = False
        elif event.type == KEYDOWN:
            if event.key in (K_LEFT, K_RIGHT, K_UP, K_DOWN):
                pass
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))

def _game_init_():
    global coef, colors, mousex, mousey, fpsClock, gridMain, miniView
    global mainWindow, livingCells, mouseIsDown, mousexCoord, mouseyCoord
    global miniViewColors, portion_of_step, readyToGenerate, mainWindowColors
    global windowDimensions
    coef = 1. / 4.
    pygame.init()
    fpsClock = pygame.time.Clock()
    readyToGenerate = False
    windowDimensions = (0, 0)
    mainWindow = pygame.display.set_mode(windowDimensions, pygame.FULLSCREEN)
    windowDimensions = (mainWindow.get_size())
    miniView = pygame.Surface((windowDimensions[0] * coef,
        windowDimensions[1] * coef))
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
    'darkGrey':pygame.Color(64, 64, 64),
    'grey': pygame.Color(127, 127, 127),
    'white': pygame.Color(255, 255, 255)
    }
    mousex, mousey, mousexCoord, mouseyCoord = 0, 0, 0, 0
    gridMain = [20, 40]
    livingCells = []
    livingCells.append(PlaceholdingClass.PlaceholdingClass())
    portion_of_step = 0.
    mainWindowColors = (colors['grey'], colors['darkGrey'])
    miniViewColors = (colors['darkGrey'], colors['grey'])
    mouseIsDown = False
    removingCells = False
    assure_cell_at(colors['magenta'], 2, 1)
    assure_cell_at(colors['green'], 2, 2)
    assure_cell_at(colors['blue'], 1, 2)
    pygame.display.set_caption('Lyfe')
