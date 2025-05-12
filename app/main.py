from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: dict, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customers_dict = []
    for customer in customers:
        customers_dict.append(Customer(name=customer["name"],
                                       food=customer["food"])
                              )

    for customers_bar in customers_dict:
        (CinemaBar.sell_product
         (product=customers_bar.food,
                               customer=customers_bar))

    hall = CinemaHall(number=hall_number)
    cleaner_instance = Cleaner(name=cleaner)
    hall.movie_session(
        movie_name=movie, customers=customers_dict,
        cleaning_staff=cleaner_instance
    )
