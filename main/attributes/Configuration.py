import codecs
import mysql.connector

import Professor, Course, StudentsGroup, Room, CourseClass

class Configuration:
    def __init__(self):
        self.isEmpty = True
        # parsed professors
        self._professors = {}
        # parsed student groups
        self._studentGroups = {}
        # parsed courses
        self._courses = {}
        # parsed rooms
        self._rooms = {}
        # parsed classes
        self._courseClasses = []

        Room.Room.restartIDs()
    
    def get_professor(self, id):
        pass

    def get_students_group(self, id):
        pass

    def get_course(self, id):
        pass
    
    def get_room(self, id):
        pass
    
    def get_course_class(self):
        return self._courseClasses
    
    #################################################################

    def get_num_of_professors(self):
        return len(self._professors.keys())
    
    def get_num_of_groups(self):
        return len(self._studentGroups)

    def get_num_of_courses(self):
        return len(self._courses)
    
    def get_num_of_rooms(self):
        return len(self._rooms)
    
    def get_num_of_course_classes(self):
        return len(self._courseClasses)
    
    # Returns TRUE if configuration is not parsed yet
    def isEmpty(self):
        return self.isEmpty