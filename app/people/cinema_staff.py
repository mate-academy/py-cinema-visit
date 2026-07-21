class Cleaner:
    # Constructor: called when an object of the class
    # is created (e.g., Cleaner("Anna"))
    def __init__(self, name: str) -> None:
        # self.name — this is the "memory" of the object.
        # We store the name to remember
        # it later its later
        self.name = name

        # Method: the object performs an action using its data (name)
    def clean_hall(self, hall_number: int) -> None:
        # print outputs the result to the console.
        # f-string substitutes variable values directly into the text.
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")
