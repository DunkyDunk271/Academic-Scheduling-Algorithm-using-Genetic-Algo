# Number of Days in Uni available
Day = 5

# Number of Hour per Day available
Hour = 12

class Reservation:
    _cur_reservation = {}
    Not_Res = -1

    def __init__(self, day, time, room):
        self.Day = day
        self.Time = time
        self.Room = room

    @staticmethod
    def getHashCode(day, time, room) -> int:
            return day * Reservation.Not_Res * Hour + room * Hour + time

    def __hash__(self) -> int:
        return Reservation.getHashCode(self.Day, self.Time, self.Room)
    
    @staticmethod
    def parse(hashCode):
        reservation = Reservation._cur_reservation.get(hashCode)
        if reservation is None:
            cur_day = hashCode // (Hour * Reservation.Not_Res)
            hashCode2 = hashCode - (cur_day * Hour * Reservation.Not_Res)
            cur_room = hashCode2 // Hour
            cur_time = hashCode2 % Hour
            reservation = Reservation(cur_day, cur_time, cur_room)
            Reservation._cur_reservation[hashCode] = reservation
        return reservation
    
    
    @staticmethod
    def getReservation(nr, day, time, room):
        if nr != Reservation.Not_Res and nr > 0:
            Reservation.Not_Res = nr
            Reservation._cur_reservation.clear()

        hashCode = Reservation.getHashCode(day, time, room)
        reservation = Reservation.parse(hashCode)

        if reservation is None:
            reservation = Reservation(day, time, room)
            Reservation._cur_reservation[hashCode] = reservation
        return reservation
    

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return hash(self) == hash(other)
            
    def __ne__(self, other):
        return not self.__eq__(other)
        
    def __str__(self):
        return "Day: " + str(self.Day) + ", " + "Room: " + str(self.Room) + ", Time: " + str(self.Time)