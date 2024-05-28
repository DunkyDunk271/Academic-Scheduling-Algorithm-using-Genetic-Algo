import random

class Course:
    def __init__(self, id, code, name, credit):
        self.Id = id
        
        # Code like COMP2020
        self.Code = code

        # Name of the course
        self.Name = name

        # Credit of the course (max 4)
        self.Credit = credit