import random
import copy
import physics

FORCE = 1000000
POPULATION = 20 # last two will be used as holders
REPRODUCTIVE_POPULATION = POPULATION - 2
GENERATIONS = 40000
CROSS_OVERS_A_GENERATION = 4
MUTATIONS_A_GENERATION = 6
FIRST_CHROMOSOMES_TO_VIEW = 20


def fitness(a, a1, a2, b, b1, b2, c, c1, c2):
    return physics.manifest(a, a1, a2, b, b1, b2, c, c1, c2)


def crossover(fitness_and_chromosome1, fitness_and_chromosome2, fitness_and_chromosome1_to_replace,
              fitness_and_chromosome2_to_replace):
    random_gene_number = int(random.uniform(1, 9))
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
                                   chromosome_1_copy[1][8])
    chromosome_2_copy[0] = fitness(chromosome_2_copy[1][0], chromosome_2_copy[1][1], chromosome_2_copy[1][2],
                                   chromosome_2_copy[1][3],
                                   chromosome_2_copy[1][4], chromosome_2_copy[1][5], chromosome_2_copy[1][6],
                                   chromosome_2_copy[1][7],
                                   chromosome_2_copy[1][8])

    # replace in low fitting
    # only if the offsprings ain't the same as the parents
    print('offsprings:')
    print(fitness_and_chromosome1)
    print('X')
    print(fitness_and_chromosome2)
    print('↓')
    if chromosome_1_copy not in chromosomes_ranked_by_fitness[:REPRODUCTIVE_POPULATION]:
        fitness_and_chromosome1_to_replace[0] = chromosome_1_copy[0]
        fitness_and_chromosome1_to_replace[1] = chromosome_1_copy[1]
        print(fitness_and_chromosome1_to_replace)
        print('||')
    else:
        print('offspring 1 dismissed to avoid recurrence')
    if chromosome_2_copy not in chromosomes_ranked_by_fitness[:REPRODUCTIVE_POPULATION]:
        fitness_and_chromosome2_to_replace[0] = chromosome_2_copy[0]
        fitness_and_chromosome2_to_replace[1] = chromosome_2_copy[1]
        print(fitness_and_chromosome2_to_replace)
    else:
        print('offspring 2 dismissed to avoid recurrence')


# ##### you can remove that [0] from the if-condition in upcoming problems ####### this is a special problem where
# many chromosomes may be different from each other (with only a single common portion of alleles) and still
# considered as the same, proven by the fitness value, as the common portion only have the effect. in more detail,
# in a set of chromosomes with a common portion, the common portion raises a common movement that hit the ball the
# same way, whereas the chromosome raises two other completely different movements from the two movements of the
# other chromosomes in the set. these two movements are far away from the effect, the time of it, and the ball it is
# needed to avoid recurrence in the population, so there is diversity in the -fittest- chromosomes so offsprings are
# not the same as parents, so the search is not stuck to the same solutions only waiting for mutation that might free
# it out to a fitter solution. the process then is all about random mutation which opposes the genetic algorithm
# concept. and, as our special individuals may sound different while they have the same exact effect on the ball
# resulting in same fitness value, it is decided to compare the individuals by the fitness value that represents the
# effect on the ball, instead of the alleles, to avoid recurrence. but in upcoming problems where fitness is
# affected, most of the time, by whole chromosome, you can remove this [0]

# again: at cross-over between 2 of the most fitting, there can be an offspring with good fitness (same as
# parents') whose alleles are changed except a certain portion (the common portion between the parents) that has all
# the effect on the ball, and hence on fitness. it would be then considered as a new well-fitting solution and be
# included to the most fitting chromosomes, from which chromosomes are picked for further cross-over, leading to have
# the best solutions in hand having the same effect but still not avoided as they are not the same -only that
# effecting part is in common- and are thought to be different good solutions to pick from for cross over,
# and when this happens nothing better is obtained from two chromosomes with same effect but the same effect or
# worse, except in rare cases where non-affecting alleles are combined to give a good effecting part(s) by chance

# as for mutation, it is like impossible to have a mutant with the same alleles as any other chromosome, but,
# as discussed, mutation may only occur to the non-effecting part to come up with a new solution with the same effect
# that is not avoided, introducing the same issue, and solved by same solution

# generally, it will be better to compare the new chromosome to each chromosome in the reproductive set (cross-over
# and mutation) for the avoidance rather than compare to only the chromosome of the origin, to avoid any chance of
# finding the same solution (a solution different from parent but still found). the risk of this, increases with more
# tight reproductive set, but this would be computationally expensive. we do not want to push real good solutions
# back to have just fake recurring solutions (with the common part) on top to reproduce thinking they may come up
# with something better or, at least, new, and instead just coming up with more recurrences, which are usually
# dismissed here, but there still is a chance as mentioned (and then it should not be always about a common effecting
# part). we want the real different good solutions to be there, for more diversity, so they are picked for cross over
# to come up with real new solutions, and then it is not all about mutation freeing it out of same parents producing
# same offsprings.


