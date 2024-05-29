import codecs
#import mysql.connector
import csv

from Professor import Professor
from Course import Course
from StudentsGroup import StudentsGroup
from Room import Room
from CourseClass import CourseClass
 
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

        Room.restartIDs()

    def readcsv(self):
        # Clear previously used data
        self._professors = {}
        self._studentGroups = {}
        self._courses = {}
        self._rooms = {}
        self._courseClasses = []

        # Read professors
        count = 0
        with open("database/professors.csv", "r") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if count == 0:
                    count += 1
                    continue
                id = int(row[0])
                name = row[1]
                prof = Professor(id, name)
                self._professors[prof.GetId()] = prof

        # Read courses
        count = 0
        with open("database/courses.csv", "r") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if count == 0:
                    count += 1
                    continue
                id = int(row[0])
                code = row[1]
                name = row[2]
                credits = int(row[3])
                course = Course(id, code, name, credits)
                self._courses[course.GetId()] = course

        # Read rooms
        count = 0
        with open("database/rooms.csv", "r") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if count == 0:
                    count += 1
                    continue
                name = row[0]
                lab = row[1]
                number_of_seats = int(row[2])
                room = Room(name, lab, number_of_seats)
                self._rooms[room.GetId()] = room

        #Read groups
        count = 0
        with open("database/groups.csv", "r") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if count == 0:
                    count += 1
                    continue
                id = int(row[0])
                name = row[1]
                number_of_students = int(row[2])
                group = StudentsGroup(id, name, number_of_students)
                self._studentGroups[group.GetId()] = group
                
        #Read classes
        count = 0
        with open("database/classes.csv", "r") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if count == 0:
                    count += 1
                    continue
                print(row)
                professor = self._professors[int(row[0])]
                course = self._courses[int(row[1])]
                duration = int(row[2])
                group = [self._studentGroups[int(row[3])]]
                lab = row[4]
                cclass = CourseClass(professor, course, lab, duration, group)
                self._courseClasses.append(cclass)

        self.isEmpty = False
                
    
    def GetProfessorById(self, id):
        if id in self._professors.keys():
            return self._professors[id]
        return None

    def GetStudentsGroupById(self, id):
        if id in self._studentGroups.keys():
            return self._studentGroups[id]
        return None

    def GetCourseById(self, id):
        if id in self._courses.keys():
            return self._courses[id]
        return None
    
    def GetRoomById(self, id):
        if id in self._rooms.keys():
            return self._rooms[id]
        return None
    
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