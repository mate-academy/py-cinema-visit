from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
# write your imports here


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_list = [Customer(new_customer.get("name"),
                              new_customer.get("food"))
                     for new_customer in customers]

    for new_customer in customer_list:
        product = new_customer.food
        CinemaBar.sell_product(new_customer, product)

    cinema_hall = CinemaHall(hall_number)
    cleaner_work = Cleaner(cleaner)
    cinema_hall.movie_session(movie, customer_list, cleaner_work)
