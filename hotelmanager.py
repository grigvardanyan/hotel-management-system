
from models.guest import Guest
from models.reservation import Reservation


class HotelManager:
    def __init__(self):
        self.rooms = []
        self.guests = []
        self.reservations = []

    def add_room(self, room):
        """Add a room object (Standard, Deluxe, or Suite)"""
        self.rooms.append(room)

    def find_room(self, number):
        """Find room by number"""
        for room in self.rooms:
            if room.number == number:
                return room
        return None

    def find_guest(self, name):
        """Find guest by name"""
        for guest in self.guests:
            if guest.name.lower() == name.lower():
                return guest
        return None

    def register_guest(self, name, phone):
        """Register a new guest"""
        guest = Guest(name, phone)
        self.guests.append(guest)
        return guest

    def create_reservation(self, guest, room, check_in, check_out, nights, discount=0):
        """Create a new reservation"""
        reservation = Reservation(guest, room, check_in, check_out, nights, discount)
        self.reservations.append(reservation)
        room.available = False
        room.guest = guest
        return reservation

    def check_in(self, room_number):
        """Check in a guest"""
        room = self.find_room(room_number)
        if room and not room.available:
            return True
        return False

    def check_out(self, room_number):
        """Check out a guest"""
        room = self.find_room(room_number)
        if room:
            room.available = True
            room.guest = None
            return True
        return False