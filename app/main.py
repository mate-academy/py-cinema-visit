from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str) -> None:
    for customer in customers:
        customer_obj = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(customer_obj, customer_obj.food)

    hall = CinemaHall(hall_number)
    updated_cust = []
    cleaner = Cleaner(cleaner)
    for customer in customers:
        new_customer = Customer(customer["name"], customer["food"])
        updated_cust.append(new_customer)
    hall.movie_session(
        movie_name=movie,
        customers=updated_cust,
        cleaning_staff=cleaner
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
        customers=customers,
        hall_number=hall_number,
        cleaner=cleaner_name,
        movie=movie
    )
    # Cinema bar sold Coca-cola to Bob.
    # Cinema bar sold popcorn to Alex.
    # "Madagascar" started in hall number 5.
    # Bob is watching "Madagascar".
    # Alex is watching "Madagascar".
    # "Madagascar" ended.
    # Cleaner Anna is cleaning hall number 5.
