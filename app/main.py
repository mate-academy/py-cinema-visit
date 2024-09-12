from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers_obj = []
    for customer in customers:
        customers_obj.append(Customer(name=customer["name"],
                                      food=customer["food"]))

    for customer in customers_obj:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    cleaner_ = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)

    cinema_hall.movie_session(movie, customers_obj, cleaner_)
