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
    
    def GetProfessorById(self, id):
        pass

    def GetStudentsGroupById(self, id):
        pass

    def GetCourseById(self, id):
        pass
    
    def GetRoomById(self, id):
        pass
    
    def GetCourseClasses(self):
        return self._courseClasses
    
    #################################################################

    def GetNumberOfProfessors(self):
        return len(self._professors.keys())
    
    def GetNumberOfStudentGroups(self):
        return len(self._studentGroups)

    def GetNumberOfCourses(self):
        return len(self._courses)
    
    def GetNumberOfRooms(self):
        return len(self._rooms)
    
    def GetNumberOfCourseClasses(self):
        return len(self._courseClasses)
    
    # Returns TRUE if configuration is not parsed yet
    def isEmpty(self):
        return self.isEmpty