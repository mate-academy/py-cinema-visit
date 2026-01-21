from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list[dict], hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_list = [Customer(customer["name"], customer["food"])
                     for customer in customers]
    for customer in customer_list:
        CinemaBar.sell_product(customer=customer, product=customer.food)
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    hall.movie_session(movie_name=movie, customers=customer_list,
                       cleaning_staff=cleaner)
