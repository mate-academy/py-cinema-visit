from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str, movie: str
) -> None:
    hall_num = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)
    customer_obj = []

    for person in customers:
        customer_obj.append(Customer(person["name"], person["food"]))

    for obj in customer_obj:
        CinemaBar.sell_product(product=obj.food, customer=obj)

    hall_num.movie_session(movie, customer_obj, cleaner_obj)
