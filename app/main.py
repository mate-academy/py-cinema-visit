from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None :
    new_customers = []
    cleaner_of_day = Cleaner(cleaner)
    for cus in customers:
        customer = Customer(cus["name"], cus["food"])
        CinemaBar.sell_product(customer.food, customer)
        new_customers.append(customer)
    hall_interaction = CinemaHall(hall_number)
    hall_interaction.movie_session(movie, new_customers, cleaner_of_day)
