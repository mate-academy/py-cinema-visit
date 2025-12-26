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
    customer_list = []
    for customer_dict in customers:
        name = customer_dict["name"]
        food = customer_dict["food"]
        custom_obj = Customer(name, food)
        customer_list.append(custom_obj)

    cinema_hall_obj = CinemaHall(hall_number)
    cleaner_obj = Cleaner(name=cleaner)

    for custom_obj in customer_list:
        CinemaBar.sell_product(product=custom_obj.food, customer=custom_obj)

    cinema_hall_obj.movie_session(movie, customer_list, cleaner_obj)
