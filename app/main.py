from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_instance = []

    for customer_dict in customers:
        customer = Customer(name=customer_dict["name"],
                            food=customer_dict["food"])
        customer_instance.append(customer)

        CinemaBar.sell_product(product=customer.food,
                               customer=customer)

    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    cinema_hall.movie_session(movie_name=movie,
                              customers=customer_instance,
                              cleaning_staff=cleaning_staff)
