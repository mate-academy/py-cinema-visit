from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    my_cinema_hall = CinemaHall(hall_number)
    my_cleaner = Cleaner(cleaner)

    # Create list of customer instances
    my_customers = [Customer(name=customer.get("name"),
                             food=customer.get("food"))
                    for customer in customers]

    # sell products
    for my_customer in my_customers:
        CinemaBar.sell_product(my_customer, my_customer.food)

    # start movie session
    my_cinema_hall.movie_session(movie, my_customers, my_cleaner)
