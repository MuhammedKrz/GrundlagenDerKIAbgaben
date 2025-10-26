from search import genetic_algorithm, depth_first_tree_search, NQueensProblem, init_population

# gene_pool:  List of possible values for individuals
gene_pool = list(range(8))

# initializing start population
# pop_number:  Number of individuals in population
# state_length:  The length of each individual
population = init_population(200,gene_pool,8)

# Definition of the fitness function
def fitnessFunction(individual):
    return 100 -  total_conflicts(individual) * 3

def total_conflicts(individual):
    conflicts = 0
    n = len(individual)
    for i in range(n):
        y1 = individual[i]
        for j in range(i + 1, n):
            y2 = individual[j]
            # Check whether the queen are in the same y position or row
            if y1 == y2:
                conflicts += 1
                continue
            # Check if the y position lies on the attack field of the other queen
            dx = j - i
            if y1 == y2 + dx or y1 == y2 - dx:
                conflicts += 1
    return conflicts

#ngen max number of generations
#pmut mutation probability
result = genetic_algorithm(population, fitness_fn=fitnessFunction, f_thres=None, ngen=100, pmut=0.2)
print(result)
