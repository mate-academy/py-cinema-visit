from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    list_customers = [Customer(customer["name"], customer["food"])
                      for customer in customers]
    for customer in list_customers:
        CinemaBar.sell_product(customer, customer.food)
    cinema_hall = CinemaHall(hall_number)
    cleaner_hall = Cleaner(cleaner)
    cinema_hall.movie_session(cleaning_staff=cleaner_hall,
                              costumers=list_customers, movie_name=movie)
