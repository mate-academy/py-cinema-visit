from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:

    cinema_hall = CinemaHall(number=hall_number)
    cinema_bar = CinemaBar()
    cinema_cleaner = Cleaner(name=cleaner)

    cinema_customers = []
    for customer in customers:
        cinema_customer = Customer(name=customer["name"],
                                   food=customer["food"])
        cinema_bar.sell_product(product=cinema_customer.food,
                                customer=cinema_customer)
        cinema_customers.append(cinema_customer)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=cinema_customers,
        cleaning_staff=cinema_cleaner
    )
