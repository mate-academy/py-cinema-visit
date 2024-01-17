from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    list_of_inst_customers = [
        Customer(
            name=dict_cust.get("name"),
            food=dict_cust.get("food")
        )
        for dict_cust in customers
    ]

    inst_hall = CinemaHall(hall_number)

    inst_cleaner = Cleaner(cleaner)

    for inst_cust in list_of_inst_customers:
        CinemaBar.sell_product(inst_cust, inst_cust.food)

    inst_hall.movie_session(
        movie_name=movie,
        customers=list_of_inst_customers,
        cleaning_staff=inst_cleaner
    )
