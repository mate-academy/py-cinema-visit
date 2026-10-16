# write your imports here
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list[dict], hall_number: int,
                 cleaner: str, movie: str) -> None:
    customers_instance = []
    for c_dict in customers:
        customer_obj = Customer(name=c_dict["name"], food=c_dict["food"])
        customers_instance.append(customer_obj)
        CinemaBar.sell_product(customer=customer_obj,
                               product=customer_obj.food)

    hall = CinemaHall(hall_number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=customers_instance,
        cleaning_staff=cleaning_staff
    )
