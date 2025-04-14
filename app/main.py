from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaning_staff: str,
        movie_name: str
) -> None:

    # Creating instances
    customer_instances_list = [
        Customer(instance["name"], instance["food"]) for instance in customers
    ]
    cinema_hall_instance = CinemaHall(hall_number)
    cinema_bar_inst = CinemaBar()
    cleaner_instance = Cleaner(cleaning_staff)

    # Making calls
    for customer_instance in customer_instances_list:
        cinema_bar_inst.sell_product(
            customer_instance.food,
            customer_instance
        )
    cinema_hall_instance.movie_session(
        movie_name,
        customer_instances_list,
        cleaner_instance
    )
