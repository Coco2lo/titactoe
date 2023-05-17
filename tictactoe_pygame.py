import pygame
import sys
import time
from pygame.locals import *

# Création du jeu du morpion en interface graphique
# Le jeu doit être jouable à deux personnes

# Définition des variables globales
winner = None

draw = None

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Premier jeu morpion !")

# Définition des couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

XO= "x"
board = [[None]*3, [None]*3, [None]*3]

# Import des images
x_img = pygame.image.load("croix.png")
o_img = pygame.image.load("cercle.png")

x_img = pygame.transform.scale(x_img,(80,80))
o_img = pygame.transform.scale(o_img,(80,80))

CLOCK = pygame.time.Clock()

FPS = 30

def draw_window():
    WIN.fill(WHITE)
    pygame.display.update()

def game_initiating_window():
    # Ajout des lignes verticales
    pygame.draw.line(WIN, BLACK,(WIDTH / 3, 0), (WIDTH / 3, HEIGHT), 7)
    pygame.draw.line(WIN, BLACK, (WIDTH / 3 * 2, 0), (WIDTH / 3 * 2, HEIGHT), 7)

    # Ajout des lignes horizontales
    pygame.draw.line(WIN, BLACK,(0,HEIGHT / 3),(WIDTH, HEIGHT / 3), 7)
    pygame.draw.line(WIN, BLACK, (0, HEIGHT / 3 * 2), (WIDTH, HEIGHT / 3 * 2), 7)

    pygame.display.update()

def check_win():
    global board, winner, draw

    # Vérification d'une ligne gagné
    for row in range(0,3):
        if((board[row][0] == board[row][1] == board[row][2]) and (board[row][0] is not None)):
            winner = board[row][0]
            pygame.draw.line(WIN, RED,(0,(row + 1) * HEIGHT / 3 - HEIGHT / 6),(WIDTH, (row + 1) * HEIGHT / 3 - HEIGHT / 6), 4)
            break

    # Vérification d'une colonne gagné
    for col in range(0,3):
        if((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
            winner = board[0][col]
            pygame.draw.line(WIN, RED,(0,(col + 1) * WIDTH / 3 - WIDTH / 6, 0),((col + 1) * WIDTH / 3 - WIDTH / 6, HEIGHT), 4)
            break

    # Vérification si une diagonale de gauche à droite
    if((board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None)):
        winner = board[0][0]
        pygame.draw.line(WIN, RED, (50,50), (350,350), 4)

    # Vérification si une diagonale de droite à gauche
    if ((board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None)):
        winner = board[0][2]
        pygame.draw.line(WIN, RED, (350, 50), (50, 350), 4)

    if(all([all(row) for row in board]) and winner is None):
        draw = True

    pygame.display.update()

def drawXO(row, col):
    global board, XO

    if row == 1:
        posx = 30
    if row == 2:
        posx = WIDTH / 3 + 30
    if row == 3:
        posx = WIDTH / 3 * 2 + 30
    if col == 1:
        posy = 30
    if col == 2:
        posy = HEIGHT / 3 + 30
    if col == 3:
        posy = HEIGHT / 3 * 2 + 30

    board[row-1][col-1] = XO

    if (XO == 'x'):
        WIN.blit(x_img,(posy,posx))
        XO = 'o'
    else:
        WIN.blit(o_img,(posy,posx))
        XO = 'x'
    pygame.display.update()

def user_click():
    x, y = pygame.mouse.get_pos()

    # Check de la colonne
    if (x < WIDTH / 3):
        col = 2
    elif (x < WIDTH / 3 * 2):
        col = 1
    elif (x < WIDTH):
        col = 0
    else:
        col = None

    # Check de la ligne
    if (y < HEIGHT / 3):
        row = 2
    elif (y < HEIGHT / 3 * 2):
        row = 1
    elif (y < HEIGHT):
        row = 0
    else:
        row = None

    # Affichage des images
    if(row and col and board[row-1][col-1] is None):
        global XO

        drawXO(row,col)
        check_win()


def main ():
    run = True
    while run:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type is MOUSEBUTTONDOWN:
                user_click()

        draw_window()
        game_initiating_window()

    pygame.quit()

if __name__ == "__main__":
    main()