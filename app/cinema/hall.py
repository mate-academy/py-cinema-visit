from app.cinema.bar import CinemaBar


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie_name: str, customers: list,
                      cleaning_staff: object) -> None:
        for customer in customers:
            CinemaBar.sell_product(customer, customer.food)

        movie_start = "\"" + movie_name + "\" started in hall number "
        movie_start += str(self.number) + "."
        print(movie_start)

        for customer in customers:
            customer.watch_movie(movie_name)

        movie_end = "\"" + movie_name + "\" ended."
        print(movie_end)

        cleaning_staff.clean_hall(self.number)
