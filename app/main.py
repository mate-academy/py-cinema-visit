from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_objects = []
    for cll in customers:
        customer_objects.append(Customer(name=cll["name"], food=cll["food"]))
    hall = CinemaHall(number=hall_number)
    cleaner_obj = Cleaner(name=cleaner)
    for customer in customer_objects:
        CinemaBar.sell_product(
            product=customer.food,
            customer=customer
        )
    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaner_obj
    )


cinema_visit(
    customers=[
        {"name": "Bob", "food": "Coca-cola"},
        {"name": "Alex", "food": "popcorn"}
    ],
    hall_number=5,
    cleaner="Anna",
    movie="Madagascar"
)
