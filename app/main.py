from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customers_list = []
    cinema_hall = CinemaHall(hall_number)
    cleaner_staff = Cleaner(cleaner)

    for customer in customers:
        customers_list.append(Customer(customer["name"], customer["food"]))

    for customer in customers_list:
        CinemaBar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie_name=movie,
                              customers=customers_list,
                              cleaning_staff=cleaner_staff)
