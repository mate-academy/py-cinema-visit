from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customers_cinema = []
    for customer in customers:
        customer_obj = Customer(name=customer["name"],
                                food=customer["food"])
        customers_cinema.append(customer_obj)
    for customer in customers_cinema:
        CinemaBar.sell_product(product=customer.food,
                               customer=customer)

    cleaner_name = Cleaner(name=cleaner)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie_name=movie, customers=customers_cinema,
                       cleaning_staff=cleaner_name)
