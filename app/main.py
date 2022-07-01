from app.cinema.bar import CinemaBar as Cb
from app.cinema.hall import CinemaHall as Ch
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    ls_with_customers = [Customer(name=customers[i]["name"],
                                  food=customers[i]["food"])
                         for i in range(len(customers))]
    for guys in ls_with_customers:
        Cb.sell_product(guys.food, guys)
    clean = Cleaner(cleaner)
    main_hall = Ch(hall_number)
    main_hall.movie_session(movie_name=movie,
                            customers=ls_with_customers,
                            cleaning_staff=clean)


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]

print(cinema_visit(customers, 5, "Anna", "Madagascar"))
