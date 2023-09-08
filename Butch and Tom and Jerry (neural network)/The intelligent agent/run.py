import random
import inspect
import copy
import physics

FORCE = 1  # consider the force (weight) to calculate the maximum possible output from the nn (if it is possible to tell the maximum output needed, consdider it to determine the maximum force(weight) by looking at the neural network)
BIAS = 4.5
POPULATION = 30
GENERATIONS = 40000
CROSS_OVERS_A_GENERATION = 6
MUTATIONS_A_GENERATION = 8
FIRST_CHROMOSOMES_TO_VIEW = 30


def fitness(w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16, w17, w18, w19, w20, w21, w22, w23,
            w24, w25, w26, w27, w28, w29, w30, w31, w32, w33, w34, w35, w36, w37, w38, w39, w40, w41, w42, w43, w44,
            w45, w46, w47, w48, w49, w50, w51, w52, w53, w54, w55, w56, w57, w58, w59, w60, w61, w62, w63, w64, w65,
            w66, w67, w68, w69, w70, w71, w72, w73, w74, w75, w76, w77, w78, w79, w80, w81, w82, w83, w84, w85, w86,
            w87, w88, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11):
    return physics.manifest(w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16, w17, w18, w19, w20,
                            w21, w22, w23, w24, w25, w26, w27, w28, w29, w30, w31, w32, w33, w34, w35, w36, w37, w38,
                            w39, w40, w41, w42, w43, w44, w45, w46, w47, w48, w49, w50, w51, w52, w53, w54, w55, w56,
                            w57, w58, w59, w60, w61, w62, w63, w64, w65, w66, w67, w68, w69, w70, w71, w72, w73, w74,
                            w75, w76, w77, w78, w79, w80, w81, w82, w83, w84, w85, w86, w87, w88, b1, b2, b3, b4, b5,
                            b6, b7, b8, b9, b10, b11)


NUM_OF_GENES = len(inspect.signature(fitness).parameters)
MAX_NUM_OF_GENES_TO_BE_MUTATED = 15
MIN_NUM_OF_GENES_TO_BE_MUTATED = 1
INDEX_OF_FIRST_BIAS = 88  # start counting from 0  # or simply assign the count of total weights
FITNESS_CONSISTENCY_GUARANTEED = True  # would two identical chromosome raise the same fitness value always? True if yes, False if no


def unique(list):
    unique_list = []

    for i in list:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list


def apply_rank_based_selection(chromosomes_ranked_by_fitness):
    unique_chromosomes_ranked_by_fitness = unique(chromosomes_ranked_by_fitness)
    sum = 0
    list_of_ranges = []
    for i in range(1, len(unique_chromosomes_ranked_by_fitness) + 1):
        sum = sum + 1 / i
        list_of_ranges.append(sum)

    new_chromosomes = []
    for _ in range(len(chromosomes_ranked_by_fitness)):
        random_spin_number = random.uniform(0, sum)
        for i in range(0, len(unique_chromosomes_ranked_by_fitness)):
            if random_spin_number <= list_of_ranges[i]:
                new_chromosomes.append(copy.deepcopy(unique_chromosomes_ranked_by_fitness[i]))
                break

    new_chromosomes.sort()
    new_chromosomes.reverse()
    return new_chromosomes


def apply_fitness_proportionate_selection(chromosomes_ranked_by_fitness):
    unique_chromosomes_ranked_by_fitness = unique(chromosomes_ranked_by_fitness)
    sum = 0
    list_of_ranges = []
    for i in range(len(unique_chromosomes_ranked_by_fitness)):
        sum = sum + unique_chromosomes_ranked_by_fitness[i][0]
        list_of_ranges.append(sum)

    new_chromosomes = []
    for _ in range(len(chromosomes_ranked_by_fitness)):
        random_spin_number = random.uniform(0, sum)
        for i in range(0, len(unique_chromosomes_ranked_by_fitness)):
            if random_spin_number <= list_of_ranges[i]:
                new_chromosomes.append(copy.deepcopy(unique_chromosomes_ranked_by_fitness[i]))
                break

    new_chromosomes.sort()
    new_chromosomes.reverse()
    return new_chromosomes


