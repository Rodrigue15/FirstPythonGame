import pygame
from player import Player
from monster import Monster


# creer un classe game
class Game:
    def __init__(self):
        # generer le joeur
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)
        #groupe de monster
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}  # dict vide {cle:valeur}
        self.spawn_monster()

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)