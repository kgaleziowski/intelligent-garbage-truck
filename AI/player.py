import time
import pygame as pg
from trash import *
from settings import *
import settings
from HUD import *
from search import *


class Player(pg.sprite.Sprite):
    """description of class"""

    def __init__(self, game, map, points_grid, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.map = map
        self.image = game.player_img
        self.image_2 = game.player_img_2
        self.tmp_image = game.player_img
        self.points_grid = points_grid
        self.rect = self.image.get_rect()
        self.state = State(y, x, 1)

    def _drive(self, actions):

        # for action in actions.reverse():
        for action in actions:

            self._move(action)
            pygame.event.pump()
            self.map.refresh()
            time.sleep(TRUCK_SPEED)
            self.game.update()
            self.game.draw()


    def _move(self, action):
        x = self.state.x
        y = self.state.y
        direction = self.state.direction

        # always legal
        if action == "Left":

            self._truck_direction(direction, action)
            self.state.direction = 3 if direction == 0 else direction - 1

        # always legal
        elif action == "Right":

            self._truck_direction(direction, action)
            self.state.direction = (direction + 1) % 4

        # check if its legal
        elif action == "Forward":
            t_x = x + 1 if direction == 1 else (x - 1 if direction == 3 else x)
            t_y = y - 1 if direction == 0 else (y + 1 if direction == 2 else y)

            if self.points_grid[t_y][t_x].is_available:
                self.state.x = t_x
                self.state.y = t_y
            else:
                print("[ MOVE LOG ] - You can't move in that direction!")

        self.update()

    def _truck_direction(self, direction, action):

        if direction == 1:
            if action == "Left":
                self.image = pg.transform.rotate(self.image, 90)

            if action == "Right":
                self.image = pg.transform.rotate(self.image, -90)

        if direction == 2:
            if action == "Left":
                self.image = self.tmp_image

            if action == "Right":
                self.image = self.image_2

        if direction == 3:
            if action == "Left":
                self.image = pg.transform.rotate(self.image, 90)

            if action == "Right":
                self.image = pg.transform.rotate(self.image, -90)

        if direction == 0:
            if action == "Right":
                self.image = self.tmp_image

            if action == "Left":
                self.image = self.image_2

    def update(self):
        self.rect.x = self.state.x * TILESIZE
        self.rect.y = self.state.y * TILESIZE

    def get_position(self):
        return [self.state.y, self.state.x]

    # Segregate trashes
    def segregate(self):

        if settings.paper_amount > 0:
            goal_state = State(settings.paper_position[1], settings.paper_position[0], None)
            Search(self.map.points_grid, self.game).graph_search_AStar(self.state, goal_state)
            settings.current_amount -= settings.paper_amount
            settings.trash_capacity[0] += settings.paper_amount
            settings.paper_amount = 0


        if settings.glass_amount > 0:
            goal_state = State(settings.glass_position[1], settings.glass_position[0], None)
            Search(self.map.points_grid, self.game).graph_search_AStar(self.state, goal_state)
            settings.current_amount -= settings.glass_amount
            settings.trash_capacity[2] += settings.glass_amount
            settings.glass_amount = 0


        if settings.plastic_amount > 0:
            goal_state = State(settings.plastic_position[1], settings.plastic_position[0], None)
            Search(self.map.points_grid, self.game).graph_search_AStar(self.state, goal_state)
            settings.current_amount -= settings.plastic_amount
            settings.trash_capacity[1] += settings.plastic_amount
            settings.plastic_amount = 0

        if settings.mixed_amount > 0:
            goal_state = State(settings.mixed_position[1], settings.mixed_position[0], None)
            Search(self.map.points_grid, self.game).graph_search_AStar(self.state, goal_state)
            settings.current_amount -= settings.mixed_amount
            settings.trash_capacity[3] += settings.mixed_amount
            settings.mixed_amount = 0
        
        goal_state = State(10, 66, None)
        Search(self.map.points_grid, self.game).graph_search_AStar(self.state, goal_state)

        if settings.current_day == 7.5:
            settings.current_day = 1
            settings.trash_capacity = [0,0,0,0]
        else:
            settings.current_day += 0.5

    def main_loop(self):
        # from map object get trash places
        trash_places = self.map.get_trash_places()
        # for every trash order
        for trash in trash_places:
            print(trash.x,trash.y)
            # determine desired state
            goal_state = State(trash.x, trash.y, None)
            # draw trash
            # draw obstacles
            self.map.add_obstacles()
            self.map.add_trash(trash)

            # try to reach desired state
            Search(self.map.points_grid, self.game).graph_search_AStar(self.state, goal_state)
            # remove obstacles
            self.map.remove_obstacles()
            self.map.remove_trash(trash)

        self.map.add_obstacles()
        self.segregate()
        self.map.remove_obstacles()


    



