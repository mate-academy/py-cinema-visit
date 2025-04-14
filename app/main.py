from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> str:

    cleaner = Cleaner(name=cleaner)
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(number=hall_number)

    customers_list = [Customer(name=c["name"],
                      food=c["food"]) for c in customers]

    for person in customers_list:
        cinema_bar.sell_product(customer=person, product=person.food)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=cleaner
    )
