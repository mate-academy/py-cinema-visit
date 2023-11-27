from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    customers_list = []
    for customer in customers:
        customers_list.append(Customer(customer["name"], customer["food"]))

    c_bar = CinemaBar()
    c_hall = CinemaHall(number=hall_number)
    c_staff = Cleaner(name=cleaner)

    for person in customers_list:
        c_bar.sell_product(product=person.food, customer=person)

    c_hall.movie_session(movie_name=movie,
                         customers=customers_list,
                         cleaning_staff=c_staff)
