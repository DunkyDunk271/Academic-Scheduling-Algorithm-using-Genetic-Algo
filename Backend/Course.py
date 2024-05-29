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
    
    def GetId(self):
        return self.Id
    
    def GetCredits(self):
        return self.Credit
    
    def GetName(self):
        return self.Name