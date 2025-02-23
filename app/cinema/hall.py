from typing import List


class CinemaHall:

    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: List["Customer"],
            cleaning_staff: "Cleaner"
    ) -> None:
        print(f"\"{movie_name}\" started in hall number {self.number}")

        for customer in customers:
            customer.watch_movie()

        print(f"{movie_name} ended.")

        # TODO: print "Cleaner {cleaning_staff.name} is cleaning hall number {self.number}"
        # TODO: call cleaning_staff.clean_hall()
