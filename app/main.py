from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)

    customer_instances = []

    for customer_info in customers:
        customer_name = customer_info["name"]
        food_choice = customer_info["food"]
        customer = Customer(customer_name, food_choice)
        cinema_bar.sell_product(customer, food_choice)
        customer_instances.append(customer)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance
    )
