from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[dict[str, str]], hall_number: int,
                 cleaner_name: str, movie: str) -> None:
    customer_objects = []

    for customer in customers:
        customer_obj = Customer(name=customer["name"], food=customer["food"])

        CinemaBar.sell_product(customer_obj, customer["food"])

        customer_objects.append(customer_obj)

    hall = CinemaHall(hall_number)

    hall.movie_session(movie_name=movie, customers=customer_objects,
                       cleaning_staff=Cleaner(cleaner_name))


if __name__ == "__main__":
    customers = [
        {"name": "Bob", "food": "Coca-cola"},
        {"name": "Alex", "food": "popcorn"}
    ]
    hall_number = 5
    cleaner_name = "Anna"
    movie = "Madagascar"
    cinema_visit(customers=customers, hall_number=hall_number,
                 cleaner_name=cleaner_name, movie=movie)
