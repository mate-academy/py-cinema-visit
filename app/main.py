from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    list_customers = []
    cinema_hall = CinemaHall(hall_number)
    cleaner_object = Cleaner(cleaner)
    for customer in customers:
        customer_obj = Customer(name=customer["name"], food=customer["food"])
        list_customers.append(customer_obj)
        CinemaBar.sell_product(product=customer_obj.food, customer=customer_obj)
    cinema_hall.movie_session(movie_name=movie, customers=list_customers, cleaning_staff=cleaner_object)

# # #test
# customers = [{'name': 'Susan', 'food': 'Pepsi'}, {'name': 'Michael', 'food': 'Coca-cola'}, {'name': 'Monica', 'food': 'popcorn'}]
# hall_number = 3
# cleaner = "Vasiliy"
# movie = "Interstellar"
#
# print(cinema_visit(customers=customers, hall_number=hall_number, cleaner=cleaner, movie=movie))



