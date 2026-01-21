class Cleaner:
    """
    Cleaner class represents cinema staff that contains function
    for cleaning the cinema halls after movies.
    """
    def __init__(self, name: str) -> None:
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        """
        Function for cleaning hall after movie session.
        :param hall_number: cinema hall number
        :return: None
        """
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")
