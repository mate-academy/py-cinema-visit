from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_person_list = []
    for customer in customers:
        customer_person = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(
            customer=customer_person,
            product=customer["food"]
        )
        customer_person_list.append(customer_person)
    cleaner_person = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    CinemaHall.movie_session(
        self=hall,
        movie_name=movie,
        customers=customer_person_list,
        cleaning_staff=cleaner_person
    )
