from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    # Sell products to each customer
    for cust in customers:
        customer = Customer(name=cust["name"],
                            food=cust["food"])
        cinema_bar.sell_product(customer=customer,
                                product=customer.food)

    # Start the movie session
    cinema_hall.movie_session(movie_name=movie,
                              customers=[Customer(**cust)
                                         for cust in customers],
                              cleaning_staff=cleaning_staff)
