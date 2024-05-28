import random

class Course:
    def __init__(self, course_id, course_code, course_name, prof_ids):
        self.__course_id = course_id
        self.__course_code = course_code
        self.__course_name = course_name
        self.__prof_ids = prof_ids

    @property
    def course_id(self):
        return self.__course_id

    @property
    def course_code(self):
        return self.__course_code

    @property
    def course_name(self):
        return self.__course_name

    def get_random_prof_id(self):
        return random.choice(self.__prof_ids)