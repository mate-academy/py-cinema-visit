from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_instances = []
    for customer_dict in customers:
        customer_instances.append(
            Customer(customer_dict["name"], customer_dict["food"])
        )

    [CinemaBar.sell_product(customer_instance.food, customer_instance)
     for customer_instance in customer_instances]

    cinema_hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)
    cinema_hall.movie_session(movie, customer_instances, cleaner_instance)
