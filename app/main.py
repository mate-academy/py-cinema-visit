# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: [dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    created_customers = [
        Customer(
            name=customer["name"],
            food=customer["food"]
        )
        for customer in customers
    ]

    created_cinema_hall = CinemaHall(hall_number)
    created_cleaner = Cleaner(cleaner)

    for customer in created_customers:
        CinemaBar.sell_product(customer, customer.food)

    created_cinema_hall.movie_session(
        movie,
        created_customers,
        created_cleaner
    )
