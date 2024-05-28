class StudentGroup:
    def __init__(self, id, name, numberOfStudents):
        self.Id = id
        self.Name = name
        self.NumberOfStudents = numberOfStudents
        self.CourseClasses = []

    @property
    def stud_group_id(self):
        return self.__stud_group_id

    @property
    def stud_group_size(self):
        return self.__stud_group_size

    @property
    def course_ids(self):
        return self.__course_ids