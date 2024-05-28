class Room:
    # Increment ID
    _nxt_id = 0

    # Restarts ID assigments
    @staticmethod
    def restartIDs() -> None:
        Room._nxt_id = 0

    def __init__(self, room_name, is_lab, number_of_seats):
        self.Id = Room._nxt_id
        Room._nxt_id += 1

        # Name like C310        
        self.Name = room_name
        
        # TRUE if room has computers
        self.Lab = is_lab
        
        # Returns number of seats in room
        self.NumberOfSeats = number_of_seats
    
    def __hash__(self):
        return hash(self.Id)
    
    # Compare ID
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return hash(self) == hash(other)

    def __ne__(self, other):
        return not (self == other)