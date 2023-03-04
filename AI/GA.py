import random
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

POPULATION_SIZE = 100
ELITE_SIZE = 10
MUTATION_RATE = 0.01
GENERATIONS = 1000
# C-001.csv
cfg = "008"
COST_MATRIX =  "C-" + cfg + ".csv"

""" Loads cost matrix - generated for particular state of map."""
def load_cost_matrix():
    cost_matrix = []

    # open folder with cost matrix for that config
    config_dir = os.path.join( os.getcwd(), cfg )

    config_file = os.path.join(config_dir, COST_MATRIX)

    with open(config_file, 'r') as file:

        for line in file:
            row = []
            for path_cost in line.strip().split(";"):
                row.append(int(path_cost))

            cost_matrix.append(row)

    return cost_matrix

""" Generates new individual - starting from 0 and ends with 0. Individual is a list of numbers - a path. """
def generate_individual(houses_count):
    # start with 0
    individual = ["0"]

    # list of possible destinations - if houses_count is 5, we choose from 1, 2, 3, 4, 5
    available = [str(x) for x in range(1, houses_count + 1)]

    # loop as long as there is house to be visited
    for i in range(0, houses_count ):
        # get random house of available array
        random_house = random.choice(available)
        # add to gene array
        individual.append(random_house)
        # remove from array of available
        available.remove(random_house)

    # end gene with 0
    individual.append(str(houses_count + 1))

    return individual

""" Generate individuals (lists) - every individual starts from 0 and end with 0 - starting point for trash """
def generate_population(population_size, houses_count):

    population = []

    # population size determines iterations count
    for i in range(population_size):
        # create individual
        individual = generate_individual(houses_count)
        population.append(individual)

    return population

""" Calculate fitness for each individual """
""" Example: [0, 1, 2, 3, 4, 5 ] so we check [0][1] + [1][2] + [2][3] + [3][4] etc. ... result is cost of whole path"""
def calculate_fitness(individual, cost_matrix):
    fitness = 0

    for i in range( len(individual) - 1):
        # calculate cost of path
        x = int(individual[i])
        y = int(individual[i + 1])
        fitness += cost_matrix[x][y]

    # return cost of particular path
    return fitness

""" Rank all individuals - order them by best fitness score (cheapest cost)"""
def rank_population(population, cost_matrix):
    fitness_results = {}

    for i in range(0, len(population) ):
        individual = population[i]
        fitness_results[i] = calculate_fitness( individual, cost_matrix )

    return sorted(fitness_results.items(), key=lambda item : item[1])

""" Select parents of next population """
""" """
def selection(ranked_population, elite_size):
    selection_results = []
    # using pandas create data structure with labeled axes for easier arithmetic operations
    data_frame = pd.DataFrame(np.array(ranked_population), columns=["Index", "Fitness"])
    data_frame['cum_sum'] = data_frame.Fitness.cumsum()
    data_frame['cum_perc'] = 100 * data_frame.cum_sum / data_frame.Fitness.sum()

    for i in range(0, elite_size):
        selection_results.append(ranked_population[i][0])

    for i in range(0, len(ranked_population) - elite_size ):
        pick = 100 * random.random()

        for i in range(0, len(ranked_population)):
            if pick <= data_frame.iat[i, 3]:
                selection_results.append(ranked_population[i][0])
                break

    return selection_results

""" Mating pool - extract routes selected by selection function """
""" Selection function returns indexes of best individuals, we simply extract the path """
def mating_pool(population, selection_results):
    mating_pool = []
    for i in range(0, len(selection_results) ):
        index = selection_results[i]
        mating_pool.append( population[index] )

    return mating_pool

""" Crossover between two parents """
""" After crossover individual has to start with 0 and end with the highest number because these points don't change"""
def crossover(parent1, parent2):

    geneA = random.randint(1, len(parent1) - 2)
    geneB = random.randint(1, len(parent2) - 2)

    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    childP1 = []

    for i in range(startGene, endGene):
        if parent1[i] != '0':
            childP1.append(parent1[i])

    childP2 = [item for item in parent2 if item not in childP1 and item != str(len(parent1) - 1) and item != '0']

    child =  ['0'] + childP1 + childP2 + [str(len(parent1) - 1)]
    return child

""" Crossing whole population """
def crossover_population(mating_pool, elite_size):
    children = []
    length = len(mating_pool) - elite_size
    pool = random.sample(mating_pool, len(mating_pool))

    for i in range(0, elite_size):
        children.append(mating_pool[i])

    for i in range(0, length):
        child = crossover(pool[i], pool[ len(mating_pool) - i - 1 ])
        children.append(child)

    return children

""" Mutate with specified mutation rate"""
def mutate(individual, mutation_rate):
    for to_be_swapped in range(1, len(individual) - 2):
        rand_num = random.random()
        if(rand_num < mutation_rate):
            swap_with = random.randint(1, len(individual) - 2)

            house_A = individual[to_be_swapped]
            house_B = individual[swap_with]

            individual[to_be_swapped] = house_B
            individual[swap_with] = house_A

    return individual

""" Mutating whole population """
def mutate_population(population, mutation_rate):
    mutated_population = []

    for index in range(0, len(population) ):
        mutated_individual = mutate(population[index], mutation_rate)
        mutated_population.append(mutated_individual)

    return mutated_population

""" Creating new generation """
def next_generation(current_generation, cost_matrix, elite_size, mutation_rate):
    # rank previous population in order to get best individuals
    population_ranked = rank_population(current_generation, cost_matrix)
    # proceed selection on population
    selection_results = selection(population_ranked, elite_size)
    # extract results of selection
    mat_pool = mating_pool(current_generation, selection_results)
    # create children (next population) by crossover
    children = crossover_population(mat_pool, elite_size)
    # finish creating next generation by mutating some of individuals
    next_generation = mutate_population(children, mutation_rate)

    return next_generation

""" Output best path after whole process """
def write_best_path(best_path):

    # get configuration direction
    config_dir = os.path.join( os.getcwd(), cfg )

    file_name = "BP-" + cfg + ".csv"

    best_path_file = os.path.join(config_dir, file_name)

    with open(best_path_file, "w") as file:
        file.write(best_path)

def main():
    # getting cost_matrix that will be used for calculating fitness
    cost_matrix = load_cost_matrix()
    # number of houses to visit is length of row - 1
    houses_count = len(cost_matrix) - 2
    # generate initial population based on houses_count
    population = generate_population(POPULATION_SIZE, houses_count )
    # track progress of whole process
    progress = []
    # add best individual from initial population
    progress.append(rank_population(population, cost_matrix)[0][1])

    # proceed with next generations
    for i in range(0, GENERATIONS):
        # create new population based on previous
        population = next_generation(population, cost_matrix, ELITE_SIZE, MUTATION_RATE)
        # get sorted population by its fitness
        best_in_generation = rank_population(population, cost_matrix)
        # add best individual from that population
        progress.append( best_in_generation[0][1] )
        # print log for console about current generation
        print("Generation: " + str(i))

    # final population is meant to be our best so we extract the best individual
    bestIdx = rank_population(population, cost_matrix)[0][0]
    # save that path
    write_best_path(" -> ".join(population[bestIdx]))

    # create plot
    plt.plot(progress)
    plt.ylabel('Cost')
    plt.xlabel('Generation')

    # save plot to file
    config_dir = os.path.join( os.getcwd(), cfg )
    plot_name = "PLOT-" + cfg + ".png"
    plot_file = os.path.join(config_dir, plot_name)
    plt.savefig(plot_file)

    plt.show()

main()
