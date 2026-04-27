
    
from hotelmanager import HotelManager

hotel = HotelManager()

def addRoomMenu():
    number = int(input("Enter room number: "))
    room_type = input("Enter room type (Single/Double/Suite): ")
    hotel.add_room(number, room_type)
    print(f"Room {number} added successfully.")

def registerGuestMenu():
    name = input("Enter guest name: ")
    phone = input("Enter guest phone: ")
    guest_id = hotel.register_guest(name, phone)
    print(f"Guest {name} registered successfully with ID {guest_id}.")

def createReservationMenu():
    guest_id = int(input("Enter guest ID: "))
    room_number = int(input("Enter room number: "))
    check_in = input("Enter check-in date (YYYY-MM-DD): ")
    check_out = input("Enter check-out date (YYYY-MM-DD): ")
    nights = int(input("Enter number of nights: "))
    discount = float(input("Enter discount percentage (0 if none): "))
    
    reservation = hotel.create_reservation(guest_id, room_number, check_in, check_out, nights, discount)
    if reservation:
        print(f"Reservation created successfully for guest ID {guest_id} in room {room_number}.")
    else:
        print("Failed to create reservation. Please check guest ID and room availability.")

def checkInMenu():
    room_number = int(input("Enter room number for check-in: "))
    if hotel.check_in_guest(room_number):
        print(f"Guest checked in to room {room_number} successfully.")
    else:
        print("Failed to check in. Please check room number.")

def checkOutMenu():
    room_number = int(input("Enter room number for check-out: "))
    if hotel.check_out_guest(room_number):
        print(f"Guest checked out from room {room_number} successfully.")
    else:
        print("Failed to check out. Please check room number.")
def viewRoomsMenu():
    print("-------------------11------------------")
    hotel.view_rooms()

def viewGuestsMenu():
    hotel.view_guests() 
    print("-------------------22-----------------")
def mainMenu():
        print("\nHotel Management System")
        print("1. Add Room")
        print("2. Register Guest")
        print("3. Create Reservation")
        print("4. Check In Guest")
        print("5. Check Out Guest")
        print("6. View Rooms")
        print("7. View Guests")
        print("0. Exit")

def main():

    while True:
        mainMenu()
        choice = input("Enter your choice: ")
        if choice == '1':
            addRoomMenu()
        elif choice == '2':
            registerGuestMenu()
        elif choice == '3':
            createReservationMenu()
        elif choice == '4':
            checkInMenu()
        elif choice == '5':
            checkOutMenu()
        elif choice == '6':
            viewRoomsMenu()
        elif choice == '7':
            viewGuestsMenu()
        elif choice == '0':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()