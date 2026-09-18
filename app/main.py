# from cinema import bar, hall
# from people import cinema_staff, customer
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    customers_list = []
    for item in customers:
        new_customer = Customer(item["name"], item["food"])
        customers_list.append(new_customer)

        CinemaBar.sell_product(new_customer.food, new_customer)

    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    cinema_hall.movie_session(movie, customers_list, cleaning_staff)
