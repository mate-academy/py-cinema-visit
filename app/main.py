from app.people import Customer, Cleaner
from app.cinema import CinemaBar, CinemaHall

def cinema_visit(movie: str, customers: list, hall_number: int, cleaner: str) -> None:
    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    customers = [Customer(name=c["name"], food=c["food"]) for c in customers]
    [CinemaBar.sell_product(c.food, c) for c in customers]
    cinema_hall.movie_session(movie, customers, cleaning_staff)
