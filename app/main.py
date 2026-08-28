from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> str:
    new_customers = [Customer(food=customer["food"],
                              name=customer["name"])
                     for customer in customers]
    num = CinemaHall(hall_number)
    cleaner_name = Cleaner(cleaner)
    for customer in new_customers:
        CinemaBar.sell_product(customer.food, customer)
    num.movie_session(movie, new_customers, cleaner_name)
