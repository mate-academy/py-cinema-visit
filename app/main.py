from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    list_customers = []
    for customer in customers:
        name = customer["name"]
        food = customer["food"]
        list_customers.append(Customer(name, food))

    for customer in list_customers:
        CinemaBar.sell_product(customer.food, customer)

    staff = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie, list_customers, staff)
