import os
import random
import numpy
import torch
import tensorflow
from torchvision import transforms
from torchvision.datasets.mnist import MNIST
from Utils.settings import *
from os import path
from Graphics.HUD import *
from keras.models import load_model
from keras.preprocessing import image
import Utils.settings
vec = pygame.math.Vector2




class Trash(pygame.sprite.Sprite):


    def __init__(self, game, point):
        self.groups = game.all_sprites, game.trash
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = trashCanBlack
        self.rect = self.image.get_rect()
        self.pos = vec(point.x, point.y) * TILESIZE
        self.rect.center = self.pos
        self.game = game
        self.weight = random.randint(1, 70) #80
        self.bin_closed = numpy.random.choice([True,False], p=[1, 0]) #
        self.bills_paid = numpy.random.choice([True,False], p=[1, 0]) #
        self.length = numpy.random.choice([30,random.randint(20, 80)], p=[0.95, 0.05])
        self.width = numpy.random.choice([30,random.randint(20, 80)], p=[0.95, 0.05])
        self.height = numpy.random.choice([120,random.randint(20, 80)], p=[0.95, 0.05])



        file = random.choice(os.listdir('./GameTrashes'))

        self.img_trash = './GameTrashes/' + file


    def pass_params_to_HUD(self):
        HUD.check_trash_params(self.game, self, self.img_trash)



    def delete_trash(self):

        self.pass_params_to_HUD()
        img = image.load_img(self.img_trash, target_size=(512, 384))
        img_tensor = image.img_to_array(img)
        img_tensor = numpy.expand_dims(img_tensor, axis=0)
        img_tensor /= 255.
        pred = self.game.model.predict(img_tensor) #returns list of 4 numbers: glass, paper, plastic, mixed


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

        print(pred)
        print(predicted_class)


        if (predicted_class=='glass'):
            if(self.game.tree.make_decision(self,2)):
                Utils.settings.glass_amount += 1
                self.kill()
        elif (predicted_class == 'paper'):
            if(self.game.tree.make_decision(self,0)):
                Utils.settings.paper_amount += 1
                self.kill()
        elif (predicted_class == 'plastic'):
            if(self.game.tree.make_decision(self,1)):
                Utils.settings.plastic_amount += 1
                self.kill()
        elif (predicted_class == 'mixed'):
            if(self.game.tree.make_decision(self,3)):
                Utils.settings.mixed_amount += 1
                self.kill()

