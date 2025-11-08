from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_obj = []
    for customer in customers:
        name = customer["name"]
        food = customer["food"]
        cust = Customer(name, food)
        CinemaBar.sell_product(product=food, customer=cust)
        customers_obj.append(cust)

    hall = CinemaHall(number=hall_number)
    cleaner_obj = Cleaner(name=cleaner)
    hall.movie_session(movie_name=movie,
                       customers=customers_obj,
                       cleaning_staff=cleaner_obj)
