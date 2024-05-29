from Algorithm import Algorithm
import Configuration
from Schedule import Schedule

'''
prototype = Schedule(3, 3, 75, 4)
instance = Algorithm(100, 8, 5, prototype)
bestChromosome = instance.Start()
print("best", bestChromosome.GetFitness(), bestChromosome.score)
'''

instance = Configuration.Configuration()

instance.readcsv()
print(instance.GetNumberOfCourseClasses())