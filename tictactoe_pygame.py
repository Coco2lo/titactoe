import pygame

# Création du jeu du morpion en interface graphique
# Le jeu doit être jouable à deux personnes

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Premier jeu morpion !")

# Définition des couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

XO= "x"
board = [[None]*3, [None]*3, [None]*3]

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
    
def user_click():
    x, y = pygame.mouse.get_pos()

    if (x < WIDTH / 3):
        col = 2
        print("col 2")
    elif (x < WIDTH / 3 * 2):
        col = 1
        print("col 1")
    elif (x < WIDTH):
        col = 0
        print("col 0")
    else:
        col = None

    if (y < HEIGHT / 3):
        row = 2
        print("row 2")
    elif (y < HEIGHT / 3 * 2):
        row = 1
        print("row 1")
    elif (y < HEIGHT):
        row = 0
        print("row 0")
    else:
        row = None


def main ():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()
        game_initiating_window()
        user_click()

    pygame.quit()

if __name__ == "__main__":
    main()