from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customer_instances = []
    for c in customers:
        cust = Customer(name=c["name"], food=c["food"])
        CinemaBar.sell_product(product=cust.food, customer=cust)
        customer_instances.append(cust)

    cleaner_instance = Cleaner(name=cleaner)
    hall = CinemaHall(hall_number=hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance
    )


if __name__ == "__main__":
    customers = [
        {"name": "Bob", "food": "Coca-cola"},
        {"name": "Alex", "food": "popcorn"}
    ]
    hall_number = 5
    cleaner_name = "Anna"
    movie = "Madagascar"

    cinema_visit(
        movie=movie,
        customers=customers,
        hall_number=hall_number,
        cleaner=cleaner_name
    )
