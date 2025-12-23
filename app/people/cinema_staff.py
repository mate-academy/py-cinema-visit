

class Cleaner:
    """
    Represents a Cleaner entity responsible for
    performing cleaning tasks.

    This class is used to instantiate a cleaner
    with a specific name who can perform cleaning
    operations on specified hall numbers.

    """
    def __init__(self, name: str) -> None:
        """
        Represents a class that initializes
        with a name attribute.

        This class is used to demonstrate formatted
        docstrings following the reStructuredText
        specification strictly. It contains an initialization
        method for setting up the `name` attribute.

        :ivar name: The name associated with
            an instance of this class.
        """
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        """
        Cleans the specified hall. This method displays
        a message indicating which hall the cleaner is
        currently cleaning.

        :param hall_number: The number of the hall
            to be cleaned.
        :type hall_number: int
        :return: None
        """
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")
