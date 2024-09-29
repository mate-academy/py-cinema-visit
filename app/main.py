from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[dict], hall_number: int,
                 cleaner: str, movie: str) -> None:
    visitors = []
    for customer_and_food in customers:
        new_customer = Customer(
            customer_and_food["name"],
            customer_and_food["food"]
        )

        visitors.append(new_customer)
        CinemaBar.sell_product(new_customer.food, new_customer)

    current_session = CinemaHall(hall_number)
    cleaner_master = Cleaner(cleaner)
    current_session.movie_session(movie, visitors, cleaner_master)
