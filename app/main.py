# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[Customer],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cinema_cleaner = Cleaner(cleaner)
    cinema_customers = [Customer(name=customer["name"], food=customer["food"])
                        for customer in customers]
    for customer in customers:
        customer_instance = Customer(customer["name"], customer["food"])
        cinema_bar.sell_product(customer=customer_instance,
                                product=customer_instance.food)
    cinema_hall.movie_session(movie=movie,
                              customers=cinema_customers,
                              cleaning_staff=cinema_cleaner)
