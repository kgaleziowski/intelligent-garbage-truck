import csv
import os
from Point import *
from search import *

# helper script to generate cost map for configuration

CONFIG_FILE = '008.csv'

points_grid = []

trash_points = []

class TrashPoint():

    def __init__(self, ordinal_number, y, x):
        self.ordinal = ordinal_number
        self.y = y
        self.x = x

# after this function we have list of points we want to visit, first is starting point, end is dump point where sorting begins
def load_config(config_file):
    global trash_points

    config_dir = os.path.join( os.getcwd(), config_file.split(".")[0])

    config = os.path.join(config_dir, config_file)

    with open(config, 'r') as file:

        # first point is starting point with ordinal_number 0
        start = TrashPoint(0, 10, 66)
        trash_points.append(start)

        trash_point_ordinal_number = 1

        y = 0
        for line in file:
            x = 0
            points_row = []
            print(line)
            for mark in line.split(';'):
                point = Point(y, x)

                # point is available
                if mark != 'X':
                    point.set_available()

                    # it's trash point
                    if mark == 'T':
                        point.set_trash_point()
                        trash_point = TrashPoint(trash_point_ordinal_number, y, x)
                        trash_points.append(trash_point)
                        trash_point_ordinal_number += 1

                    elif mark == 'O':
                        point.set_obstacle()

                    elif mark == 'D':
                        point.set_dump()

                    elif mark == 'R':
                        point.set_road()

                x += 1
                points_row.append(point)

            y += 1
            points_grid.append(points_row)

        # last point is dump point
        end = TrashPoint(trash_point_ordinal_number, 11, 82)
        trash_points.append(end)

        return points_grid

# generate cost matrix (identity matrix) depending on points grid from configuration
def cost_matrix(points_grid):
    global trash_points

    searcher = Search(points_grid, None)

    cost_matrix = [[0 for col in range(len(trash_points))] for row in range(len(trash_points))]

    for i in range( len(trash_points) ):
        start_point = trash_points[i]
        start_state = State(start_point.y, start_point.x, 2)

        for j in range(i):
            end_point = trash_points[j]
            goal_state = State(end_point.y, end_point.x, 2)

            print("[SEARCH] Counting cost from " + str(start_point.ordinal) + " to " + str(end_point.ordinal) )

            cost_matrix[i][j] = searcher.graph_search_AStar(start_state, goal_state)
            cost_matrix[j][i] = cost_matrix[i][j]
            print("COST: " + str(cost_matrix[i][j]))

    return cost_matrix

def save_cost_matrix(config_file, cost_matrix):

    filename = "C-" + config_file.split(".")[0] + ".csv"

    config_dir = os.path.join( os.getcwd(), config_file.split(".")[0])

    file_path = os.path.join( config_dir, filename)

    with open(file_path, 'w', newline='') as cost_file:
        csv_writer = csv.writer(cost_file, delimiter=';')
        csv_writer.writerows(cost_matrix)

def save_trash_points(config_file):
    global trash_points
    # ordinal number ; y ; x
    filename = "TP-" + config_file.split(".")[0] + ".csv"

    config_dir = os.path.join( os.getcwd(), config_file.split(".")[0])

    file_path = os.path.join( config_dir, filename)

    with open(file_path, 'w', newline='') as points_file:
        csv_writer = csv.writer(points_file, delimiter=";")

        for trash_point in trash_points:
            row = [ trash_point.ordinal, trash_point.y, trash_point.x ]
            csv_writer.writerow(row)

# load configuration
points_grid = load_config(CONFIG_FILE)

# generate cost map depending on configuration
cost_matrix = cost_matrix(points_grid)

# create two files - one file is for client to translate path depending on GA TSP result and second is cost matrix for GA
save_cost_matrix(CONFIG_FILE, cost_matrix)

save_trash_points(CONFIG_FILE)

