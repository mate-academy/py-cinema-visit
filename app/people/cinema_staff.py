class Cleaner:
    def __init__(self, name: str) -> None:
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        print(
            "Cleaner {} is cleaning hall number {}.".format(
                self.name,
                hall_number
            )
        )
