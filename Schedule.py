

class Schedule:
    """
    Represents a university class schedule.
    """

    def __init__(self):
        """
        Initializes a new schedule object.
        """
        self.classrooms = {}
        self.professors = {}
        self.courses = {}
        self.student_groups = {}
        self.timeslots = {}

    def __init__(self, schedule):
        """
        Copy constructor to create a new schedule from another schedule.
        """
        self.classrooms = schedule.getClassrooms()
        self.professors = schedule.getProfessors()
        self.courses = schedule.getCourses()
        self.student_groups = schedule.getStudentGroups()
        self.timeslots = schedule.getTimeslots()

    def getClassrooms(self):
        return self.classrooms
    
    def getProfessors(self):
        return self.professors
    
    def getCourses(self):
        return self.courses
    
    def getStudentGroups(self):
        return self.student_groups
    
    def getTimeslots(self):
        return self.timeslots
    
    def getClasses(self):
        return self.classes
    