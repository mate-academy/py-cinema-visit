from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
):
    list_of_customers = [Customer(name=cust["name"], food=cust["food"]) for cust in customers]
    hall_num = CinemaHall(hall_number)
    staff = Cleaner(cleaner)
    for visitor_1 in list_of_customers:
        bar = CinemaBar()
        bar.sell_product(visitor_1.food, visitor_1)
    print(f"\"{movie}\" started in hall number {hall_number}.")
    for visitor_2 in list_of_customers:
        print(f"{visitor_2.name} is watching \"{movie}\".")
    print(f"\"{movie}\" ended.")
    staff.clean_hall(hall_number)
