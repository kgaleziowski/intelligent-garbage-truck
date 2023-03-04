from map import TiledMap
import pygame as pg
import sys
from os import path
from settings import *
from player import *
from map import *
from HUD import *
from DecisionTree import *
from trash import *
from search import *

class Game:

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        # key delay
        pg.key.set_repeat(500, 100)

        # false = A* true = BFS
        self.algorithm = False

        # all objects
        self.all_sprites = pg.sprite.Group()
        self.trash = pg.sprite.Group()
        self.obstacle = pg.sprite.Group()

        self.model = load_model('./LearningMethods/train_model.h5')

        self.init()

        #HUD init
        self.HUD = HUD(self)

        # load game configuration
        self.load_data()
       
        # create player
        self.player = Player(self, self.map, self.points_grid, 66, 10)

        self.tree = DecisionTree()

        # start game - main loop
        while True:
            # refresh
            self.dt = self.clock.tick(FPS) / 1000
            # check for events
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                # keyboard events
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.quit()
                    if event.key == pg.K_LEFT:
                        self.player._move(action="Left")
                    if event.key == pg.K_RIGHT:
                        self.player._move(action="Right")
                    if event.key == pg.K_UP:
                        self.player._move(action="Forward")
                    if event.key == pg.K_SPACE:
                        self.main_loop()
                    if event.key == pg.K_a:
                        self.algorithm = not self.algorithm
                        print("[ UTILS LOG ] Searching algorithm: ", end="")
                        if self.algorithm:
                            print("A*")
                        else:
                            print("BFS")
                    if event.key == pg.K_c:
                        # clear map
                        self.map.clear()
                        print("C")
                    if event.key == pg.K_o:
                        self.map.add_obstacle()
                        # add obstacle
                        print("O")
                    if event.key == pg.K_t:
                        self.map.add_trash_point()
                        # add trash
                        print("T")
                    if event.key == pg.K_s:
                        self.map.save_configuration()
                        print("S")


                # mouse events
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # by left click we choose point on map
                    if event.button == 1:
                        self.map.sel_point_by_click(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

                    if event.button == 3:
                        self.map.run_SEARCH_ALGORITHM_for_selected(self.player.state)

            # update objects
            self.update()
            # draw
            self.draw()

    # loading data function
    def load_data(self):
        game_folder = path.dirname(__file__)
        map_folder = path.join(game_folder, 'map')
        self.map = TiledMap(self,path.join(map_folder, 'City_3.tmx'))
        self.map.map_to_points_grid()
        self.points_grid = self.map.points_grid
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.player_img = pg.image.load(path.join(map_folder,'truckdelivery.png')).convert_alpha()
        self.player_img_2 = pg.image.load(path.join(map_folder,'truckdeliverymirror.png')).convert_alpha()

    # update objects function
    def update(self):
        self.all_sprites.update()

        pick_up = pg.sprite.spritecollide(self.player,self.trash,True)
        if pick_up == True:
            self.trash.remove()
            self.HUD.display_hud()
            self.draw()



    # draw objects function
    def draw(self):
        self.screen.blit(self.map_img, self.map_rect)
        self.all_sprites.draw(self.screen)
        self.HUD.display_hud()
        pg.display.flip()

    def init(self):
        img = image.load_img('./Dataset-trashes/glass/glass (1).jpg', target_size=(512, 384))
        img_tensor = image.img_to_array(img)
        img_tensor = numpy.expand_dims(img_tensor, axis=0)
        img_tensor /= 255.
        self.model.predict(img_tensor)


    def load_config(self, cfg):

        self.pickup_states = dict()

        config_dir = os.path.join( os.getcwd(), cfg)
        file_name = os.path.join(config_dir, "TP-" + cfg + ".csv")

        with open(file_name, 'r') as file:

            # [ordinal number, y, x]
            for line in file:

                row = line.split(";")
                ordinal_number = (row[0])
                print(ordinal_number)
                y = int(row[1])
                x = int(row[2])


                if y != DUMP_TILE_Y and x != DUMP_TILE_X and y != 10 and x != 66:
                    self.map.trash_points.append( self.map.points_grid[y][x] )


                state = State(y, x, None)
                self.pickup_states[ordinal_number] = state

        # add ending point
        endpoint = State(DUMP_TILE_Y, DUMP_TILE_X , None)
        self.pickup_states[ len(self.pickup_states) ] = endpoint

    def start(self, cfg):
        
        searcher = Search(self.map.points_grid, self)

        config_dir = os.path.join( os.getcwd(), cfg)
        file_name = os.path.join(config_dir, "BP-" + cfg + ".csv")

        # best path is gene like 0 -> 7 -> 6 -> 1 -> 2 -> 4 -> 3 -> 9 -> 0
        with open(file_name, 'r') as file:
            print("PATH")
            path = file.readline().split(" -> ")
            print(path)

            for house in path[1:]:
                destination = self.pickup_states[house]
                print("Driving to: " + str(house) + " Coordinates: " + str(destination.y) + " / " + str(destination.x))
                searcher.graph_search_AStar(self.player.state, destination)
                if(destination.x == DUMP_TILE_X and destination.y == DUMP_TILE_Y):
                    self.map.clear()
                    continue
                self.map.trash_points.remove( self.map.points_grid[destination.y][destination.x] )
                self.map.remove_trash(destination.y, destination.x)

    def main_loop(self):
        for cfg in configurations:
            self.load_config(cfg)
            self.map.draw_configuration(cfg)
            self.start(cfg)
            self.player.segregate()
