from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str):
    # create list with Customer instances
    list_of_customers = [
        Customer(
            name=customer["name"],
            food=customer["food"]
        )
        for customer in customers
    ]

    # sell the product to customers
    bar = CinemaBar()
    for customer in list_of_customers:
        bar.sell_product(customer.name, customer.food)

    # create CinemaHall instance and complete movie session acts
    film_session = CinemaHall(hall_number)
    film_session.movie_session(movie_name=movie,
                               customers=list_of_customers,
                               cleaning_staff=Cleaner(cleaner))
