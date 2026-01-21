from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers_list: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_instance_list = [
        Customer(name=item["name"], food=item["food"])
        for item in customers_list
    ]
    hall = CinemaHall(number=hall_number)
    hall_cleaner = Cleaner(name=cleaner)
    cinema_bar = CinemaBar()
    for customer in customers_instance_list:
        cinema_bar.sell_product(product=customer.food, customer=customer)
    hall.movie_session(
        movie_name=movie,
        customers=customers_instance_list,
        cleaning_staff=hall_cleaner
    )
