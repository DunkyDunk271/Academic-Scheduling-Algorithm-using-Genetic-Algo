import random
from collections import OrderedDict

class GeneticAlgorithm:

    def __init__(self, population_size, mutation_rate, crossover_rate, elitism_count, tournament_size):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.elitism_count = elitism_count
        self.tournament_size = tournament_size
        self.temperature = 1.0
        self.fitness_hash = OrderedDict()

    def init_population(self, schedule):
        population = Population(self.population_size, schedule)
        return population

    def is_termination_condition_met(self, generations_count, max_generations):
        return generations_count > max_generations

    def is_termination_condition_met_population(self, population):
        return population.get_fittest(0).get_fitness() == 1.0

    def calc_fitness(self, individual, schedule):
        if individual in self.fitness_hash:
            return self.fitness_hash[individual]

        thread_schedule = Schedule(schedule)
        thread_schedule.create_univ_classes(individual)

        clashes = thread_schedule.calc_clashes()
        fitness = 1 / (clashes + 1)

        individual.set_fitness(fitness)
        self.fitness_hash[individual] = fitness

        return fitness

    def eval_population(self, population, schedule):
        for i in range(population.size()):
            self.calc_fitness(population.get_individual(i), schedule)

        population_fitness = sum(self.calc_fitness(ind, schedule) for ind in population.get_individuals())
        population.set_population_fitness(population_fitness)

    def select_parent(self, population):
        tournament = Population(self.tournament_size)
        population.shuffle()

        for i in range(self.tournament_size):
            tournament.set_individual(i, population.get_individual(i))

        return tournament.get_fittest(0)

    def crossover_population(self, population):
        new_population = Population(population.size())

        for population_index in range(population.size()):
            parent1 = population.get_fittest(population_index)

            if self.crossover_rate > random.random() and population_index >= self.elitism_count:
                offspring = Individual(parent1.get_chromosome_length())
                parent2 = self.select_parent(population)

                for gene_index in range(parent1.get_chromosome_length()):
                    if 0.5 > random.random():
                        offspring.set_gene(gene_index, parent1.get_gene(gene_index))
                    else:
                        offspring.set_gene(gene_index, parent2.get_gene(gene_index))

                new_population.set_individual(population_index, offspring)
            else:
                new_population.set_individual(population_index, parent1)

        return new_population

    def mutate_population(self, population, schedule):
        new_population = Population(self.population_size)
        best_fitness = population.get_fittest(0).get_fitness()

        for population_index in range(population.size()):
            individual = population.get_fittest(population_index)
            random_individual = Individual(schedule)

            adaptive_mutation_rate = self.mutation_rate
            if individual.get_fitness() > population.get_avg_fitness():
                fitness_delta1 = best_fitness - individual.get_fitness()
                fitness_delta2 = best_fitness - population.get_avg_fitness()
                adaptive_mutation_rate = (fitness_delta1 / fitness_delta2) * self.mutation_rate

            for gene_index in range(individual.get_chromosome_length()):
                if population_index > self.elitism_count:
                    if (adaptive_mutation_rate * self.get_temperature()) > random.random():
                        individual.set_gene(gene_index, random_individual.get_gene(gene_index))

            new_population.set_individual(population_index, individual)

        return new_population

    def get_temperature(self):
        return self.temperature

    def set_temperature(self, temperature):
        self.temperature = temperature

# Example placeholder classes for Population, Individual, Schedule
class Population:
    def __init__(self, size, schedule=None):
        self.individuals = [Individual() for _ in range(size)]
        self.population_fitness = 0

    def size(self):
        return len(self.individuals)

    def get_individual(self, index):
        return self.individuals[index]

    def set_individual(self, index, individual):
        self.individuals[index] = individual

    def get_individuals(self):
        return self.individuals

    def get_fittest(self, index):
        self.individuals.sort(key=lambda x: x.get_fitness(), reverse=True)
        return self.individuals[index]

    def set_population_fitness(self, fitness):
        self.population_fitness = fitness

    def get_avg_fitness(self):
        return self.population_fitness / len(self.individuals)

    def shuffle(self):
        random.shuffle(self.individuals)

class Individual:
    def __init__(self, chromosome_length=10):
        self.chromosome = [random.randint(0, 1) for _ in range(chromosome_length)]
        self.fitness = -1

    def get_chromosome_length(self):
        return len(self.chromosome)

    def get_gene(self, index):
        return self.chromosome[index]

    def set_gene(self, index, value):
        self.chromosome[index] = value

    def get_fitness(self):
        return self.fitness

    def set_fitness(self, fitness):
        self.fitness = fitness

class Schedule:
    def __init__(self, schedule=None):
        pass

    def create_univ_classes(self, individual):
        pass

    def calc_clashes(self):
        return random.randint(0, 10)
