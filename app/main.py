from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    customer_list = []

    for customer in customers:
        customer_instance = Customer(
            name=customer["name"],
            food=customer["food"]
        )
        customer_list.append(customer_instance)

    hall = CinemaHall(hall_number)

    cleaning_staff = Cleaner(name=cleaner)

    for customer in customer_list:
        CinemaBar.sell_product(
            product=customer.food,
            customer=customer
        )

    hall.movie_session(
        movie_name=movie,
        customers=customer_list,
        cleaning_staff=cleaning_staff
    )


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"},
    {"name": "Alice", "food": "Sprite"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"
cinema_visit(
    customers=customers,
    hall_number=hall_number,
    cleaner=cleaner_name,
    movie=movie
)
