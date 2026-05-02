class Room:
    """Base room class"""
    def __init__(self, number):
        self.number = number
        self.available = True
        self.guest = None
    
    def get_price(self):
        raise NotImplementedError
    
    def __str__(self):
        return f"Room {self.number} ({self.__class__.__name__})"


class Standard(Room):
    """Standard room: $100/night"""
    def get_price(self):
        return 100


class Deluxe(Room):
    """Deluxe room: $150/night"""
    def get_price(self):
        return 150


class Suite(Room):
    """Suite room: $250/night"""
    def get_price(self):
        return 250
