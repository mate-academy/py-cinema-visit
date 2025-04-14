from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        visitors: list,
        auditorium_number: int,
        cleaner_name: str,
        movie_title: str
) -> None:
    customers_list = [Customer(customer.get("name"), customer.get("food"))
                      for customer in visitors]

    cleaning_staff = Cleaner(cleaner_name)
    hall = CinemaHall(auditorium_number)

    for customer in customers_list:
        CinemaBar.sell_product(customer, customer.food)

    hall.movie_session(movie_title, customers_list, cleaning_staff)
