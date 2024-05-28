class UniversityClass:
    def __init__(self, class_id, stud_group_id, course_id):
        self.__class_id = class_id
        self.__stud_group_id = stud_group_id
        self.__course_id = course_id
        self.__prof_id = None
        self.__timeslot_id = None
        self.__class_room_id = None

    def add_professor(self, professor_id):
        self.__prof_id = professor_id

    def add_timeslot(self, timeslot_id):
        self.__timeslot_id = timeslot_id

    def set_class_room_id(self, class_room_id):
        self.__class_room_id = class_room_id

    @property
    def class_id(self):
        return self.__class_id

    @property
    def stud_group_id(self):
        return self.__stud_group_id

    @property
    def course_id(self):
        return self.__course_id

    @property
    def professor_id(self):
        return self.__prof_id

    @property
    def timeslot_id(self):
        return self.__timeslot_id

    @property
    def class_room_id(self):
        return self.__class_room_id