def crossover(fitness_and_chromosome1, fitness_and_chromosome2, fitness_and_chromosome1_to_replace,
              fitness_and_chromosome2_to_replace, unique_chromosomes):
    random_gene_number = int(random.uniform(1, NUM_OF_GENES - 1))  # 1 -- length-1
    # copy to crossover
    chromosome_1_copy = copy.deepcopy(fitness_and_chromosome1)
    chromosome_2_copy = copy.deepcopy(fitness_and_chromosome2)

    # swap a randomized part
    holder = chromosome_1_copy[1][random_gene_number:]
    chromosome_1_copy[1][random_gene_number:] = chromosome_2_copy[1][random_gene_number:]
    chromosome_2_copy[1][random_gene_number:] = holder

    # show parents
    print('offsprings:')
    print(fitness_and_chromosome1)
    print('X')
    print(fitness_and_chromosome2)
    print('↓')
    # recalculate fitness value
    if FITNESS_CONSISTENCY_GUARANTEED:
        is_in = False
        for fitness_and_chromosome in unique_chromosomes:
            if chromosome_1_copy[1] == fitness_and_chromosome[1]:
                chromosome_1_copy[0] = fitness_and_chromosome[0]
                print('already there, fitness value copied')
                is_in = True
                break

        if is_in == False:
            chromosome_1_copy[0] = fitness(*chromosome_1_copy[1])
            is_in = False

        for fitness_and_chromosome in unique_chromosomes:
            if chromosome_2_copy[1] == fitness_and_chromosome[1]:
                chromosome_2_copy[0] = fitness_and_chromosome[0]
                print('already there, fitness value copied')
                is_in = True
                break

        if is_in == False:
            chromosome_2_copy[0] = fitness(*chromosome_2_copy[1])
    else:
        chromosome_1_copy[0] = fitness(*chromosome_1_copy[1])
        chromosome_2_copy[0] = fitness(*chromosome_2_copy[1])

    # replace in low fitting
    fitness_and_chromosome1_to_replace[0] = chromosome_1_copy[0]
    fitness_and_chromosome1_to_replace[1] = chromosome_1_copy[1]
    print(fitness_and_chromosome1_to_replace)
    print('||')
    fitness_and_chromosome2_to_replace[0] = chromosome_2_copy[0]
    fitness_and_chromosome2_to_replace[1] = chromosome_2_copy[1]
    print(fitness_and_chromosome2_to_replace)


def mutate(fitness_and_chromosome, fitness_and_chromosome_to_replace):
    # copy
    chromosome_copy = copy.deepcopy(fitness_and_chromosome)
    # mutate a randomized gen
    list_of_random_genes_to_mutate = []
    for _ in range(int(random.uniform(MIN_NUM_OF_GENES_TO_BE_MUTATED,
                                      MAX_NUM_OF_GENES_TO_BE_MUTATED))):  # random mutating energy hitting (1 to 20) alleles in a chromosome
        list_of_random_genes_to_mutate.append(int(random.uniform(0, NUM_OF_GENES)))  # 0 -- length

    for random_gene_number in list_of_random_genes_to_mutate:
        if random_gene_number < INDEX_OF_FIRST_BIAS:
            chromosome_copy[1][random_gene_number] = random.uniform(-FORCE, FORCE)
        else:
            chromosome_copy[1][random_gene_number] = random.uniform(-BIAS, BIAS)

    # show chromosome to be mutated
    print('mutant:')
    print(fitness_and_chromosome)
    print('↓')

    # recalculate fitness
    chromosome_copy[0] = fitness(*chromosome_copy[1])

    # replace
    fitness_and_chromosome_to_replace[0] = chromosome_copy[0]
    fitness_and_chromosome_to_replace[1] = chromosome_copy[1]
    print(fitness_and_chromosome_to_replace)


# generate random chromosomes
chromosomes = []
given_chromosome = []
output_string = 'Will you provide a chromosome that is fittingly well for initializing the population? If so, please type in ' + str(
    NUM_OF_GENES) + ' gene numbers separated by a comma and a space (, ). If not, kindly enter any invalid input.'
