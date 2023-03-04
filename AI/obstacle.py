import random
from settings import *
from os import path
from Point import *
from HUD import *
import settings
vec = pygame.math.Vector2

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, game, point):
        self.groups = game.all_sprites, game.trash
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = obstacle
        self.rect = self.image.get_rect()
        self.pos = vec(point.x, point.y) * TILESIZE
        self.rect.center = self.pos
        self.game = game