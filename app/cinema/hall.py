class CinemaHall:
    
    def __init__(self, hall_number: int):
        self.hall_number = hall_number
 
 
    def movie_session(self, movie_name, customers: list, cleaning_staff):
        print(f"The movie '{movie_name}' is starting in hall {self.hall_number}.")
        
        for customer in customers:
            customer.watch_movie(movie_name)
        
        print(f"The movie '{movie_name}' has ended.")
        
        cleaning_staff.clean_hall(self.hall_number)
        
        