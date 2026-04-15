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
    customer_instances = []
    for person in customers:
        customer = Customer(person["name"], person["food"])
        customer_instances.append(customer)
        CinemaBar.sell_product(customer.food, customer)

    hall = CinemaHall(hall_number)
    staff_member = Cleaner(cleaner)
    hall.movie_session(movie, customer_instances, staff_member)
