from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_list = []

    for cust in customers:
        name = cust.get("name")
        food = cust.get("food", "default_food")

        if name:
            customers_list.append(Customer(name=name, food=food))

    for customer in customers_list:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall = CinemaHall(hall_number)
    cleaner_staff = Cleaner(cleaner)
    hall.movie_session(movie_name=movie, customers=customers_list,
                       cleaning_staff=cleaner_staff)
