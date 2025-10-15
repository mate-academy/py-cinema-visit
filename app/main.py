# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    # write you code here
    customs = [Customer(
        name=customer["name"],
        food=customer["food"]
    )
        for customer in customers
    ]
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    for cust in customs:
        CinemaBar.sell_product(product=cust.food, customer=cust)
    hall.movie_session(
        movie_name=movie,
        customers=customs,
        cleaning_staff=cleaner
    )
