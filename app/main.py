from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str,
                 movie: str) -> None:
    customer_instances = [
        Customer(name=c["name"], food=c["food"]) for c in customers
    ]

    cb = CinemaBar()
    ch = CinemaHall(number=hall_number)
    cleaner_instance = Cleaner(name=cleaner)

    for customer in customer_instances:
        cb.sell_product(product=customer.food, customer=customer)

    ch.movie_session(movie_name=movie, customers=customer_instances,
                     cleaning_staff=cleaner_instance)


# Example usage
if __name__ == "__main__":
    customers = [
        {"name": "Bob", "food": "Coca-cola"},
        {"name": "Alex", "food": "popcorn"}
    ]
    hall_number = 5
    cleaner_name = "Anna"
    movie = "Madagascar"

    cinema_visit(customers=customers, hall_number=hall_number,
                 cleaner=cleaner_name, movie=movie)
