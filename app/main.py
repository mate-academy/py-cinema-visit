from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaning_staff: str,
        movie_name: str,
) -> None:
    # write you code here
    # for ccc in customers:
    #     customer = Customer(ccc["name"], ccc["food"])
    # customer = Customer(customers[0], customers[1])
    customer = [Customer(customer["name"], customer["food"]) for customer in customers]
    hull_numb = CinemaHall(hall_number)
    cleaner = Cleaner(cleaning_staff)
    cinema_bar = CinemaBar()

    for cus in customer:
        cinema_bar.sell_product(cus.food, cus)
        hull_numb.movie_session(movie_name, customer, cleaning_staff)
    cleaner.clean_hall(hall_number)
