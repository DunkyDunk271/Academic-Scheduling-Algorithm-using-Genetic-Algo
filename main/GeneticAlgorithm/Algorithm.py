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
        if trackBest < 1:
            trackBest = 1

        if self.replaceByGeneration < 1:
            self.replaceByGeneration = 1
        elif self.replaceByGeneration > number_chromosomes - track_best:
            self.replaceByGeneration = number_chromosomes - track_best
    
        self.chromosomes = number_chromosomes * [None]
        self.bestFlags = number_chromosomes * [False]

        # reserve space for best chromosome group
        self.bestChromosomes = trackBest * [None]