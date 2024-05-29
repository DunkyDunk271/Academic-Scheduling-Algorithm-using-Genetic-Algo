class StudentsGroup:
    def __init__(self, id, name, numberOfStudents):
        self.Id = id
        self.Name = name
        self.NumberOfStudents = numberOfStudents
        self.CourseClasses = []

    # Bind group to class
    def addClass(self, course_class):
        self.CourseClasses.append(course_class)

    def GetId(self):
        return self.Id

    def __hash__(self):
        return hash(self.Id)

    # Compares ID
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return hash(self) == hash(other)

    def __ne__(self, other):
        return not (self == other)