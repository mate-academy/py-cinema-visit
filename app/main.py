from app.cinema import Customer, CinemaBar, CinemaHall, Cleaner

def cinema_visit(customers: list[dict], hall_number: int, cleaner: str, movie: str):
    customer_instances = []
    for c in customers:
        new_customer = Customer(**c)
        CinemaBar.sell_product(new_customer, new_customer.food)
        customer_instances.append(new_customer)

    hall = CinemaHall(hall_number)
    staff = Cleaner(cleaner)

    hall.movie_session(movie, customer_instances, staff)
