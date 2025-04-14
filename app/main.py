from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner_name: str,
        movie: str
) -> None:

    inst_of_customers = []
    cleaner_instance = Cleaner(cleaner_name)

    for custom in customers:
        customers_inst = Customer(name=custom["name"], food=custom["food"])
        CinemaBar.sell_product(
            customer=customers_inst,
            product=customers_inst.food
        )
        inst_of_customers.append(customers_inst)

    cinema_hall_instance = CinemaHall(number=hall_number)
    cinema_hall_instance.movie_session(
        movie_name=movie,
        customers=inst_of_customers,
        cleaning_staff=cleaner_instance
    )
