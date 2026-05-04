from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    cleaner_obj = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    customers_list = []
    for customer in customers:
        customer_obj = Customer(name=customer["name"], food=customer["food"])
        customers_list.append(customer_obj)
        CinemaBar.sell_product(customer=customer_obj,
                               product=customer_obj.food)
    hall.movie_session(movie_name=movie,
                       customers=customers_list, cleaning_staff=cleaner_obj)
