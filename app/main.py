from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cust_list = []
    for custom in customers:
        cust = Customer(name=custom["name"], food=custom["food"])
        cust_list.append(cust)
        CinemaBar.sell_product(product=cust.food, customer=cust)
    cinema_hall = CinemaHall(number=hall_number)
    cleaner_staff = Cleaner(name=cleaner)
    cinema_hall.movie_session(
        movie_name=movie,
        customers=cust_list,
        cleaning_staff=cleaner_staff
    )
