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
	
        if number_chromosomes < 2:
            number_chromosomes = 2
        if track_best < 1:
            track_best = 1

        if self.replaceByGeneration < 1:
            self.replaceByGeneration = 1
        elif self.replaceByGeneration > number_chromosomes - track_best:
            self.replaceByGeneration = number_chromosomes - track_best
    
        self.chromosomes = number_chromosomes * [None]
        self.bestFlags = number_chromosomes * [False]

        # reserve space for best chromosome group
        self.bestChromosomes = track_best * [None]

    
    def GetInstance():
        prototype = Schedule(3, 3, 75, 4)
        instance = Algorithm(100, 10, 10, prototype)
        return instance
    
    def Start(self):
        for cur in range(len(self.chromosomes)):
            if self.chromosomes[cur]:
                del self.chromosomes[cur]

            self.chromosomes[cur] = self.prototype.MakeNewFromPrototype()
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
            for j in range(0, self.replaceByGeneration):
                a = randint(0, 400000) % lengthOfChromosomes
                b = randint(0, 400000) % lengthOfChromosomes
                p1 = self.chromosomes[a]
                p2 = self.chromosomes[b]
                offspring[j] = p1.Crossover(p2)
                offspring[j].Mutation()

            for j in range(0, self.replaceByGeneration):
                chromosome_index = randint(0, 40000) % len(self.chromosomes)
                while (self.IsInBest(chromosome_index)):
                    chromosome_index = randint(0, 40000) % len(self.chromosomes)

                self.chromosomes[chromosome_index] = offspring[j]

                # try to add new chromosomes in best chromosome group
                self.AddToBest(chromosome_index)

            self.currentGeneration = self.currentGeneration + 1

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
            # group is not full?
            if i < len(self.bestChromosomes):
                if  self.chromosomes[self.bestChromosomes[i - 1 ]].GetFitness() > self.chromosomes[chromosome_index].GetFitness():
                    j = i
                    break

                # move chromosomes to make room for new
                self.bestChromosomes[i] = self.bestChromosomes[i - 1]
            else:
                # group is full remove worst chromosomes in the group
                self.bestFlags[ self.bestChromosomes[i - 1]] = False
            j = i - 1

        self.bestChromosomes[j] = chromosome_index
        self.bestFlags[chromosome_index] = True
        
        if self.currentBestSize < len(self.bestChromosomes):
            self.currentBestSize = self.currentBestSize + 1


    def IsInBest(self, chromosomeIndex):
        return self.bestFlags[chromosomeIndex]


    def ClearBest(self):
        for i in range(len(self.bestFlags), -1, -1):
            self.bestFlags[i] = False
        self.currentBestSize = 0
    
