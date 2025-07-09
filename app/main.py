from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> str:
    customer_objects = []
    for cust in customers:
        customer = Customer(cust["name"], cust["food"])
        CinemaBar.sell_product(customer, customer.food)
        customer_objects.append(customer)

    cleaning_staff = Cleaner(cleaner)
    hall = CinemaHall(hall_number)

    hall.movie_session(movie, customer_objects, cleaning_staff)
    return ""
