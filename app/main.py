from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customer_objects = []
    for customer in customers:
        cust = Customer(name=customer["name"], food=customer["food"])
        customer_objects.append(cust)
        CinemaBar.sell_product(product=cust.food, customer=cust)

    cleaning_staff = Cleaner(name=cleaner)
    hall = CinemaHall(number=hall_number)
    hall.movie_session(movie_name=movie, customers=customer_objects, cleaning_staff=cleaning_staff)

customers = [
    {"name": "Bob", "food": "popcorn"},
    {"name": "Alex", "food": "Coca-cola"}
]
cinema_visit(
    customers=customers,
    hall_number=5,
    cleaner="Anna",
    movie="Madagascar"
)