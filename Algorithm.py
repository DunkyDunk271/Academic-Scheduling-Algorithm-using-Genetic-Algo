import Schedule
import random
from random import randint

# Number of Studying day in a week
DAYS_NUM = 5

# Number of hours in a day
DAY_HOURS = 8

class Algorithm:
    def __init__(self, number_chromosomes, replacement, track_best, prototype):
        self.replaceByGeneration = replacement
        self.prototype = prototype
        self.currentBestSize = 0
        self.currentGeneration = 0

        self.numberChromosomes = number_chromosomes
        if number_chromosomes < 2:
            self.numberChromosomes = 2

        self.trackBest = track_best
        if track_best < 1:
            self.trackBest = 1

        if self.replaceByGeneration < 1:
            self.replaceByGeneration = 1
        elif self.replaceByGeneration > self.numberChromosomes - self.trackBest:
            self.replaceByGeneration = self.numberChromosomes - self.trackBest

        self.chromosomes = []
        self.bestFlags = []
        self.bestChromosomes = []
        self.Initialize()

    def Initialize(self):
        self.chromosomes = []
        self.bestFlags = []
        self.bestChromosomes = []
        self.chromosomes = self.numberChromosomes * [None]
        self.bestFlags = self.numberChromosomes * [False]
        self.bestChromosomes = self.trackBest * [None]

    
    def GetInstance():
        prototype = Schedule(2, 3, 75, 5)
        instance = Algorithm(100, 10, 10, prototype)
        return instance
    
    
    def Generate(self):
        for cur in range(len(self.chromosomes)):
            if self.chromosomes[cur]:
                del self.chromosomes[cur]

            self.chromosomes[cur] = self.prototype.SampleFromPrototype()
            self.AddToBest(cur)

        self.currentGeneration = 0
        random.seed()
        lengthOfChromosomes = len(self.chromosomes)

        while 1:
            best = self.GetBestChromosome()

            # algorithm has reached criteria?
            if best.GetFitness() >= 1:
                print("best", best.GetFitness(), best.score)
                break

            # produce offspring
            offspring = self.replaceByGeneration * [None]
            for j in range(self.replaceByGeneration):
                a = randint(0, lengthOfChromosomes - 1)
                b = randint(0, lengthOfChromosomes - 1)
                p1 = self.chromosomes[a]
                p2 = self.chromosomes[b]
                offspring[j] = p1.Crossover(p2)
                offspring[j].Mutation()

            for j in range(self.replaceByGeneration):
                chromosome_index = randint(0, len(self.chromosomes) - 1)
                while (self.IsInBest(chromosome_index)):
                    chromosome_index = randint(0, len(self.chromosomes) - 1)

                self.chromosomes[chromosome_index] = offspring[j]

                # try to add new chromosomes in best chromosome group
                self.AddToBest(chromosome_index)

            self.currentGeneration += 1


    # Keep track the path
    def reverse_algo(self):
        path = []
        for cur in range(len(self.chromosomes)):
            if self.chromosomes[cur]:
                path.append(self.chromosomes[:])
                del self.chromosomes[cur]

            self.chromosomes[cur] = self.prototype.SampleFromPrototype()
            self.AddToBest(cur)
            path.append(self.chromosomes[:])
        return path


    def GetBestChromosome(self):
        return self.chromosomes[self.bestChromosomes[0]]


    def AddToBest(self, chromosome_index):
        if self.currentBestSize == len(self.bestChromosomes):
            if self.chromosomes[self.bestChromosomes[self.currentBestSize - 1]].GetFitness() >= self.chromosomes[chromosome_index].GetFitness():
              return

        if self.IsInBest(chromosome_index):
            return
        
        i = self.currentBestSize
        j = 0
       
        for i in range(self.currentBestSize, 0, -1):
            if i < len(self.bestChromosomes):
                if  self.chromosomes[self.bestChromosomes[i - 1]].GetFitness() > self.chromosomes[chromosome_index].GetFitness():
                    j = i
                    break
                # Make room for new chromosome
                self.bestChromosomes[i] = self.bestChromosomes[i - 1]
            else:
                # Remove the worst chromosome
                self.bestFlags[self.bestChromosomes[i - 1]] = False
            j = i - 1

        self.bestChromosomes[j] = chromosome_index
        self.bestFlags[chromosome_index] = True
        
        if self.currentBestSize < len(self.bestChromosomes):
            self.currentBestSize = self.currentBestSize + 1

    def IsInBest(self, chromosomeIndex):
        return self.bestFlags[chromosomeIndex]
    
