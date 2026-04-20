class HotelManager:
    def __init__(self):
        self.rooms = []
        self.guests = []
        self.reservations = []

    def add_room(self, number, room_type):
        room = room(number, room_type)
        self.rooms.append(room)

def find_room(self,number):
        for room in self.rooms:
            if room.number == number:
                return room
        return None 
