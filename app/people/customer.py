class Customer:
    def __init__(self, name, food):
        self.name = name
        self.food = food  # Виправлено: foof -> food

    def watch_movie(self, movie):
        print(f"{self.name} is watching \"{movie}\".")








# customer.py - inside this module create Customer class,
#     its __init__ method takes and stores name, food -
#     food that customer wants to buy in cinema bar.
#     This class should have only one method watch_movie,
#     this method takes movie and prints what movie customer is watching.