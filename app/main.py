from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    cinema_hall = CinemaHall(hall_number)
    cinema_cleaner = Cleaner(cleaner)
    cinema_customers = []

    for cust_dict in customers:
        cinema_cust = Customer(cust_dict.get("name"), cust_dict.get("food"))
        CinemaBar.sell_product(product=cinema_cust.food, customer=cinema_cust)
        cinema_customers.append(cinema_cust)

    cinema_hall.movie_session(movie_name=movie,
                              customers=cinema_customers,
                              cleaning_staff=cinema_cleaner)
