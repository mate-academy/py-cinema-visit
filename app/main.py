from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    # write you code here
    pass
    cinema_customers = [
        Customer(name=item["name"], food=item["food"]) for item in customers
    ]

    for customer in cinema_customers:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    hall.movie_session(movie_name=movie, customers=cinema_customers,
                       cleaning_staff=cleaning_staff)