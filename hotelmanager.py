
from model import Room, Guest, Reservation

class HotelManager:
    def __init__(self):
        self.rooms = []
        self.guests = []
        self.reservations = []

    def add_room(self, number, room_type):
        room = Room(number, room_type)
        self.rooms.append(room)

    def find_room(self, number):
        for room in self.rooms:
            if room.number == number:
                return room
        return None

    def find_guest(self, guest_id):
        if 0 <= guest_id < len(self.guests):
            return self.guests[guest_id]
        return None

    def register_guest(self, name, phone):
        guest = Guest(name, phone)
        self.guests.append(guest)
        return len(self.guests) - 1

    def create_reservation(self, guest_id, room_number, check_in, check_out, nights, discount=0):
        guest = self.find_guest(guest_id)
        room = self.find_room(room_number)
        
        if guest and room and room.available:
            reservation = Reservation(guest, room, check_in, check_out, nights, discount)
            self.reservations.append(reservation)
            room.available = False
            return reservation
        return None

    def check_in_guest(self, room_number):
        room = self.find_room(room_number)
        if room:
            room.available = False
            return True
        return False

    def check_out_guest(self, room_number):
        room = self.find_room(room_number)
        if room:
            room.available = True
            room.guest = None
            return True
        return False

    def view_rooms(self):
        # if rooms are empty 
        print ("-------------------1------------------")
        if not self.rooms:
            print(" -> No rooms have been added yet  ")
            print ("-------------------2------------------")
        # if rooms are not empty
        print ("-------------------3------------------")
        for room in self.rooms:
            status = "Available" if room.available else "Occupied"
            print ("-------------------4------------------")
            print(f"Room {room.number}: {room.room_type} - ${room.get_price()} - {status}")
            print ("-------------------5------------------")
    def view_guests(self):
        print ("-------------------6------------------")
        if not self.guests:
            print("-------------------7------------------")
            print(" -> No guests have been registered yet  ")
        for idx, guest in enumerate(self.guests):
            print("-------------------8------------------")
            print(f"Guest {idx}: {guest.name} - {guest.phone}")
            print("-------------------9------------------")