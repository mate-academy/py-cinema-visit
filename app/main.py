from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    list_of_customers = []
    for customer in customers:
        list_of_customers.append(Customer(name=customer["name"],
                                          food=customer["food"]))
    hall = CinemaHall(hall_number)
    cleaner_staff = Cleaner(cleaner)

    for sell in list_of_customers:
        CinemaBar.sell_product(product=sell.food, customer=sell)
    hall.movie_session(movie_name=movie,
                       customers=list_of_customers,
                       cleaner_staff=cleaner_staff)
