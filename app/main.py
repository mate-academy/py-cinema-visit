from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_list = [Customer(customer["name"], customer["food"])
                     for customer in customers]
    cinema_hall = CinemaHall(hall_number)
    cleaner_person = Cleaner(cleaner)

    for customer in customer_list:
        CinemaBar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie, customer_list, cleaner_person)
