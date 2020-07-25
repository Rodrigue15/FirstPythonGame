import pygame
import math
from game import Game

pygame.init()

# genrer la fenetre
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))

# import l'arrie plan
background = pygame.image.load('assets/assets/bg.jpg')

# importer la banier
banner = pygame.image.load('assets/assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rest = banner.get_rect()
banner_rest.x = math.ceil(screen.get_width() / 4)

# importer button pour le lancement
play_button = pygame.image.load('assets/assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

# charger le jeu
game = Game()

running = True

# boucle qui sexecute tant que la condition est vraie
while running:
    # appliquer larrier plan
    screen.blit(background, (0, -200))

    # verifier si le jeu a commencé
    if game.is_playing:
        #declencher les instruction
        game.update(screen)

    # verifier si notre jeu na pas commencer
    else:
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rest)


    # mettre a jour la fenetre
    pygame.display.flip()

    # si le joueur ferme la fenetre
    for event in pygame.event.get():
        # verifier si cest la fermeture de la fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # detecter si un joueur lache une touche
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detecter si la touche espace est enclaché
            if event.key == pygame.K_SPACE:
                game.player.launch_proj()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verification si la souris est en collision avec une button
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu a lance
                game.start()