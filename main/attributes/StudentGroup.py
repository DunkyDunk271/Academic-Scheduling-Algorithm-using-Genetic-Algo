class StudentGroup:
    def __init__(self, stud_group_id, stud_group_size, course_ids):
        self.__stud_group_id = stud_group_id
        self.__stud_group_size = stud_group_size
        self.__course_ids = course_ids

    @property
    def stud_group_id(self):
        return self.__stud_group_id

    @property
    def stud_group_size(self):
        return self.__stud_group_size

    @property
    def course_ids(self):
        return self.__course_ids