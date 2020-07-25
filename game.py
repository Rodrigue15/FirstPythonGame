import pygame
from player import Player
from monster import Monster


# creer un classe game
class Game:
    def __init__(self):
        # definir si notre jeu a commené
        self.is_playing = False
        # generer le joeur
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)
        # groupe de monster
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}  # dict vide {cle:valeur}

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        # remettre le jeu à neuf, retirer les monstre et remettre les points de vie du joueur
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):
        # appliquer limage du jouer
        screen.blit(self.player.image, self.player.rect)

        # Actualiser la barre
        self.player.update_health_bar(screen)

        # recupere les porjectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # depalcer les montres
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        # appliquer le group de projectile
        self.player.all_projectiles.draw(screen)

        # appliquer le group de monsters
        self.all_monsters.draw(screen)

        # verifier si le joueur veut aller a gche ou  dte
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_rigth()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
