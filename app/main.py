from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(*args, **kwargs) -> None:
    if kwargs:
        movie = kwargs.get("movie")
        customers = kwargs.get("customers")
        hall_number = kwargs.get("hall_number")
        cleaner = kwargs.get("cleaner")
    else:
        if len(args) >= 4:
            if isinstance(args[0], list):
                customers, hall_number, cleaner, movie = args[:4]
            else:
                movie, customers, hall_number, cleaner = args[:4]
        else:
            raise TypeError("Invalid arguments for cinema_visit")

    customers_objs = [
        Customer(name=c["name"], food=c["food"])
        for c in customers
    ]
    for cust in customers_objs:
        CinemaBar.sell_product(product=cust.food, customer=cust)
    cinema_hall = CinemaHall(hall_number=hall_number)
    cleaner_pers = Cleaner(name=cleaner)
    cinema_hall.movie_session(
        movie_name=movie,
        customers=customers_objs,
        cleaning_staff=cleaner_pers
    )
