import pygame
pygame.font.init()

# name of config file
cfg = "008"

# CONFIGURATIONS
configurations = [
    "001",
    "002",
    "005",
    "007",
    "008"
]

#
VISITED_IMG = pygame.image.load("Icons/visited.png")

#define some colors (R, G, B)
WHITE = (255,255,255)
BLACK = (0,0,0)
DARKGREY = (40,40,40)
LIGHTGREY = (100,100,100)
GREEN = (0,255,0)
RED = (255,0,0)
YELLOW = (255,255,0)

# game settings
WIDTH = 1440
HEIGHT = 720
FPS = 60
TITLE = "Inteligentna śmieciarka"
START_CORD_X = 10
START_CORD_Y = 80
TILES_WIDTH = 90
TILES_HEIGHT = 45
TRUCK_SPEED = 0.01
# MOVES
MOVE_UP = -TILES_WIDTH
MOVE_DOWN = TILES_WIDTH
MOVE_LEFT = -1
MOVE_RIGHT = 1

TILESIZE = 16
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# MAP
ILLEGAL_TILES = ['0']
TRASH_TILE = '891'
TRASH_COUNT = 10
DUMP_TILE_Y = 11
DUMP_TILE_X = 82

#Icons

#Map Icons
trashCanBlue = pygame.image.load("map/blueTrash.png")
trashCanBlack = pygame.image.load("map/blackTrash.png")
trashCanYellow = pygame.image.load("map/yellowTrash.png")
trashCanGreen = pygame.image.load("map/greenTrash.png")

#Obstacle Icon
obstacle = pygame.image.load("Icons/barrier.png")
OBSTACLES_COUNT = 20

#HUD Icons
ICON_WIDTH, ICON_HEIGHT = 30, 30
BAR_WIDTH, BAR_HEIGHT = 50, 320
BAR = pygame.image.load("Icons/HUD.png")
CALENDAR = pygame.image.load("Icons/calendar.png")
CALENDAR = pygame.transform.scale(CALENDAR, (100, 100))
DAY = pygame.image.load("Icons/day.png")
DAY = pygame.transform.scale(DAY, (100, 100))
NIGHT = pygame.image.load("Icons/night.png")
NIGHT = pygame.transform.scale(NIGHT, (80, 80))
NIGHT_ILLUSION = pygame.image.load("Icons/night_illusion.png")
BILL_UNPAID = pygame.image.load("Icons/bill_not_paid.png")
BILL_UNPAID = pygame.transform.scale(BILL_UNPAID, (50, 50))
TOO_HEAVY = pygame.image.load("Icons/too_heavy.png")
TOO_HEAVY = pygame.transform.scale(TOO_HEAVY, (65, 65))
TRASH_FULL = pygame.image.load("Icons/trash_full.png")
TRASH_FULL = pygame.transform.scale(TRASH_FULL, (50, 65))
WRONG_TRASHCAN_SIZE = pygame.image.load("Icons/wrong_size.png")
WRONG_TRASHCAN_SIZE = pygame.transform.scale(WRONG_TRASHCAN_SIZE, (50, 60))

#Fonts

HUD_FONT = pygame.font.SysFont("comicsans", 20)
DUMP_FONT = pygame.font.Font("Fonts/SourceCodePro-BoldItalic.ttf", 15)

#Trash Coordinates

glass_position = [76, 6]
plastic_position = [82, 6]
mixed_position = [88, 6]
paper_position = [70, 6]
all_trash = [glass_position, plastic_position, mixed_position, paper_position]
all_trash_places = []
trash_capacity = [0,0,0,0]
max_capacity = 15

#Trash amount

glass_amount = 0
plastic_amount = 0
paper_amount = 0
mixed_amount = 0
current_amount = glass_amount + plastic_amount + paper_amount + mixed_amount
max_amount = 15

#Days of the week
days = ["MON", " TUE", "WEN", " THU", " FRI", " SAT", " SUN"]
current_day = 1

