import random
import copy
import physics

FORCE = 400
POPULATION = 20
GENERATIONS = 40000
CROSS_OVERS_A_GENERATION = 4
MUTATIONS_A_GENERATION = 6
FIRST_CHROMOSOMES_TO_VIEW = 20


def fitness(a, a1, a2, b, b1, b2, c, c1, c2, d, d1, d2, e, e1, e2, f, f1, f2):
    return physics.manifest(a, a1, a2, b, b1, b2, c, c1, c2, d, d1, d2, e, e1, e2, f, f1, f2)


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
              fitness_and_chromosome2_to_replace):
    random_gene_number = int(random.uniform(1, 17))
    # copy to crossover
    chromosome_1_copy = copy.deepcopy(fitness_and_chromosome1)
    chromosome_2_copy = copy.deepcopy(fitness_and_chromosome2)

    # swap a randomized part
    holder = chromosome_1_copy[1][random_gene_number:]
    chromosome_1_copy[1][random_gene_number:] = chromosome_2_copy[1][random_gene_number:]
    chromosome_2_copy[1][random_gene_number:] = holder

    # recalculate fitness value
    chromosome_1_copy[0] = fitness(chromosome_1_copy[1][0], chromosome_1_copy[1][1], chromosome_1_copy[1][2],
                                   chromosome_1_copy[1][3],
                                   chromosome_1_copy[1][4], chromosome_1_copy[1][5], chromosome_1_copy[1][6],
                                   chromosome_1_copy[1][7],
                                   chromosome_1_copy[1][8],
                                   chromosome_1_copy[1][9], chromosome_1_copy[1][10], chromosome_1_copy[1][11],
                                   chromosome_1_copy[1][12],
                                   chromosome_1_copy[1][13], chromosome_1_copy[1][14], chromosome_1_copy[1][15],
                                   chromosome_1_copy[1][16],
                                   chromosome_1_copy[1][17]
                                   )
    chromosome_2_copy[0] = fitness(chromosome_2_copy[1][0], chromosome_2_copy[1][1], chromosome_2_copy[1][2],
                                   chromosome_2_copy[1][3],
                                   chromosome_2_copy[1][4], chromosome_2_copy[1][5], chromosome_2_copy[1][6],
                                   chromosome_2_copy[1][7],
                                   chromosome_2_copy[1][8],
                                   chromosome_2_copy[1][9], chromosome_2_copy[1][10], chromosome_2_copy[1][11],
                                   chromosome_2_copy[1][12],
                                   chromosome_2_copy[1][13], chromosome_2_copy[1][14], chromosome_2_copy[1][15],
                                   chromosome_2_copy[1][16],
                                   chromosome_2_copy[1][17])

    # replace in low fitting
    print('offsprings:')
    print(fitness_and_chromosome1)
    print('X')
    print(fitness_and_chromosome2)
    print('↓')
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
    for _ in range(int(random.uniform(1, 6))):  # random mutating energy hitting (1 to 5) alleles in a chromosome
        list_of_random_genes_to_mutate.append(int(random.uniform(0, 18)))
    for random_gene_number in list_of_random_genes_to_mutate:
        chromosome_copy[1][random_gene_number] = random.uniform(0, FORCE)
        # chromosome_copy[1][random_gene_number] = random.uniform(chromosome_copy[1][random_gene_number],400)


    # recalculate fitness
    chromosome_copy[0] = fitness(chromosome_copy[1][0], chromosome_copy[1][1], chromosome_copy[1][2],
                                 chromosome_copy[1][3],
                                 chromosome_copy[1][4], chromosome_copy[1][5], chromosome_copy[1][6],
                                 chromosome_copy[1][7],
                                 chromosome_copy[1][8], chromosome_copy[1][9], chromosome_copy[1][10],
                                 chromosome_copy[1][11],
                                 chromosome_copy[1][12],
                                 chromosome_copy[1][13], chromosome_copy[1][14], chromosome_copy[1][15],
                                 chromosome_copy[1][16],
                                 chromosome_copy[1][17])

    # replace
    print('mutant:')
    print(fitness_and_chromosome)
    print('↓')
    fitness_and_chromosome_to_replace[0] = chromosome_copy[0]
    fitness_and_chromosome_to_replace[1] = chromosome_copy[1]
    print(fitness_and_chromosome_to_replace)



# generate random chromosomes
chromosomes = []
for _ in range(POPULATION):
    chromosomes.append(
        [random.uniform(0, FORCE), random.uniform(0, FORCE), random.uniform(0, FORCE), random.uniform(0, FORCE),
         random.uniform(0, FORCE), random.uniform(0, FORCE), random.uniform(0, FORCE), random.uniform(0, FORCE),
         random.uniform(0, FORCE), random.uniform(0, FORCE), random.uniform(0, FORCE), random.uniform(0, FORCE),
         random.uniform(0, FORCE), random.uniform(0, FORCE), random.uniform(0, FORCE), random.uniform(0, FORCE),
         random.uniform(0, FORCE), random.uniform(0, FORCE) ])

# calculate fitness for each chromosome and sort them by
chromosomes_ranked_by_fitness = []
fitnessValue = None

print('fitness values for each chromosome in the initial random population:')
for chromosome in chromosomes:
    fitnessValue = fitness(chromosome[0], chromosome[1], chromosome[2], chromosome[3], chromosome[4], chromosome[5],
                           chromosome[6], chromosome[7], chromosome[8], chromosome[9], chromosome[10], chromosome[11],
                           chromosome[12], chromosome[13], chromosome[14],
                           chromosome[15], chromosome[16], chromosome[17])
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

    chromosomes_ranked_by_fitness = apply_rank_based_selection(chromosomes_ranked_by_fitness)

    print('right after selection process:')
    for chromosome in chromosomes_ranked_by_fitness[:FIRST_CHROMOSOMES_TO_VIEW]:
        print(chromosome)

    for _ in range(CROSS_OVERS_A_GENERATION):
        while True:
            random_chromosome_1 = int(random.uniform(0, POPULATION))
            random_chromosome_2 = int(random.uniform(0, POPULATION))

            if copy.deepcopy(chromosomes_ranked_by_fitness[random_chromosome_1]) != copy.deepcopy(chromosomes_ranked_by_fitness[random_chromosome_2]):
                crossover(chromosomes_ranked_by_fitness[random_chromosome_1],
                          chromosomes_ranked_by_fitness[random_chromosome_2],
                          chromosomes_ranked_by_fitness[random_chromosome_1],
                          chromosomes_ranked_by_fitness[random_chromosome_2])
                break




    print('right after cross-over process:')
    for chromosome in chromosomes_ranked_by_fitness[:FIRST_CHROMOSOMES_TO_VIEW]:
        print(chromosome)

    for _ in range(MUTATIONS_A_GENERATION):
        random_chromosome = int(random.uniform(0, POPULATION))
        mutate(chromosomes_ranked_by_fitness[random_chromosome],
               chromosomes_ranked_by_fitness[random_chromosome])

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
