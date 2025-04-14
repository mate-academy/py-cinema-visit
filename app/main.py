from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    new_customers = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    new_cinema_hall = CinemaHall(hall_number)
    new_cleaner = Cleaner(cleaner)

    for customer in new_customers:
        CinemaBar.sell_product(customer.food, customer)

    new_cinema_hall.movie_session(movie_name=movie,
                                  customers=new_customers,
                                  cleaning_staff=new_cleaner)
