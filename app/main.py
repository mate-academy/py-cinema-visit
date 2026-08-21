from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_list = []

    # Step 1: Sell product to all customers first
    for customer in customers:
        customer_obj = Customer(name=customer["name"], food=customer["food"])
        CinemaBar.sell_product(product=customer_obj.food,
                               customer=customer_obj)
        customer_list.append(customer_obj)

    # Step 2: Initialize hall and cleaner outside the loop
    cinema_hall = CinemaHall(number=hall_number)

    # Step 3: Run cleaner
    cleaner_obj = Cleaner(name=cleaner)

    # Step 4: Run the movie session once for all customers
    cinema_hall.movie_session(movie, customer_list, cleaner_obj)
