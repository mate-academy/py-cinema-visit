from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_list = []
    cleaner_obj = Cleaner(cleaner)
    for customer in customers:
        customer_obj = Customer(name=customer["name"], food=customer["food"])
        customers_list.append(customer_obj)

    for customer in customers_list:
        CinemaBar.sell_product(customer, customer.food)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie, customers_list, cleaner_obj)
