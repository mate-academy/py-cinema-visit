from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_name = []
    for c_data in customers:
        customer = Customer(name=c_data["name"], food=c_data["food"])
        CinemaBar.sell_product(product=customer.food, customer=customer)
        customer_name.append(customer)
    hall = CinemaHall(hall_number)
    cleaner1 = Cleaner(cleaner)
    hall.movie_session(movie_name=movie, customers=customer_name,
                       cleaning_staff=cleaner1)
