from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:
    customers_came_to_cinema = list()
    for person in customers:
        customers_came_to_cinema.append(
            Customer(person["name"],
                     person["food"]
                     )
        )

    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar
    cleaner_person = Cleaner(cleaner)

    for person in customers_came_to_cinema:
        cinema_bar.sell_product(
            person.food,
            person
        )

    cinema_hall.movie_session(
        movie,
        customers_came_to_cinema,
        cleaner_person
    )
