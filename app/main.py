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
    list_of_customers = []
    for customer in customers:
        list_of_customers.append(
            Customer(
                name=customer["name"],
                food=customer["food"]
            )
        )
    for member in list_of_customers:
        CinemaBar.sell_product(
            product=member.food,
            customer=member
        )
    CinemaHall(number=hall_number).movie_session(
        movie_name=movie,
        customers=list_of_customers,
        cleaning_staff=Cleaner(name=cleaner)
    )
