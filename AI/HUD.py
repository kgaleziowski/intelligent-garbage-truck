from numpy import printoptions
from settings import  *
import math
import random
import settings
import time
import numpy as np
import pygame

class HUD():


    def __init__ (self, game):
        self.screen = game.screen
        self.game = game

    def get_day(self):
        return days[(int(settings.current_day // 1))-1]

    def check_trash_params(self, trash, image):

        if trash.weight > 80:
            self.screen.blit(TOO_HEAVY, (60, 93))
            print("TOO HEAVY")
        if trash.bin_closed == False:
            self.screen.blit(TRASH_FULL, (125, 93))
            print("BIN NOT CLOSED")
        if trash.bills_paid == False:
            self.screen.blit(BILL_UNPAID, (10, 100))
            print("BILL NOT PAID")
        if (trash.width > 30 or trash.length > 30 or trash.height > 130):
            self.screen.blit(WRONG_TRASHCAN_SIZE, (150, 93))
            print("WRONG SIZE")

        img = pygame.image.load(image)
        img = pygame.transform.scale(img, (100,100))
        self.screen.blit(img ,(10,600))
        pygame.display.update()
        time.sleep(2)

    
    def display_hud(self):

        #setting place of icons

        bar = pygame.Rect(1370, 225, BAR_WIDTH, BAR_HEIGHT)
        glass_amount_text = HUD_FONT.render(str(settings.glass_amount), True, BLACK)
        plastic_amount_text = HUD_FONT.render(str(settings.plastic_amount), True, BLACK)
        paper_amount_text = HUD_FONT.render(str(settings.paper_amount), True, BLACK)
        mixed_amount_text = HUD_FONT.render(str(settings.mixed_amount), True, BLACK)
        calendar_text = HUD_FONT.render(self.get_day(), True, BLACK)
        paper_capacity_text = DUMP_FONT.render(str(settings.trash_capacity[0]) + "/" + "15", True, BLACK)
        glass_capacity_text = DUMP_FONT.render(str(settings.trash_capacity[2]) + "/" + "15", True, BLACK)
        plastic_capacity_text = DUMP_FONT.render(str(settings.trash_capacity[1]) + "/" + "15", True, BLACK)
        mixed_capacity_text = DUMP_FONT.render(str(settings.trash_capacity[3]) + "/" + "15", True, BLACK)

        if (settings.current_day % 1) == 0:
            self.screen.blit(DAY, (100, 0))
            self.screen.blit(CALENDAR, (0, 0))
            self.screen.blit(calendar_text, (25, 55))
        else:
            self.screen.blit(CALENDAR, (0, 0))
            self.screen.blit(calendar_text, (25, 55))
            self.screen.blit(NIGHT, (100, 15))
            self.screen.blit(NIGHT_ILLUSION, (0, 0))

        self.screen.blit(BAR, (bar.x, bar.y))
        self.screen.blit(mixed_amount_text, (1415, 270))
        self.screen.blit(paper_amount_text, (1415, 345))
        self.screen.blit(glass_amount_text, (1415, 420))
        self.screen.blit(plastic_amount_text, (1415, 495))
        self.screen.blit(paper_capacity_text, (1110, 29))
        self.screen.blit(glass_capacity_text, (1206, 29))
        self.screen.blit(plastic_capacity_text, (1303, 29))
        self.screen.blit(mixed_capacity_text, (1400, 29))

        pygame.display.update()