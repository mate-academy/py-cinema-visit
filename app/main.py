from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    all_visitor = []
    cinema_go = CinemaHall(hall_number)
    clean_go = Cleaner(cleaner)
    for visitor in customers:
        visitor["name"] = Customer(visitor["name"], visitor["food"])
        CinemaBar.sell_product(
            customer=visitor["name"],
            product=visitor["name"].food
        )
        all_visitor.append(visitor["name"])

    cinema_go.movie_session(movie, all_visitor, clean_go)
