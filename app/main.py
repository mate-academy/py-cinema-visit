from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer

customers_list = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]


def cinema_visit(customers: list, hall_number: int, cleaner: str,
                 movie_name: str) -> None:

    cinema_hall = CinemaHall(number=hall_number)
    cleaner = Cleaner(cleaner)

    guests = []

    for customer in customers:
        customer_inst = Customer(name=customer["name"], food=customer["food"])
        CinemaBar.sell_product(
            customer=customer_inst,
            product=customer["food"]
        )
        guests.append(customer_inst)

    cinema_hall.movie_session(movie_name=movie_name,
                              customers=guests,
                              cleaning_staff=cleaner)


cinema_visit(
    customers=customers_list,
    hall_number=5,
    cleaner="Anna",
    movie_name="The Martian"
)
