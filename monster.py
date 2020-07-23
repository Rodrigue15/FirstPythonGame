import pygame


class Monster(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.health_max = 100
        self.attack = 5
        self.image = pygame.image.load('assets/assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 540
        self.velocity = 3

    def forward(self):
        self.rect.x -= self.velocity
