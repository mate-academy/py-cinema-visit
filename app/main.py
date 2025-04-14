from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_list = []
    cleaner1 = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)
    for customer_person in customers:
        customer = Customer(customer_person["name"], customer_person["food"])
        customer_list.append(customer)

    for person in customer_list:
        CinemaBar.sell_product(person.food, person)

    CinemaHall.movie_session(cinema_hall, movie, customer_list, cleaner1)
