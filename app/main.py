from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    customer_list = [
        Customer(person["name"], person["food"])
        for person in customers
    ]
    hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    staff = Cleaner(cleaner)

    for customer in customer_list:
        cinema_bar.sell_product(customer.food, customer)
    hall.movie_session(movie, customer_list, staff)
