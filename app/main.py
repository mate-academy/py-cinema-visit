from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list[dict],
                 number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_ls = []
    cinema_hal = CinemaHall(number=number)
    clean = Cleaner(name=cleaner)
    for cust in customers:
        cust_instance = Customer(name=cust["name"], food=cust["food"])
        customers_ls.append(cust_instance)
        CinemaBar.sell_product(product=cust_instance.food,
                               customer=cust_instance)
    cinema_hal.movie_session(movie_name=movie,
                             customers=customers_ls,
                             cleaning_staff=clean)


if __name__ == "__main__":
    customers = [
        {"name": "Bob", "food": "Coca-cola"},
        {"name": "Alex", "food": "popcorn"}
    ]
    hall_number = 5
    cleaner_name = "Anna"
    movie = "Madagascar"
    cinema_visit(customers=customers,
                 number=hall_number,
                 cleaner=cleaner_name,
                 movie=movie)
