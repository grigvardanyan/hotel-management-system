# Hotel Data Models

# Counters for IDs
room_id = 100
guest_id = 200
reservation_id = 300


class Room:
    def __init__(self, number, room_type):
        self.number = number
        self.room_type = room_type  # "standard", "deluxe", or "suite"
        self.available = True
        self.guest = None
    
    def get_price(self):
        if self.room_type == "standard":
            return 100
        elif self.room_type == "deluxe":
            return 150
        elif self.room_type == "suite":
            return 250
        return 100


class Guest:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class Reservation:
    def __init__(self, guest, room, check_in, check_out, nights, discount):
        self.guest = guest
        self.room = room
        self.check_in = check_in
        self.check_out = check_out
        self.nights = nights
        self.discount = discount
        self.status = "pending" 
    
    def get_cost(self):
        price = self.room.get_price()
        total = price * self.nights
        discount_amount = total * (self.discount / 100)
        return total - discount_amount
