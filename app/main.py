# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[dict], hall_number: int,
                 cleaner: str, movie: str) -> None:
    visitors_list = []
    for customer in customers:
        visitor = Customer(
            name=customer["name"],
            food=customer["food"]
        )
        visitors_list.append(visitor)
        CinemaBar.sell_product(product=visitor.food, customer=visitor)
    hall = CinemaHall(hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=visitors_list,
        cleaning_staff=Cleaner(cleaner)
    )
