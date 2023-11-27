from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    all_customers = []
    bar = CinemaBar()
    for customer in customers:
        new_customer = Customer(customer['name'], customer['food'])
        bar.sell_product(new_customer.food, new_customer)
        all_customers.append(new_customer)
    hall = CinemaHall(hall_number)
    cleaner_name = Cleaner(cleaner)
    hall.movie_session(movie, all_customers, cleaner_name)


"""If everything is ok please approve it again,
because on the platform this task appears like unsolved.
Thank you
"""
