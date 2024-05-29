from Algorithm import Algorithm
import Configuration
from Schedule import Schedule


prototype = Schedule(3, 3, 75, 4)
instance = Algorithm(100, 8, 5, prototype)
instance.Start()
bestChromosome = instance.GetBestChromosome()
classes = bestChromosome.GetClasses()
print(classes)