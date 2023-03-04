import pygame
from trash import *
from settings import *
from obstacle import *

vec = pygame.math.Vector2

class Point(pygame.sprite.Sprite):

    def __init__(self, x, y, game = None):
        self.game = game
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.coordinates = [y, x]
        self.is_available = False
        self.is_road = False
        self.is_trash_point = False
        self.is_obstacle = False
        self.is_dump = False
        self.marked = False
        self.neighbours = []

    def set_available(self):
        self.is_available = True

    def set_road(self):
        self.is_road = True

    def set_dump(self):
        self.is_dump = True

    def set_neighbours(self, neighbours):
        self.neighbours = neighbours

    def set_trash_point(self):
        self.is_trash_point = True

    def remove_trash_point(self):
        self.is_trash_point = False
        if(hasattr(self, 'trash')):
            self.trash.kill()

    def set_garbage_collection_point(self):
        self.is_trash_point = True
        # self.trash = Trash(self.game, self)

    def draw_trash(self):
        self.trash = Trash(self.game, self)

    def remove_trash(self):
        Trash.delete_trash(self.trash)
        self.trash.kill()

    def set_obstacle(self):
        self.is_obstacle = True

    def draw_obstacle(self):
        self.obs = Obstacle(self.game, self)

    def remove_obstacle(self):
        self.obs.kill()
        
    def details(self):
        print("Coordinates: " + "[" + str(self.y) + ", " + str(self.x) + "]")
        print("Is available?: " + str(self.is_available))
        if self.is_road and not self.is_dump:
            print("Is road?: " + str(self.is_road))
        elif self.is_dump:
            print("Is dump?: " + str(self.is_dump))
        else:
            print("Is trash point?: " + str(self.is_trash_point))