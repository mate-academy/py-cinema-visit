from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    cinema_bar = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaner_person = Cleaner(cleaner)

    customers_list = []
    for customer in customers:
        new_custom = Customer(customer["name"], customer["food"])
        customers_list.append(new_custom)
        cinema_bar.sell_product(product=new_custom.food, customer=new_custom)

    hall.movie_session(movie_name=movie,
                       customers=customers_list,
                       cleaning_staff=cleaner_person)
