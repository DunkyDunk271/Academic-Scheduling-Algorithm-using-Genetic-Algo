# Connect Course and Class

class CourseClass:
    # Increment ID counter
    _next_id = 0

    def __init__(self, professor, course, computer_required, duration, group_of_students):
        self.Id = CourseClass._next_id
        CourseClass._next_id += 1
        
        # Professor teaches the course
        self.Professor = professor
        
        # Course belongs to the class
        self.Course = course

        # Number of seats required
        self.NumberOfSeats = 0

        # If course needs computer return True
        self.LabRequired = computer_required

        # Duration in hours
        self.Duration = duration

        # List of students register for the course
        self.Groups = set(group_of_students)

        # Bind prof to class
        self.Professor.addCourseClass(self)

        # Bind group of student to the class
        for studs in self.Groups:
            studs.addClass(self)
            self.NumberOfSeats += studs.NumberOfStudents
    
    def GetDuration(self):
        return self.Duration
    
    def GetNumberOfSeats(self):
        return self.NumberOfSeats
    
    def GetGroups(self):
        return self.Groups
    
    def GetCourse(self):
        return self.Course
    
    def GetProfessor(self):
        return self.Professor
    
    def IsLabRequired(self):
        return self.LabRequired

    def __hash__(self):
        return hash(self.Id)

    # TRUE if another class with overlapping student groups.
    def GroupsOverlap(self, o):
        return len(self.Groups & o.Groups) > 0

    # TRUE if another class with the same professor.
    def ProfessorOverlaps(self, o):
        return self.Professor == o.Professor

    # True if the number of students less than 90
    def exceedNumOfStudents(self):
        return self.NumberOfSeats < 90

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return hash(self) == hash(other)

    def __ne__(self, other):
        return not (self == other)

    # Restarts ID
    @staticmethod
    def restartIDs() -> None:
        CourseClass._next_class_id = 0