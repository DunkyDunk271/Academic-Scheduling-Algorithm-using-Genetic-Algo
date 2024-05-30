from Configuration import Configuration
from random import randint

# Number of Studying day in a week
DAYS_NUM = 5

# Number of hours in a day
DAY_HOURS = 8

# Get instance of configuration
instance = Configuration()
instance.readcsv()

# Schedule Choromsome
class Schedule:

    def __init__(self, num_crossoverPoints, mutation_size, crossover_probability, mutation_probability):
            # Number of crossover points of parent's class tables
            self.numberOfCrossoverPoints = num_crossoverPoints
            # Number of classes that is moved randomly by single mutation operation
            self.mutationSize = mutation_size
            # Probability that crossover will occure
            self.crossoverProbability = crossover_probability
            # Probability that mutation will occure
            self.mutationProbability = mutation_probability
            # Fitness value of chromosome
            self.fitness = 0
            # Timeslots, one entry represent one hour in one classroom
            self.slots = []
            # Flags of class requirements satisfaction
            self.criteria = []

            self.score = 0
            
            self.classes = {}
            
            self.slots = ( DAYS_NUM * DAY_HOURS * instance.GetNumberOfRooms() ) * [None]
            self.criteria = (instance.GetNumberOfCourseClasses() * 5 )* [None]

    def GetClasses(self):
        return self.classes
    
    def copy(self, not_null = False):
        c = Schedule(0, 0, 0, 0)
        
        if not_null == False:
            c.slots = self.slots
            c.classes = self.classes
            c.criteria = self.criteria
            c.fitness = self.fitness
        else:
            c.slots = ( DAYS_NUM * DAY_HOURS * instance.GetNumberOfRooms() ) * [None]
            c.criteria = ( instance.GetNumberOfCourseClasses() * 5 ) * [None]

        # copy parameters
        c.numberOfCrossoverPoints = self.numberOfCrossoverPoints
        c.mutationSize = self.mutationSize
        c.crossoverProbability = self.crossoverProbability
        c.mutationProbability = self.mutationProbability
        c.score = self.score

        return c
    

    def MakeNewFromPrototype(self):
            cur_chromosome = self.copy(True)

            # place classes at random position
            cur_class = instance.GetCourseClasses()
            num_room = instance.GetNumberOfRooms()
            
            for cur in cur_class:
                # determine random position of class
                dur = cur.GetDuration()
                
                day = randint(0, 40000) % DAYS_NUM
                room = randint(0, 40000) % num_room
                time = randint(0, 40000) % (DAY_HOURS + 1 - dur)

                pos = day * num_room * DAY_HOURS + room * DAY_HOURS + time
                cur_chromosome.classes[cur] = pos
                        
                # fill time-space slots, for each hour of class
                for i in range(dur - 1, -1, -1):
                    if cur_chromosome.slots[pos + i] is None:
                        cur_chromosome.slots[pos + i] = [cur]
                    else:
                        cur_chromosome.slots[pos + i].append(cur)

                # insert in class table of chromosome
                cur_chromosome.classes[cur] = pos

            cur_chromosome.CalculateFitness()

            return cur_chromosome
    
    # Can be changed
    # Performes crossover operation using two chromosomes and returns pointer to offspring
    def Crossover(self, par_chromosome_2):
        if randint(0, 40000) % 100 > self.crossoverProbability:
            # if probability > cur.crossoverProb => no crossover, just copy first parent
            return self.copy(False)

        size = len(self.classes)
        crossover_point = size * [None]

        cur_chromosome = self.copy(True)

        # determine crossover point (randomly)
        for i in range(self.numberOfCrossoverPoints, 0, -1):
            while 1:
                p = randint(0, 40000) % size
                if (not crossover_point[p]):
                    crossover_point[p] = True
                    break
        
        # make new code by combining parent codes
        first = randint(0, 1) == 0
        j = 0
        for i in range(0, size):
            if first:
                # insert class from first parent into new chromosome's class table
                if j >= len(list(self.classes.keys())):
                        break
                it1 = self.classes[list(self.classes.keys())[j]]
                cur_chromosome.classes[ list(self.classes.keys())[j]] = it1
                
                for k in range(list(self.classes.keys())[j].GetDuration() - 1, -1, -1):
                    if cur_chromosome.slots[it1 + k] is None:
                        cur_chromosome.slots[it1 + k] = [list(self.classes.keys())[j]]
                    else:
                        cur_chromosome.slots[it1 + k].append(list(self.classes.keys())[j])
            else:
                # insert class from second parent into new chromosome's class table
                if j >= len(list(par_chromosome_2.classes.keys())):
                        break
                it2 = par_chromosome_2.classes[ list(par_chromosome_2.classes.keys())[j]]
                cur_chromosome.classes[list(par_chromosome_2.classes.keys())[ j ]] = it2

                for k in range(list(par_chromosome_2.classes.keys())[ j ].GetDuration() - 1, -1, -1):
                    if cur_chromosome.slots[ it2 + k ] is None:
                        cur_chromosome.slots[ it2 + k ] = [list(par_chromosome_2.classes.keys())[ j ]]
                    else:
                        cur_chromosome.slots[ it2 + k ].append(list(par_chromosome_2.classes.keys())[ j ])

            # crossover point
            if crossover_point[i]:
                first = not first

            j = j + 1

        cur_chromosome.CalculateFitness()

        return cur_chromosome
    

    def Mutation(self):
        if randint(0, 40000) % 100 > self.mutationProbability:
            return None

        
        num_classes = len(self.classes)

        # move selected number of classes at random position
        for _ in range(self.mutationSize, 0, -1):
            move_pos = randint(0, 40000) % num_classes
            pos1 = self.classes[list(self.classes.keys())[move_pos]]
            cur = list(self.classes.keys())[move_pos]
            cur_class_1 = cur

            # Randomize Class position
            num_room = instance.GetNumberOfRooms()
            dur = cur_class_1.GetDuration()
            day = randint(0, 40000) % DAYS_NUM
            room = randint(0, 40000) % num_room
            time = randint(0, 40000) % (DAY_HOURS + 1 - dur)
            pos2 = day * num_room * DAY_HOURS + room * DAY_HOURS + time

            # move timeslots
            for j in range(dur - 1, -1, -1):
                c1 = self.slots[pos1 + j]
                for k in range(0, len(c1)):
                    if c1[k] == cur_class_1:
                        del c1[k]
                        break

                    # move class hour to new time-space slot
                if self.slots[ pos2 + j ] is None:
                    self.slots[ pos2 + j ] = [cur_class_1]
                else:
                    self.slots[ pos2 + j ].append(cur_class_1)

            # change entry of class table to point to new time-space slots
            self.classes[cur_class_1] = pos2
        
        self.CalculateFitness()

    # Can be changed
    # Calculates fitness value of chromosome
    def CalculateFitness(self):
        score = 0
        numberOfRooms = instance.GetNumberOfRooms()
        daySize = DAY_HOURS * numberOfRooms

        ci = 0

        for i in self.classes.keys():
            p = self.classes[i]
            day = p // daySize
            time = p % daySize
            room = time // DAY_HOURS
            time = time % DAY_HOURS

            dur = i.GetDuration()

            # check for room overlapping of classes
            ro = False
            for j in range( dur - 1, -1, -1 ):
                if len( self.slots[ p + j ] ) > 1:
                    ro = True
                    break

            # on room overlapping
            if not ro:
                score = score + 1

            self.criteria[ ci + 0 ] = not ro
                
            cc = i
            r = instance.GetRoomById( room )
            # does current room have enough seats
            self.criteria[ci + 1] = r.GetNumberOfSeats() >= cc.GetNumberOfSeats()
            if self.criteria[ ci + 1 ]:
                score = score + 1

            # does current room have computers if they are required
            self.criteria[ ci + 2 ] = (not cc.IsLabRequired()) or (cc.IsLabRequired() and r.IsLab())
            if self.criteria[ci + 2]:
                score = score + 1

            po = False
            go = False
            # check overlapping of classes for professors and student groups
            t = day * daySize + time
            breakPoint = False
            for k in range(numberOfRooms, 0, -1):
                if breakPoint == True: break
                # for each hour of class
                for l in range( dur - 1, -1, -1 ):
                    if breakPoint == True: break
                    # check for overlapping with other classes at same time
                    cl = self.slots[ t + l ]
                    if not cl is None:
                        for it in cl:
                            if breakPoint == True: break
                            if cc != it:
                                # professor overlaps?
                                if not po and cc.ProfessorOverlaps(it):
                                    po = True
                                # student group overlaps?
                                if not go and cc.GroupsOverlap(it):
                                    go = True
                                # both type of overlapping? no need to check more
                                if po and go:
                                    breakPoint = True
                                                    
                t = t + DAY_HOURS
            # professors have no overlapping classes?
            if not po:
                score = score + 1
            self.criteria[ci + 3] = not po

            # student groups has no overlapping classes?
            if not go:
                score = score + 1
            self.criteria[ci + 4] = not go

            ci += 5

        # calculate fitness value based on score
        self.fitness = score / (instance.GetNumberOfCourseClasses() * DAYS_NUM)
        self.score = score

    # Returns fitness value of chromosome
    def GetFitness(self):
        return self.fitness