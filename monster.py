import pygame
import random


class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.health_max = 100
        self.attack = 0.3
        self.image = pygame.image.load('assets/assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = 3 + random.randint(1, 4)

    def damage(self, amount):
        # infliger les degat
        self.health -= amount

        # verifier si son nouveau nombre de vi est inf ou egale a zero
        if self.health <= 0:
            # reapparaitre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 4)
            self.health = self.health_max

    def update_health_bar(self, surface):
        # definir une couleur pour la jauge de vie
        bar_color = (111, 210, 46)
        # couleur d'arrier plan de jauge
        back_bar_color = (60, 63, 60)

        # definir la position de notre jauge de vie et sa largeur et son epaisseur
        bar_position = [self.rect.x + 11, self.rect.y - 20, self.health, 5]
        # definir la position de arriere plan de la jauge de vie
        back_bar_position = [self.rect.x + 11, self.rect.y - 20, self.health_max, 5]

        # dessiner la barre de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def forward(self):
        if not self.game.check_collision(self, self.game.all_player):
            self.rect.x -= self.velocity
        # si e montre est en collision avec le joeur
        else:
            # infliger les degat
            self.game.player.damege(self.attack)
