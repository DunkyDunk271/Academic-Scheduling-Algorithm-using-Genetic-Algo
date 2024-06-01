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
            self.numberOfCrossoverPoints = num_crossoverPoints
            self.mutationSize = mutation_size
            self.crossoverProbability = crossover_probability
            self.mutationProbability = mutation_probability
            self.fitness = 0

            self.score = 0
            self.classes = {}
            
            # Time-space slots
            self.slots = []
            # Hard Constraints
            self.criteria = []

            self.Initialzie()

    def Initialzie(self):
        self.slots = []
        self.criteria = []
        self.slots = ( DAYS_NUM * DAY_HOURS * instance.GetNumberOfRooms() ) * [None]
        self.criteria = (instance.GetNumberOfCourseClasses() * 5 )* [None]

    def GetClasses(self):
        return self.classes
    
    def copy(self, not_null = False):
        cur = Schedule(self.numberOfCrossoverPoints, self.mutationSize, self.crossoverProbability, self.mutationProbability)
        cur.score = self.score

        if not_null == False:
            cur.slots = self.slots
            cur.classes = self.classes
            cur.criteria = self.criteria
            cur.fitness = self.fitness
        else:
            cur.Initialzie()

        return cur
    

    def SampleFromPrototype(self):
        cur_chromosome = self.copy(True)

        # Place classes at random position
        cur_class = instance.GetCourseClasses()
        num_room = instance.GetNumberOfRooms()
            
        for cur in cur_class:
            dur = cur.GetDuration()
            day = randint(0, DAYS_NUM - 1)
            room = randint(0, num_room - 1)
            time = randint(0, DAY_HOURS - dur)

            pos = day * num_room * DAY_HOURS + room * DAY_HOURS + time
            cur_chromosome.classes[cur] = pos
                        
            for i in range(dur):
                if cur_chromosome.slots[pos + i] is None:
                    cur_chromosome.slots[pos + i] = [cur]
                else:
                    cur_chromosome.slots[pos + i].append(cur)

            # Insert in class table of chromosome
            cur_chromosome.classes[cur] = pos

        cur_chromosome.CalculateFitness()

        return cur_chromosome
    
    def Crossover(self, par_chromosome_2):
        if randint(0, 200) > self.crossoverProbability:
            return self.copy(False)

        size = len(self.classes)
        crossover_point = size * [None]
        cur_chromosome = self.copy(True)

        for i in range(self.numberOfCrossoverPoints):
            while 1:
                p = randint(0, size - 1)
                if (not crossover_point[p]):
                    crossover_point[p] = True
                    break
        
        # Create child chromosome from parents
        is_first = randint(0, 1)
        j = 0
        for i in range(size):
            if is_first == 0:
                # Choose first parent
                if j >= len(list(self.classes.keys())):
                        break
                
                id = list(self.classes.keys())[j]
                cur1 = self.classes[id]
                cur_chromosome.classes[id] = cur1
                
                for k in range(id.GetDuration()):
                    if cur_chromosome.slots[cur1 + k] is None:
                        cur_chromosome.slots[cur1 + k] = [id]
                    else:
                        cur_chromosome.slots[cur1 + k].append(id)
            else:
                # Choose second parent
                if j >= len(list(par_chromosome_2.classes.keys())):
                        break
                
                id = list(par_chromosome_2.classes.keys())[j]
                cur2 = par_chromosome_2.classes[id]
                cur_chromosome.classes[id] = cur2

                for k in range(id.GetDuration()):
                    if cur_chromosome.slots[cur2 + k] is None:
                        cur_chromosome.slots[cur2 + k] = [id]
                    else:
                        cur_chromosome.slots[cur2 + k].append(id)

            if crossover_point[i]:
                is_first = not is_first

            j = j + 1

        cur_chromosome.CalculateFitness()

        return cur_chromosome
    

    def Mutation(self):
        if randint(0, 200) > self.mutationProbability:
            return None

        num_classes = len(self.classes)

        # Number of classes to move
        for _ in range(self.mutationSize, 0, -1):
            move_pos = randint(0, 40000) % num_classes
            cur = list(self.classes.keys())[move_pos]
            pos1 = self.classes[cur]
            cur_class_1 = cur

            num_room = instance.GetNumberOfRooms()
            dur = cur_class_1.GetDuration()
            day = randint(0, DAYS_NUM - 1)
            room = randint(0, num_room - 1)
            time = randint(0, DAY_HOURS - dur)
            pos2 = day * num_room * DAY_HOURS + room * DAY_HOURS + time

            # Move timeslots
            for j in range(dur):
                class_1 = self.slots[pos1 + j]
                for k in range(0, len(class_1)):
                    if class_1[k] == cur_class_1:
                        del class_1[k]
                        break

                if self.slots[pos2 + j] is None:
                    self.slots[pos2 + j] = [cur_class_1]
                else:
                    self.slots[pos2 + j].append(cur_class_1)

            self.classes[cur_class_1] = pos2
        
        self.CalculateFitness()


    def CalculateFitness(self):
        score = 0
        numberOfRooms = instance.GetNumberOfRooms()
        day_size = DAY_HOURS * numberOfRooms

        id = 0

        for i in self.classes.keys():
            p = self.classes[i]
            day = p // day_size
            time = p % day_size
            room = time // DAY_HOURS
            time = time % DAY_HOURS
            dur = i.GetDuration()

            # Check for room overlapping of classes
            is_room_overlap = False
            for j in range(dur):
                if len(self.slots[p + j]) > 1:
                    is_room_overlap = True
                    break
            if not is_room_overlap:
                score = score + 1
            self.criteria[id] = not is_room_overlap
            id += 1

            # Check for room capacity
            cur_class = i
            cur_room = instance.GetRoomById(room)
            self.criteria[id] = cur_room.GetNumberOfSeats() >= cur_class.GetNumberOfSeats()
            if self.criteria[id]:
                score = score + 1
            id += 1


            # Check for lab requirement
            self.criteria[id] = (not cur_class.IsLabRequired()) or (cur_class.IsLabRequired() and cur_room.IsLab())
            if self.criteria[id]:
                score = score + 1
            id += 1

            # Check for overlapping classes of professors and student groups
            is_prof_overlap = False
            is_group_overlap = False

            t = day * day_size + time
            ok = False
            
            for _ in range(numberOfRooms):
                if ok == True: break
                
                for k in range(dur):
                    if ok == True: break

                    cl = self.slots[t + k]
                    if cl is None: continue

                    for cur in cl:
                        if ok == True: break
                        if cur_class != cur:
                            if not is_prof_overlap and cur_class.ProfessorOverlaps(cur):
                                is_prof_overlap = True
                                
                            if not is_group_overlap and cur_class.GroupsOverlap(cur):
                                is_group_overlap = True
                                
                            if is_prof_overlap and is_group_overlap:
                                ok = True
                                break
                                                    
                t = t + DAY_HOURS

            # Professors has no overlapping classes?
            if not is_prof_overlap:
                score = score + 1
            self.criteria[id] = not is_prof_overlap
            id += 1

            # Groups has no overlapping classes?
            if not is_group_overlap:
                score = score + 1
            self.criteria[id] = not is_group_overlap
            id += 1

        self.fitness = score / (instance.GetNumberOfCourseClasses() * DAYS_NUM)
        self.score = score


    def GetFitness(self):
        return self.fitness
    
    
    # Soft constraints optimization
    def OptimizeFitness(self):
        score = 0
        for i in range(len(self.criteria)):
            if self.criteria[i]:
                score = score + 1
        
        for cur in self.classes.keys():
            if cur.course.GetNumberOfSeats() > instance.GetRoomById(self.classes[cur].room).GetNumberOfSeats():
                score = score - 1
            if cur.course.credit >= 3:
                score += 2

        self.fitness = self.fitness * (instance.GetNumberOfCourseClasses() * DAYS_NUM) / score