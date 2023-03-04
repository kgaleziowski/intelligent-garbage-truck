from Point import *
import xml.etree.cElementTree as ET
import pygame as pg
import pytmx
import settings
import shutil
from search import *
import os
from settings import *
import random
import csv


class TiledMap:
    def __init__(self, game, filename):
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.game = game
        self.filename = filename
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm
        self.all_sprites = game.all_sprites
        self.trash = game.trash
        self.flag = True
        self.obstacles = []
        self.trash_points = []

    def render(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmxdata.tilewidth,
                                            y * self.tmxdata.tileheight))

    def make_map(self):
        temp_surface = pg.Surface((self.width, self.height))
        self.render(temp_surface)
        self.map_to_points_grid()

        return temp_surface

    def map_to_points_grid(self):
        # treat as XML
        tree = ET.parse(self.filename)
        root = tree.getroot()
        # list of rows
        roads = root.findall('layer')[0].find('data').text.split('\n')
        # list of lists
        map = []

        # list of trashes
        self.trash_places = []

        for row in roads:
            fetched_row = row[:-1].split(",")
            map.append(fetched_row)

        # get rid of first and last empty lines
        map.pop(0)
        map.pop(45)
        # in map now is stored 2d list of chars representing our grid
        # we parse that map in order to generate grid of points
        # from roads and trash_spots we init graph
        self.points_grid = []
        self.road_points = []
        x = 0
        y = 0
        for row in map:
            points_row = []
            for tile in row:
                # for each tile we create point for better navigation on mafp
                new_point = Point(x, y, self.game)

                # for each point which is part of road we extend that object with other properties
                if tile not in ILLEGAL_TILES:
                    # mark as reachable point for our truck
                    new_point.set_available()
                    # check if its dump_tile
                    if x == DUMP_TILE_X and y == DUMP_TILE_Y:
                        new_point.set_dump()
                    # check if its trash or part of road and mark as it
                    new_point.set_road()
                    self.road_points.append(new_point)

                points_row.append(new_point)
                x = x + 1

            self.points_grid.append(points_row)
            y = y + 1
            x = 0

    def get_trash_places(self):
        return random.sample(self.trash_places, TRASH_COUNT)

    def add_trash(self, point):
        self.points_grid[point.y][point.x].draw_trash()

    def remove_trash(self, y, x):
        self.points_grid[y][x].remove_trash()

    def sel_point_by_click(self, pos_x, pos_y):
        x = pos_x // TILESIZE
        y = pos_y // TILESIZE
        selected_point = self.points_grid[y][x]
        selected_point.details()
        self.selected_state = State(y, x, None)
        self.selected_point = selected_point

    def run_SEARCH_ALGORITHM_for_selected(self, player_state):
        # clear map
        for point in self.road_points:
            if point.marked == True:
                point.visu_remove_mark()
        # if there is selected point we can run A*
        if hasattr(self, 'selected_point'):
            if self.selected_point == None:
                print("Select destination point by left click!")
            else:
                if self.game.algorithm:
                    Search(self.points_grid, self.game).graph_search_BFS(player_state, self.selected_state)
                    print("[ SEARCH LOG ] Path found by: BFS")
                else:
                    Search(self.points_grid, self.game).graph_search_AStar(player_state, self.selected_state)
                    print("[ SEARCH LOG ] Path found by: A*")
        # clear point
        self.selected_point = None
        # remove all obstacles

    def add_trash_point(self):
        if hasattr(self, 'selected_point'):
            if(self.selected_point == None):
                print('[ UTILS LOG ] No garbage truck collection point selected. Do it by left click!')
            elif self.selected_point.is_road:
                print('[ UTILS LOG ] Garbage truck collection set')
                self.points_grid[self.selected_point.y][self.selected_point.x].set_garbage_collection_point()
                self.points_grid[self.selected_point.y][self.selected_point.x].draw_trash()
                self.trash_points.append(self.points_grid[self.selected_point.y][self.selected_point.x])


    def add_obstacle(self):
        if hasattr(self, 'selected_point'):
            if self.selected_point is None:
                print("Select point by left click and then press D to create obstacle!")
            elif self.selected_point.is_road:
                self.points_grid[self.selected_point.y][self.selected_point.x].set_obstacle()
                self.points_grid[self.selected_point.y][self.selected_point.x].draw_obstacle()
                self.obstacles.append(self.points_grid[self.selected_point.y][self.selected_point.x])
        else:
            print("[ ERR ] Select point by left click and then press D to create obstacle!")

    def remove_trash(self, y, x):
        self.points_grid[y][x].remove_trash()

    def clear(self):
        for row in self.points_grid:
            for point in row:
                if point.is_trash_point:
                    self.points_grid[point.y][point.x].remove_trash_point()
                if point.is_obstacle:
                    self.points_grid[point.y][point.x].remove_obstacle()

        self.trash_points = []
        self.obstacles = []

    def refresh(self):

        # redraw trash point if is still in list
        for trash_point in self.trash_points:
            self.points_grid[ trash_point.y ][ trash_point.x ].remove_trash_point()
            self.points_grid[ trash_point.y ][ trash_point.x ].draw_trash()

        # redraw obstacles after truck driving through
        for obstacle in self.obstacles:
            self.points_grid[ obstacle.y ][ obstacle.x ].remove_obstacle()
            self.points_grid[ obstacle.y ][ obstacle.x ].draw_obstacle()


    """ Function draws state of map from configuration file """
    def draw_configuration(self, cfg):
        config_dir = os.path.join( os.getcwd(), cfg)
        file_name = os.path.join(config_dir, cfg + ".csv")

        y = 0
        with open(file_name, 'r') as file:
            for line in file:
                row = line.strip().split(";")
                x = 0
                for mark in row:

                    # point is available
                    if mark != 'X':
                        self.points_grid[y][x].set_available()

                        # it's trash point
                        if mark == 'T':
                            if x == DUMP_TILE_X and y == DUMP_TILE_Y:
                                continue
                            self.points_grid[y][x].set_garbage_collection_point()
                            self.points_grid[y][x].draw_trash()

                        elif mark == 'O':
                            self.points_grid[y][x].set_obstacle()
                            self.points_grid[y][x].draw_obstacle()
                            self.obstacles.append(self.points_grid[y][x])

                        elif mark == 'D':
                            self.points_grid[y][x].set_dump()

                        elif mark == 'R':
                            self.points_grid[y][x].set_road()

                    x += 1
                y += 1

    """ Function saves current state of map to .csv file """
    def save_configuration(self):
        map_config = []
        for row in self.points_grid:
            map_row = []
            for point in row:
                if point.is_available:

                    if point.is_trash_point:
                        map_row.append("T")

                    elif point.is_obstacle:
                        map_row.append("O")

                    elif point.is_dump:
                        map_row.append("D")

                    else:
                        map_row.append("R")

                else:
                    map_row.append("X")

            map_config.append(map_row)

        # create folder for configuration files - name is from settings file
        config_dir = os.path.join( os.getcwd(), cfg)

        # clear folder with that name if exists
        if os.path.exists(config_dir):
            shutil.rmtree(config_dir, ignore_errors=True)

        # create new folder
        os.makedirs(config_dir)

        # set file path
        config_file = os.path.join(config_dir, cfg + ".csv")

        # save configuration file in that folder
        with open(config_file, 'w', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerows(map_config)