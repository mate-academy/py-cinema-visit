class CinemaHall:
    def __init__(self, hall_number: int) -> None:
        """
        Initializes the cinema hall with its number.
        """
        self.hall_number = hall_number

    def movie_session(self, movie_name: str, customers: list, cleaning_staff) -> None:
        """
        Simulates a movie session using the exact required parameter names.
        """
        print(f'"{movie_name}" started in hall number {self.hall_number}.')
        
        for customer in customers:
            customer.watch_movie(movie_name)
            
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(self.hall_number)
