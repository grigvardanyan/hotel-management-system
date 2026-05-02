
from hotelmanager import HotelManager
from models.room import Standard, Deluxe, Suite

def main():
    hotel = HotelManager()
    
    while True:
        print("\n=== HOTEL MANAGEMENT ===")
        print("[1] Add Room")
        print("[2] Register Guest")
        print("[3] Create Reservation")
        print("[4] Check-in Guest")
        print("[5] Check-out Guest")
        print("[6] View Rooms")
        print("[7] View Guests")
        print("[8] Exit")
        
        choice = input("Enter choice: ").strip()
        
        if choice == "1":
            try:
                number = int(input("Enter room number: "))
                print("1. Standard ($100/night)")
                print("2. Deluxe ($150/night)")
                print("3. Suite ($250/night)")
                room_choice = input("Select room type: ")
                
                if room_choice == "1":
                    hotel.add_room(Standard(number))
                elif room_choice == "2":
                    hotel.add_room(Deluxe(number))
                elif room_choice == "3":
                    hotel.add_room(Suite(number))
                else:
                    print("Invalid choice!")
                    continue
                print(f"Room {number} added!")
            except ValueError:
                print("Invalid input!")
        
        elif choice == "2":
            name = input("Enter guest name: ")
            phone = input("Enter phone: ")
            hotel.register_guest(name, phone)
            print(f"Guest '{name}' registered!")
        
        elif choice == "3":
            guest_name = input("Enter guest name: ")
            guest = hotel.find_guest(guest_name)
            if not guest:
                print("Guest not found!")
                continue
            
            try:
                room_num = int(input("Enter room number: "))
                room = hotel.find_room(room_num)
                if not room:
                    print("Room not found!")
                    continue
                if not room.available:
                    print("Room not available!")
                    continue
                
                check_in = input("Check-in date (YYYY-MM-DD): ")
                check_out = input("Check-out date (YYYY-MM-DD): ")
                nights = int(input("Number of nights: "))
                discount = int(input("Discount %: "))
                
                reservation = hotel.create_reservation(guest, room, check_in, check_out, nights, discount)
                cost = reservation.get_cost()
                print(f"Reservation created! Cost: ${cost:.2f}")
            except ValueError:
                print("Invalid input!")
        
        elif choice == "4":
            try:
                room_num = int(input("Enter room number: "))
                hotel.check_in(room_num)
                print("Guest checked in!")
            except ValueError:
                print("Invalid input!")
        
        elif choice == "5":
            try:
                room_num = int(input("Enter room number: "))
                hotel.check_out(room_num)
                print("Guest checked out!")
            except ValueError:
                print("Invalid input!")
        
        elif choice == "6":
            print("\n--- ROOMS ---")
            for room in hotel.rooms:
                status = "Available" if room.available else f"Occupied ({room.guest.name})"
                print(f"Room {room.number} ({room.__class__.__name__}): ${room.get_price()} - {status}")
        
        elif choice == "7":
            print("\n--- GUESTS ---")
            for guest in hotel.guests:
                print(f"{guest.name} - {guest.phone}")
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()