try:
    while len(given_chromosome) != NUM_OF_GENES:
        given_chromosome = input(output_string)
        given_chromosome = list(map(float, given_chromosome.split(', ')))
        output_string = 'The number of provided numbers is unequal to ' + str(
            NUM_OF_GENES) + '. You may choose to provide the chromosome again or opt out by inputting an invalid input'
    chromosomes.append(given_chromosome)
    POPULATION -= 1
except Exception as e:
    print('Invalid input received, thank you. The population will now be completely randomly initialized.')

for _ in range(POPULATION):
    chromosome = []
    for _ in range(INDEX_OF_FIRST_BIAS):
        chromosome.append(random.uniform(-FORCE, FORCE))
    for _ in range(NUM_OF_GENES - INDEX_OF_FIRST_BIAS):
        chromosome.append(random.uniform(-BIAS, BIAS))

    chromosomes.append(chromosome)

# calculate fitness for each chromosome and sort them by
chromosomes_ranked_by_fitness = []
fitnessValue = None

print('fitness values for each chromosome in the initial random population:')
for chromosome in chromosomes:
    fitnessValue = fitness(*chromosome)
    chromosomes_ranked_by_fitness.append([fitnessValue, chromosome])
    print(fitnessValue)

chromosomes_ranked_by_fitness.sort()
chromosomes_ranked_by_fitness.reverse()

fittest_found = chromosomes_ranked_by_fitness[0].copy()

print('Gen', 0, '  (fittest ', FIRST_CHROMOSOMES_TO_VIEW, ' solutions)')

for chromosome in chromosomes_ranked_by_fitness[:FIRST_CHROMOSOMES_TO_VIEW]:
    print(chromosome)

print(
    '____________________________________________________________________________________________________________________________________________________________')
print('fittest solution found until the moment:')
print(fittest_found)
print(
    '____________________________________________________________________________________________________________________________________________________________')

for i in range(1, GENERATIONS):
    # selection
    chromosomes_ranked_by_fitness = apply_rank_based_selection(chromosomes_ranked_by_fitness)

    print('right after selection process:')
    for chromosome in chromosomes_ranked_by_fitness[:FIRST_CHROMOSOMES_TO_VIEW]:
        print(chromosome)

    # cross-over
    for _ in range(CROSS_OVERS_A_GENERATION):
        random_chromosome_1 = int(random.uniform(0, POPULATION))
        random_chromosome_1 = chromosomes_ranked_by_fitness[random_chromosome_1]
        random_chromosome_2 = int(random.uniform(0, POPULATION))
        while random_chromosome_1[1] == chromosomes_ranked_by_fitness[random_chromosome_2][1]:
            random_chromosome_2 = int(random.uniform(0, POPULATION))
        random_chromosome_2 = chromosomes_ranked_by_fitness[random_chromosome_2]

        crossover(random_chromosome_1,
                  random_chromosome_2,
                  random_chromosome_1,
                  random_chromosome_2,
                  unique(chromosomes_ranked_by_fitness))

    print('right after cross-over process:')
    for chromosome in chromosomes_ranked_by_fitness[:FIRST_CHROMOSOMES_TO_VIEW]:
        print(chromosome)

    # mutation
    for _ in range(MUTATIONS_A_GENERATION):
        random_chromosome = int(random.uniform(0, POPULATION))
        random_chromosome = chromosomes_ranked_by_fitness[random_chromosome]
        mutate(random_chromosome,
               random_chromosome
               )

    print('right after mutation process:')
    for chromosome in chromosomes_ranked_by_fitness[:FIRST_CHROMOSOMES_TO_VIEW]:
        print(chromosome)

    chromosomes_ranked_by_fitness.sort()
    chromosomes_ranked_by_fitness.reverse()

    if chromosomes_ranked_by_fitness[0][0] > fittest_found[0]:
        fittest_found = chromosomes_ranked_by_fitness[0].copy()

    print('Gen', i, '  (fittest ', FIRST_CHROMOSOMES_TO_VIEW, ') solutions')

    for chromosome in chromosomes_ranked_by_fitness[:FIRST_CHROMOSOMES_TO_VIEW]:
        print(chromosome)
    print(
        '____________________________________________________________________________________________________________________________________________________________')
    print('fittest solution found until the moment:')

    print(fittest_found)
    print(
        '____________________________________________________________________________________________________________________________________________________________')
