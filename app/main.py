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
    created_customers = []
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    for customer in customers:
        customer_obj = Customer(name=customer["name"], food=customer["food"])
        created_customers.append(customer_obj)
        CinemaBar.sell_product(customer_obj.food, customer_obj)

    cinema_hall.movie_session(movie, created_customers, cleaner)
