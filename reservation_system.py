class CinemaHall:
    
    def __init__(self, movie_title: str, total_seats: int, ticket_price: float) -> None:
        self.movie_title = movie_title
        self.total_seats = total_seats
        self.ticket_price = ticket_price
        self.__booked_seats = []
    
    def book_seat(self, seat_number):
        if seat_number >= 1 and seat_number <= self.total_seats and seat_number not in self.__booked_seats:
            self.__booked_seats.append(seat_number)
            print(f"Successfull reserved {seat_number} seat")
        else:
            print("Incorrect data entered or this seat already reserved")
            
    def cancel_booking(self, seat_number):
        if seat_number in self.__booked_seats:
            self.__booked_seats.remove(seat_number)
            print("Your reserved seat successfully canceled!")
        else:
            print("This seat is not reserved yet")
            
    def show_hall_info(self, movie_title, total_seats, booked_seats):
        print(f"Film: {self.movie_name}")
        print(f"Total seats: {self.total_seats}")
        print(f"Booked seats: {len(self._booked_seats)}")
        print(f"available seats: {self.available_seats}")
        print(f"Income: {self.income} грн\n")
            
    @property   
    def booked_seats(self):
        return self.__booked_seats.copy()
    @property
    def available_seats(self):
        return self.total_seats - len(self._booked_seats)
    
    @property
    def income(self, __booked_seats, ticket_price):
        return len(self._booked_seats) * self.ticket_price

class VIPCinemaHall(CinemaHall):
    
    def __init__(self, movie_title: str, total_seats: int, ticket_price: float, service_fee: float):
        super().__init__(movie_title, total_seats, ticket_price)
        self.service_fee = service_fee
        
    def get_income(self):
        #кількість заброньованих місць * (ціна квитка + service_fee)
        return len(self.booked_seats) * (self.ticket_price + self.service_fee)
        

hall = CinemaHall("LALALA", 50, 200)
hall.book_seat(10)    
hall.book_seat(55)   
hall.book_seat(-5)
        
hall.cancel_booking(15)
hall.cancel_booking(99)

hall.booked_seats.append(20)

hall.show_hall_info()