class Reservation:
    def __init__(self, guest, room, check_in, check_out, nights, discount=0):
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
