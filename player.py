import pygame
from projectile import Projectile


# creer un class pour le joueur
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.image = pygame.image.load('assets/assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
        self.all_projectiles = pygame.sprite.Group()

    def launch_proj(self):
        # cree une nouvelle instance du projectile
        self.all_projectiles.add(Projectile(self))

    def move_rigth(self):
        # se deplacer seulement si le joueur nest pas en collision avec un monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
