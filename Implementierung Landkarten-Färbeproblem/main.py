from search import genetic_algorithm, init_population

# gene_pool:  List of possible values for individuals
gene_pool = list(range(1))

# initializing start population
# pop_number:  Number of individuals in population
# state_length:  The length of each individual
population = init_population(100,gene_pool,18)

# Definition of the fitness function
def fitnessFunction(individual):
    return (100 -  (total_conflicts(decodeBits(individual)) * 10)) - (numOfColors(decodeBits(individual))*5)

def decodeBits(bitString):
    decodedBit = []
    bit = ""
    for i in range(len(bitString)):
        bit += str(bitString[i])  # sammle Bits
        # Take all 3 Bit Segments on calculate the decimal number / only numbers which are divisible by 3
        if (i + 1) % 3 == 0:
            dezimal = int(bit, 2)
            decodedBit.append(dezimal)
            bit = ""
    return decodedBit

def numOfColors(decodedBit):
    numberOfDifferentElements = len(set(decodedBit))
    return numberOfDifferentElements

def total_conflicts(decodedBit):
    # A = 0 B = 1 C = 2 D = 3 E = 4 F is in this case not relevant
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    conflicts = 0
    if(decodedBit[A] == decodedBit[B]):
        conflicts += 1
    elif(decodedBit[A] == decodedBit[C]):
        conflicts += 1
    elif(decodedBit[B] == decodedBit[C]):
        conflicts += 1
    elif(decodedBit[D] == decodedBit[E]):
        conflicts += 1
    elif(decodedBit[D] == decodedBit[C]):
        conflicts += 1
    elif (decodedBit[B] == decodedBit[D]):
        conflicts += 1
    return conflicts

result = genetic_algorithm(population, fitness_fn=fitnessFunction, f_thres=None, ngen=100, pmut=0.1)
print(result)