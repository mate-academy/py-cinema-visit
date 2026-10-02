from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:

    movie_customers = []
    for customer_item in customers:
        new_customer = (
            Customer(name=customer_item["name"],
                     food=customer_item["food"]))
        movie_customers.append(new_customer)
    new_cleaner = Cleaner(cleaner)
    hall = CinemaHall(hall_number)

    for customer in movie_customers:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall.movie_session(movie,
                       customers=movie_customers,
                       cleaning_staff=new_cleaner)
    pass
