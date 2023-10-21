from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner

def cinema_visit(customers: list, hall_number: int, cleaner_name: str, movie_name: str) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner_name)

    for customer_data in customers:
        customer = Customer(name=customer_data["name"], food=customer_data["food"])
        cinema_bar.sell_product(customer, customer.food)

    cinema_hall.movie_session(
        movie_name,
        [Customer(name=customer_data["name"], food=customer_data["food"]) for customer_data in customers],
        cleaner
    )

customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie_name = "Madagascar"
cinema_visit(customers, hall_number, cleaner_name, movie_name)
