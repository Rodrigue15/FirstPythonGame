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

    def damege(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            # si le joueur na plus de points de vie
            self.game.game_over()


    def update_health_bar(self, surface):
        # definir une couleur pour la jauge de vie
        bar_color = (111, 210, 46)
        # couleur d'arrier plan de jauge
        back_bar_color = (60, 63, 60)

        # definir la position de notre jauge de vie et sa largeur et son epaisseur
        bar_position = [self.rect.x + 50, self.rect.y + 20, self.health, 7]
        # definir la position de arriere plan de la jauge de vie
        back_bar_position = [self.rect.x + 50, self.rect.y + 20, self.max_health, 7]

        # dessiner la barre de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def launch_proj(self):
        # cree une nouvelle instance du projectile
        self.all_projectiles.add(Projectile(self))

    def move_rigth(self):
        # se deplacer seulement si le joueur nest pas en collision avec un monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
