from collections import defaultdict
from attributes import ClassRoom, Professor, Course, StudentGroup, TimeSlot

class Schedule:
    def __init__(self, schedule=None):
        if schedule is None:
            self.class_rooms = defaultdict(ClassRoom)
            self.professors = defaultdict(Professor)
            self.courses = defaultdict(Course)
            self.stud_groups = defaultdict(StudentGroup)
            self.timeslots = defaultdict(TimeSlot)
            self.classes = []
            self.num_of_classes = 0
        else:
            self.class_rooms = schedule.get_class_rooms()
            self.professors = schedule.get_professors()
            self.courses = schedule.get_courses()
            self.stud_groups = schedule.get_stud_groups()
            self.timeslots = schedule.get_timeslots()
            self.classes = schedule.get_classes()
            self.num_of_classes = schedule.get_num_of_classes()

    def get_class_rooms(self):
        return self.class_rooms

    def get_professors(self):
        return self.professors

    def get_courses(self):
        return self.courses

    def get_stud_groups(self):
        return self.stud_groups

    def get_timeslots(self):
        return self.timeslots

    def get_classes(self):
        return self.classes

    def add_class_room(self, class_room_id, class_room_name, class_room_capacity):
        self.class_rooms[class_room_id] = ClassRoom(class_room_id, class_room_name, class_room_capacity)

    def add_professor(self, professor_id, professor_name):
        self.professors[professor_id] = Professor(professor_id, professor_name)

    def add_course(self, course_id, course_code, course, professor_ids):
        self.courses[course_id] = Course(course_id, course_code, course, professor_ids)

    def add_student_group(self, stud_group_id, stud_group_size, course_ids):
        self.stud_groups[stud_group_id] = StudentGroup(stud_group_id, stud_group_size, course_ids)
        self.num_of_classes = 0

    def add_timeslot(self, timeslot_id, timeslot):
        self.timeslots[timeslot_id] = TimeSlot(timeslot_id, timeslot)

    def get_student_groups_as_array(self):
        return list(self.stud_groups.values())

    # ... rest of the methods ...