from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> str:
    customers_list = []
    staff = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    for customer in customers:
        customer = Customer(
            name=customer.get("name"),
            food=customer.get("food")
        )
        CinemaBar.sell_product(customer.food, customer)
        customers_list.append(customer)
    hall.movie_session(movie_name=movie,
                       customers=customers_list,
                       cleaning_staff=staff)
