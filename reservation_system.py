class CinemaHall:
    def __init__(self, movie_title: str, total_seats: int, ticket_price: float) -> None:
        self.movie_title = movie_title
        self.total_seats = total_seats
        self.ticket_price = ticket_price
        self.__booked_seats = []
    
    @property
    def booked_seats(self) -> list[int]:
        return self.__booked_seats.copy()
    
    @property
    def available_seats(self) -> int:
        return self.total_seats - len(self.__booked_seats)
    
    @property
    def income(self) -> float:
        return len(self.__booked_seats) * self.ticket_price

    def book_seat(self, seat_number: int) -> None:
        """Books a seat if it is valid and not already reserved"""
        
        if seat_number >= 1 and seat_number <= self.total_seats and seat_number not in self.__booked_seats:
            self.__booked_seats.append(seat_number)
            print(f"Successfull reserved {seat_number} seat")
        else:
            print("Incorrect data entered or this seat already reserved")
            
    def cancel_booking(self, seat_number: int) -> None:
        """Cancels the reservation for a specific seat"""
        
        if seat_number in self.__booked_seats:
            self.__booked_seats.remove(seat_number)
            print("Your reserved seat successfully canceled!")
        else:
            print("This seat is not reserved yet")
            
    def show_hall_info(self) -> None:
        """Displays general information about the cinema hall and seat statistics"""
        
        print(f"Film: {self.movie_title}")
        print(f"Total seats: {self.total_seats}")
        print(f"Booked seats: {len(self.__booked_seats)}")
        print(f"available seats: {self.available_seats}")
        print(f"Income: {self.income} грн\n")

class VIPCinemaHall(CinemaHall):
    def __init__(self, movie_title: str, total_seats: int, ticket_price: float, service_fee: float) -> None:
        super().__init__(movie_title, total_seats, ticket_price)
        self.service_fee = service_fee
        
    @property
    def income(self) -> float:
        return len(self.booked_seats) * (self.ticket_price + self.service_fee)
        
def main() -> None:
    my_hall = CinemaHall("booBoooooooo", 50, 200)
    # print(f"CinemaHall: LALALA\n")
    print(f"CinemaHall: {my_hall.movie_title}\n")
    print(f"Initial available seats: {my_hall.available_seats}")
    print(f"Initial income: ${my_hall.income}\n")
    print("Booking seats 10, 55, and -5")
    my_hall.book_seat(10)
    my_hall.book_seat(55)
    my_hall.book_seat(-5)
    print(f"Available seats after booking: {my_hall.available_seats}")
    print(f"Current income: ${my_hall.income}\n")
    print("Canceling seat 15")
    my_hall.cancel_booking(15)
    print(f"Final available seats: {my_hall.available_seats}")
    print(f"Final income: ${my_hall.income}")
    my_hall.cancel_booking(15)
    my_hall.show_hall_info()
    
main()
