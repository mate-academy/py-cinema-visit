from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int,
                 cleaner_name: str, movie: str) -> None:

    cleaner = Cleaner(name=cleaner_name)
    hall = CinemaHall(number=hall_number)

    customer_objects = [
        Customer(name=customer_info["name"], food=customer_info["food"])
        for customer_info in customers
    ]

    for customer in customer_objects:
        CinemaBar.sell_product(
            product=customer.food, customer=customer)

    hall.movie_session(movie_name=movie,
                       customers=customer_objects,
                       cleaning_staff=cleaner)


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]

cinema_visit(movie="Madagascar",
             customers=customers, hall_number=5,
             cleaner_name="Anna")
