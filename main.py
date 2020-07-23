import pygame
from game import Game

pygame.init()

# genrer la fenetre
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))

# import l'arrie plan
background = pygame.image.load('assets/assets/bg.jpg')

# charger le jeu
game = Game()

running = True

# bouclel qui sexecute tant la condition est vrai
while running:
    # appliquer larrier plan
    screen.blit(background, (0, -200))

    # appliquer limage du jouer
    screen.blit(game.player.image, game.player.rect)

    # recupere les porjectile du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    # depalcer les montres
    for monster in game.all_monsters:
        monster.forward()

    # appliquer le group de projectile
    game.player.all_projectiles.draw(screen)

    #appliquer le group de monsters
    game.all_monsters.draw(screen)

    # mettre a jour la fenetre
    pygame.display.flip()

    # verifier si le joueur veut aller a gche ou  dte
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_rigth()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

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
