from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_instances = []
    for customer in customers:
        name = customer["name"]
        food = customer["food"]
        customer_instances.append(Customer(name=name, food=food))

    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)
    hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(name=cleaner)
    hall.movie_session(movie_name=movie, customers=customer_instances,
                       cleaning_staff=cleaner_instance)
