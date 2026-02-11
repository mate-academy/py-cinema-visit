import app.people.customer
import app.people.cinema_staff

class CinemaHall:
    def __init__(self, hall_number):
        self.hall_number = hall_number

    def movie_sesion(self, movie_name: str, customers: list[customer.Customer], cleaning_staff: cinema_staff.Cleaner):
        print(f'"{movie_name}" started in hall number {self.hall_number}.')
        for cust in customers:
            cust.watch_movie(movie_name)
        print(f'"{movie}" ended.')
        cleaning_staff.clean_hall(self.hall_number)

        
        
        



    

    


