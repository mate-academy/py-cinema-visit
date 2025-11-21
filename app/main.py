from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:
    customer_objects = []

    for data in customers:
        customer_objects.append(Customer(name=data["name"], food=data["food"]))

    for customer in customer_objects:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    cleaner_objects = Cleaner(name=cleaner)

    hall = CinemaHall(number=number)

    hall.movie_session(movie_name=movie,
                       customers=customer_objects,
                       cleaning_staff=cleaner_objects
                       )


if __name__ == "__main__":
    customers = [
        {"name": "Bob", "food": "Coca-cola"},
        {"name": "Alex", "food": "popcorn"}
    ]
    number = 5
    cleaner_name = "Anna"
    movie = "Madagascar"

    cinema_visit(
        customers=customers,
        number=number,
        cleaner=cleaner_name,
        movie=movie
    )
