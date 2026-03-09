from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall

customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_instances = [
        Customer(name=c["name"], food=c["food"])
        for c in customers
    ]

    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    for customer in customer_instances:
        CinemaBar.sell_product(
            product=customer.food,
            customer=customer
        )

    hall.movie_session(movie, customer_instances, cleaning_staff)


cinema_visit(
    customers=customers,
    hall_number=hall_number,
    cleaner=cleaner_name,
    movie=movie
)
