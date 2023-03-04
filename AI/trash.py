import os
import random
import numpy
import torch
import tensorflow
from torchvision import transforms
from torchvision.datasets.mnist import MNIST
from settings import *
from os import path
from HUD import *
from keras.models import load_model
from keras.preprocessing import image
import settings
vec = pygame.math.Vector2




class Trash(pygame.sprite.Sprite):


    def __init__(self, game, point):
        self.groups = game.all_sprites, game.trash
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = random.choice([trashCanYellow])
        self.rect = self.image.get_rect()
        self.pos = vec(point.x, point.y) * TILESIZE
        self.rect.center = self.pos
        self.game = game
        self.weight = random.randint(1, 100)
        self.bin_closed = numpy.random.choice([True,False], p=[0.9, 0.1])
        self.bills_paid = numpy.random.choice([True,False], p=[0.9, 0.1])
        self.length = numpy.random.choice([30,random.randint(20, 80)], p=[0.95, 0.05])
        self.width = numpy.random.choice([30,random.randint(20, 80)], p=[0.95, 0.05])
        self.height = numpy.random.choice([120,random.randint(20, 80)], p=[0.95, 0.05])

        dir = random.choice(os.listdir('Dataset-trashes'))
        path = './Dataset-trashes/' + dir + '/'
        file = random.choice(os.listdir(path))
        self.img_trash = path + file                     #'./Dataset-trashes/glass/glass (3).jpg'
        self.number = 1

    def pass_params_to_HUD(self):
        HUD.check_trash_params(self.game, self, self.img_trash)



    def delete_trash(self):
        self.pass_params_to_HUD()
        img = image.load_img(self.img_trash, target_size=(512, 384))
        img_tensor = image.img_to_array(img)
        img_tensor = numpy.expand_dims(img_tensor, axis=0)
        img_tensor /= 255.

        pred = self.game.model.predict(img_tensor) # returns list of 4 numbers: glass, paper, plastic, mixed

        glass = pred[0][0]
        paper = pred[0][1]
        plastic = pred[0][2]
        mixed = pred[0][3]


        if (max(glass,paper,plastic,mixed) == glass):
            predicted_class = 'glass'
        elif (max(glass,paper,plastic,mixed) == paper):
            predicted_class = 'paper'
        elif(max(glass,paper,plastic,mixed) == plastic):
            predicted_class = "plastic"
        else:
            predicted_class = 'mixed'

        if (predicted_class=='glass'):
            if(self.game.tree.make_decision(self,2)):
                settings.glass_amount += 1
                self.kill()
        elif (predicted_class == 'paper'):
            if(self.game.tree.make_decision(self,0)):
                settings.paper_amount += 1
                self.kill()
        elif (predicted_class == 'plastic'):
            if(self.game.tree.make_decision(self,1)):
                settings.plastic_amount += 1
                self.kill()
        elif (predicted_class == 'mixed'):
            if(self.game.tree.make_decision(self,3)):
                settings.mixed_amount += 1
                self.kill()

