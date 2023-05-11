import pygame

# Création du jeu du morpion en interface graphique
# Le jeu doit être jouable à deux personnes

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Premier jeu morpion !")

# Définition des couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 60

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

    pygame.quit()

if __name__ == "__main__":
    main()