def mutate(fitness_and_chromosome, fitness_and_chromosome_to_replace):
    # copy
    chromosome_copy = copy.deepcopy(fitness_and_chromosome)
    # mutate a randomized gene

    # #create list of randomized gene numbers
    # random_gene_numbers = []
    # for _ in range(int(random.uniform(1, max_number_of_genes_to_mutate))):
    #     random_gene_numbers.append(int(random.uniform(0, 9)))
    #
    # print(random_gene_numbers)

    for random_gene_number in [int(random.uniform(0, 9))]:
        if random_gene_number in [0, 3, 6]:
            chromosome_copy[1][random_gene_number] = int(random.uniform(1, 180))
        else:
            chromosome_copy[1][random_gene_number] = random.uniform(-FORCE, FORCE)

    # recalculate fitness
    chromosome_copy[0] = fitness(chromosome_copy[1][0], chromosome_copy[1][1], chromosome_copy[1][2],
                                 chromosome_copy[1][3], chromosome_copy[1][4], chromosome_copy[1][5],
                                 chromosome_copy[1][6], chromosome_copy[1][7], chromosome_copy[1][8])

    # replace
    # only if the mutant isn't the same
    print('mutant:')
    print(fitness_and_chromosome)
    print('↓')
    if chromosome_copy not in chromosomes_ranked_by_fitness[:REPRODUCTIVE_POPULATION]:
        fitness_and_chromosome_to_replace[0] = chromosome_copy[0]
        fitness_and_chromosome_to_replace[1] = chromosome_copy[1]
        print(fitness_and_chromosome_to_replace)
    else:
        print('mutant dismissed to avoid recurrence')


# ##### you can remove that [0] from the if-condition in upcoming problems ######
# ##### or reduce time range of the three movements, so they are closer to each other to be all affecting and contributing ######

# generate random chromosomes
chromosomes = []
for _ in range(POPULATION):
    chromosomes.append([int(random.uniform(1, 180)), random.uniform(-FORCE, FORCE), random.uniform(-FORCE, FORCE),
                        int(random.uniform(1, 180)), random.uniform(-FORCE, FORCE), random.uniform(-FORCE, FORCE),
                        int(random.uniform(1, 180)), random.uniform(-FORCE, FORCE), random.uniform(-FORCE, FORCE)])

# calculate fitness for each chromosome and sort them by
chromosomes_ranked_by_fitness = []
fitnessValue = None

print('fitness values for each chromosome in the initial random population:')
for chromosome in chromosomes:
    fitnessValue = fitness(chromosome[0], chromosome[1], chromosome[2], chromosome[3], chromosome[4], chromosome[5],
                           chromosome[6], chromosome[7], chromosome[8])
    chromosomes_ranked_by_fitness.append([fitnessValue, chromosome])
    print(fitnessValue)

chromosomes_ranked_by_fitness.sort()
chromosomes_ranked_by_fitness.reverse()

print('Gen', 0, '  (fittest ', FIRST_CHROMOSOMES_TO_VIEW, ')')

for chromosome in chromosomes_ranked_by_fitness[:FIRST_CHROMOSOMES_TO_VIEW]:
    print(chromosome)

for i in range(1, GENERATIONS):

    for _ in range(CROSS_OVERS_A_GENERATION):
        crossover(chromosomes_ranked_by_fitness[int(random.uniform(0, REPRODUCTIVE_POPULATION))],
                  chromosomes_ranked_by_fitness[int(random.uniform(0, REPRODUCTIVE_POPULATION))],
                  chromosomes_ranked_by_fitness[-1],
                  chromosomes_ranked_by_fitness[-2],
                  )

        chromosomes_ranked_by_fitness.sort()
        chromosomes_ranked_by_fitness.reverse()

    for _ in range(MUTATIONS_A_GENERATION):
        mutate(chromosomes_ranked_by_fitness[int(random.uniform(0, REPRODUCTIVE_POPULATION))],
               chromosomes_ranked_by_fitness[-1]
               )

        chromosomes_ranked_by_fitness.sort()
        chromosomes_ranked_by_fitness.reverse()

    print('Gen', i, '  (fittest ', FIRST_CHROMOSOMES_TO_VIEW, ')')

    for chromosome in chromosomes_ranked_by_fitness[:FIRST_CHROMOSOMES_TO_VIEW]:
        print(chromosome)
