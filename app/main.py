from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers_orders = [Customer(name=customer.get("name"),
                                 food=customer.get("food"))
                        for customer in customers]
    cinema_hall = CinemaHall(number=hall_number)
    cinema_bar = CinemaBar()
    hall_cleaner = Cleaner(name=cleaner)
    for customer in customers_orders:
        cinema_bar.sell_product(customer=customer,
                                product=customer.food)
    cinema_hall.movie_session(movie_name=movie,
                              customers=customers_orders,
                              cleaning_staff=hall_cleaner)
