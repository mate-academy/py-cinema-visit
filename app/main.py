# write your imports here
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
    hall_instance = CinemaHall(hall_number)
    bar_instance = CinemaBar()
    cleaner_inst = Cleaner(cleaner)
    customers_inst = []
    for customer in customers:
        person = Customer(name=customer["name"], food=customer["food"])
        customers_inst.append(person)
        bar_instance.sell_product(
            product=person.food,
            customer=person
        )

    hall_instance.movie_session(
        movie_name=movie,
        customers=customers_inst,
        cleaning_staff=cleaner_inst
    )
