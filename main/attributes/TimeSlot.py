class Timeslot:
    def __init__(self, timeslot_id, timeslot):
        self.__timeslot_id = timeslot_id
        self.__timeslot = timeslot

    @property
    def timeslot_id(self):
        return self.__timeslot_id

    @property
    def timeslot(self):
        return self.__timeslot