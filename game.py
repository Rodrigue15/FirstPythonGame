import pygame
from player import Player
from monster import Monster


# creer un classe game
class Game:
    def __init__(self):
        # generer le joeur
        self.player = Player(self)
        #groupe de monster
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}  # dict vide {cle:valeur}
        self.spawn_monster()

    def spawn_monster(self):
        monster = Monster()
        self.all_monsters.add(monster)

    def chechk_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)