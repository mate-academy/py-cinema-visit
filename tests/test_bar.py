from app.cinema_bar import CinemaBar

def test_cinema_bar():
    bar = CinemaBar("VIP Bar", "First Floor")
    customer = {"name": "Bob"}
    menu = ['popcorn', 'soda']
    bar.sell_product(customer, 'popcorn', menu)