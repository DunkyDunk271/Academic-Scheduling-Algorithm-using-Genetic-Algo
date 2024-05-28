# Number of Days in Uni available
Day = 5

# Number of Hour per Day available
Hour = 12

class Criteria:
    wei = [0, 0.5, 0.5, 0, 0]

    # True if room with overlapping classes
    @staticmethod
    def isRoomOverlapped(room_slots, booking, duration):
        booking_index = hash(booking)
        cur_slots = room_slots[booking_index: booking_index + duration]
        # if slot has more than 1 elements => Overlapping        
        for slot in cur_slots:
            if len(slot) > 1:
                return True
        return False
    
    # True if room has enough seats
    @staticmethod
    def isSeatEnough(room, cur_class):
        return room.NumberOfSeats >= cur_class.NumberOfSeats
    
    # True if room has computers if required
    @staticmethod
    def isComputerEnough(room, cur_class):
        return (not cur_class.LabRequired) or (cur_class.LabRequired and room.Lab)
    
    # True, True if professors, student groups with overlapping classes
    @staticmethod
    def isOverlappedProfStudentGrp(room_slots, cur_class, num_rooms, timeId):
        is_prof = is_studs = False

        dur = cur_class.Duration
        for i in range(num_rooms, 0, -1):
            # for each hour of class
            for j in range(timeId, timeId + dur):
                classes = room_slots[j]
                for cur_class1 in classes:
                    if cur_class != cur_class1:
                        # professor overlaps?
                        if not is_prof and cur_class.professorOverlaps(cur_class1):
                            is_prof = True
                        # student group overlaps?
                        if not is_studs and cur_class.groupsOverlap(cur_class1):
                            is_studs = True
                        # both type of overlapping? no need to check more
                        if is_prof and is_studs:
                            return is_prof, is_studs

            timeId += Hour
        return is_prof, is_studs
