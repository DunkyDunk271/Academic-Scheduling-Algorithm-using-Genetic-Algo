class Professor:
    def __init__(self, prof_id, prof_name):
        self.__prof_id = prof_id
        self.__prof_name = prof_name

    @property
    def prof_id(self):
        return self.__prof_id

    @property
    def prof_name(self):
        return self.__prof_name