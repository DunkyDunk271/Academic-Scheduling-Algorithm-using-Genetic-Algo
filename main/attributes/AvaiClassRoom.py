class ClassRoom:
    def __init__(self, class_room_id, class_room_name, class_room_capacity):
        self.__class_room_id = class_room_id
        self.__class_room_name = class_room_name
        self.__class_room_capacity = class_room_capacity

    @property
    def class_room_id(self):
        return self.__class_room_id

    @property
    def class_room_name(self):
        return self.__class_room_name

    @property
    def class_room_capacity(self):
        return self.__class_room_capacity