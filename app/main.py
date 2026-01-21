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

    cinema_bar = CinemaBar()
    customers_list = []
    cleaner_stuff = Cleaner(name=cleaner)

    for visitors in customers:
        customer = Customer(name=visitors["name"], food=visitors["food"])
        customers_list.append(customer)
        cinema_bar.sell_product(customer=customer, product=customer.food)

    cinema_hall = CinemaHall(number=hall_number)
    cinema_hall.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_stuff=cleaner_stuff
    )
