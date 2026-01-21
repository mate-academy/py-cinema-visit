from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    clean_worker = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    customers_list = [
        Customer(name=customer.get("name"), food=customer.get("food"))
        for customer in customers
    ]
    [
        cinema_bar.sell_product(customer=customer, product=customer.food)
        for customer in customers_list
    ]
    cinema_hall.movie_session(movie, customers_list, clean_worker)
