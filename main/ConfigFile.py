import Schedule

class ConfigFile:
    @staticmethod
    def initialize_schedule():
        # Create timetable
        schedule = Schedule()

        # Set up rooms
        schedule.add_class_room(101, "Shillman", 35)
        schedule.add_class_room(201, "East Village", 50)
        schedule.add_class_room(401, "Ell Hall", 40)
        schedule.add_class_room(503, "Snell Engineering", 45)

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
        schedule.add_professor(1, "Dr N Sharma")
        schedule.add_professor(2, "Mrs G Kalra")
        schedule.add_professor(3, "Dr R Thomsan")
        schedule.add_professor(4, "Mr R Ponting")

        # Set up modules and define the professors that teach them
        schedule.add_course(1, "CSE05", "Computer Science", [1, 2])
        schedule.add_course(2, "ALG04", "Algorithms", [1, 3])
        schedule.add_course(3, "OS101", "Operating System", [1, 2])
        schedule.add_course(4, "EET08", "Engineering Ethics", [3, 4])
        schedule.add_course(5, "TED07", "Thermodynamics", [4])
        schedule.add_course(6, "BDA03", "Big Data", [1, 4])

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