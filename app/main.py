from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: "Cleaner",
        movie: str
) -> None:
    cleaner_obj = Cleaner(cleaner)
    customers_list = []
    for customer in customers:
        customer_obj = Customer(customer["name"], customer["food"])
        customers_list.append(customer_obj)
        CinemaBar.sell_product(customer_obj.food, customer_obj)

    hall = CinemaHall(hall_number)
    hall.movie_session(movie, customers_list, cleaner_obj)
