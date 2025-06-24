from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str | Cleaner,
                 movie: str
                 ) -> None:

    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    list_of_customers = []
    for customer in customers:
        customer = Customer(customer["name"], customer["food"])
        list_of_customers.append(customer)

    for customer in list_of_customers:
        CinemaBar.sell_product(customer.food, customer)

    hall.movie_session(movie_name=movie,
                       customers=list_of_customers,
                       cleaning_staff=cleaner)
