class ConfigFile:

    @staticmethod
    def initialize_schedule():
        # Create timetable
        schedule = Schedule()

        # Set up rooms
        schedule.add_classroom(101, "Large Lecture Hall", 35)
        schedule.add_classroom(201, "Small Lecture Hall", 50)
        schedule.add_classroom(401, "Computer Lab", 40)
        schedule.add_classroom(503, "Team Based Leaning", 45)

        # Set up timeslots
        schedule.add_timeslot(1, "Monday 9:00 - 11:00")
        schedule.add_timeslot(2, "Monday 11:00 - 13:00")
        schedule.add_timeslot(3, "Monday 13:00 - 15:00")
        schedule.add_timeslot(4, "Tuesday 9:00 - 11:00")
        schedule.add_timeslot(5, "Tuesday 11:00 - 13:00")
        schedule.add_timeslot(6, "Tuesday 13:00 - 15:00")
        schedule.add_timeslot(7, "Wednesday 9:00 - 11:00")
        schedule.add_timeslot(8, "Wednesday 11:00 - 13:00")
        schedule.add_timeslot(9, "Wednesday 13:00 - 15:00")
        schedule.add_timeslot(10, "Thursday 9:00 - 11:00")
        schedule.add_timeslot(11, "Thursday 11:00 - 13:00")
        schedule.add_timeslot(12, "Thursday 13:00 - 15:00")
        schedule.add_timeslot(13, "Friday 9:00 - 11:00")
        schedule.add_timeslot(14, "Friday 11:00 - 13:00")
        schedule.add_timeslot(15, "Friday 13:00 - 15:00")

        # Set up professors
        schedule.add_professor(1, "Prof. Nam")
        schedule.add_professor(2, "Prof. Khoa")
        schedule.add_professor(3, "Prof. Hieu")
        schedule.add_professor(4, "Prof. Dinh")

        # Set up modules and define the professors that teach them
        schedule.add_course(1, "MATH1010", "Calculus", [1, 2])
        schedule.add_course(2, "COMP2010", "Algorithm Design", [1, 3])
        schedule.add_course(3, "COMP1010", "Introduction to Programming", [1, 2])
        schedule.add_course(4, "MATH2010", "Advanced Probability and Statistics", [3, 4])
        schedule.add_course(5, "COMP3010", "Computer Organization", [4])
        schedule.add_course(6, "HASS100", "Ho Chi Minh Ideology", [1, 4])

        # Set up student groups and the modules they take.
        schedule.add_student_group(1, 30, [1, 3, 4])
        schedule.add_student_group(2, 50, [2, 3, 5, 6])
        schedule.add_student_group(3, 38, [3, 4, 5])
        schedule.add_student_group(4, 45, [1, 4])
        schedule.add_student_group(5, 40, [2, 3, 5])
        schedule.add_student_group(6, 42, [1, 4, 5])
        schedule.add_student_group(7, 36, [1, 3])
        schedule.add_student_group(8, 38, [2, 6])
        schedule.add_student_group(9, 44, [1, 6])
        schedule.add_student_group(10, 45, [3, 4])
        
        return schedule


# Placeholder classes for Schedule, Classroom, Timeslot, Professor, Course, and StudentGroup
class Schedule:
    def __init__(self):
        self.classrooms = []
        self.timeslots = []
        self.professors = []
        self.courses = []
        self.student_groups = []

    def add_classroom(self, room_number, building, capacity):
        self.classrooms.append(Classroom(room_number, building, capacity))

    def add_timeslot(self, id, timeslot):
        self.timeslots.append(Timeslot(id, timeslot))

    def add_professor(self, id, name):
        self.professors.append(Professor(id, name))

    def add_course(self, id, code, name, professor_ids):
        self.courses.append(Course(id, code, name, professor_ids))

    def add_student_group(self, id, size, course_ids):
        self.student_groups.append(StudentGroup(id, size, course_ids))

class Classroom:
    def __init__(self, room_number, building, capacity):
        self.room_number = room_number
        self.building = building
        self.capacity = capacity

class Timeslot:
    def __init__(self, id, timeslot):
        self.id = id
        self.timeslot = timeslot

class Professor:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Course:
    def __init__(self, id, code, name, professor_ids):
        self.id = id
        self.code = code
        self.name = name
        self.professor_ids = professor_ids

class StudentGroup:
    def __init__(self, id, size, course_ids):
        self.id = id
        self.size = size
        self.course_ids = course_ids
