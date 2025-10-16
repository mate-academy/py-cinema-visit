# Відвідування кінотеатру

- Перед початком прочитайте [інструкцію](https://github.com/mate-academy/py-task-guideline/blob/main/README.md).

Ви відкрили власний кінотеатр. Щоб краще розуміти,
що відбувається в кінотеатрі,
ви вирішили вести облік подій.
Для цього вам потрібно створити такі модулі:

1.  У каталозі `app` створіть пакет `cinema`. У цьому
    пакеті створіть модулі:
    -   `bar.py` - у цьому модулі створіть клас `CinemaBar`,
        який описує роботу кінобару.
        Цей клас повинен мати лише один статичний метод `sell_product`,
        який приймає `product` - назву товару, який хоче клієнт,
        та `customer` - екземпляр `Customer`, що означає клієнта.
        Метод `sell_product` продає товар клієнту та відображає, який товар було продано і кому.

        ```python
        cb = CinemaBar()
        customer = Customer("Bob", "popcorn")
        cb.sell_product(customer=customer, product=customer.food)
        # Cinema bar sold popcorn to Bob.
        ```

    -   `hall.py` - у цьому модулі створіть клас `CinemaHall`,
        який описує дії під час кіносеансу. Його
        метод `__init__` приймає та зберігає ЛИШЕ `number` залу в кінотеатрі.
        Цей клас повинен мати лише один метод `movie_session`, який
        приймає `movie_name`, `customers` - список клієнтів
        (екземплярів `Customer`), `cleaning_staff` - прибиральника (екземпляр
        `Cleaner`). Цей метод друкує про початок фільму, викликає
        метод клієнтів `watch_movie`, друкує про закінчення фільму,
        викликає метод прибиральника `clean_hall`. Отже, ми очікуємо,
        що все перераховане вище буде виконано у функції `movie_session`.

```python
hall = CinemaHall(hall_number=5)
movie_name = "Madagascar"
customers = [
    Customer(name="Bob", food="Coca-cola"),
    Customer(name="Alex", food="popcorn")
]
cleaning_staff = Cleaner(name="Anna")

hall.movie_session(movie_name=movie_name, customers=customers, cleaning_staff=cleaning_staff)
```

2.  У каталозі `app` створіть пакет `people`. У цьому пакеті
    створіть модулі:
    -   `customer.py` - у цьому модулі створіть клас `Customer`,
        його метод `__init__` приймає та зберігає `name`, `food` - їжу, яку
        клієнт хоче купити в кінобарі.
        Цей клас повинен мати лише один метод `watch_movie`, цей
        метод приймає `movie` і друкує, який фільм дивиться клієнт.

        ```python
        bob = Customer(name="Bob", food="popcorn")
        bob.watch_movie(movie="Madagascar")
        # Bob is watching "Madagascar".
        ```

    -   `cinema_staff.py` - у цьому модулі створіть клас `Cleaner`,
        його метод `__init__` приймає та зберігає `name`.
        Цей клас повинен мати лише один метод `clean_hall`, цей метод
        приймає `hall_number` - номер залу, який прибиральник має прибрати, і
        друкує, що прибиральник прибирає цей зал.

        ```python
        anna = Cleaner(name="Anna")
        anna.clean_hall(hall_number=5)
        # Cleaner Anna is cleaning hall number 5.
        ```

У модулі `main.py` ви повинні імпортувати всі ці класи. Класи
повинні бути імпортовані за абсолютним шляхом, що починається з `app.` з
ключовим словом `from`. Напишіть
функцію `cinema_visit`, яка приймає `movie`, `customers` - список
клієнтів, елементи якого є словниками з `name` та бажаною `food`
клієнта, `hall_number` - номер залу в кінотеатрі,
`cleaner` - ім'я прибиральника, який буде прибирати
зал після кіносеансу.

Ця функція повинна створювати екземпляри `Customer`, `CinemaHall` та `Cleaner`.
Спочатку кінобар повинен продати їжу клієнтам. Для цього ви можете використовувати клас `CinemaBar`
, не створюючи екземпляра. Потім кінозал повинен запланувати кіносеанс,
і, нарешті, прибиральник повинен прибрати кінозал. Ми очікуємо, що кожен клас буде працювати з наданими даними,
приймати параметри в правильному порядку та мати необхідні методи.
Жодних додаткових перевірок чи обробки помилок не потрібно!

Приклад (не додавайте його до `main.py`):
```python
customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"
cinema_visit(customers=customers, hall_number=hall_number, cleaner=cleaner_name, movie=movie)
# Cinema bar sold Coca-cola to Bob.
# Cinema bar sold popcorn to Alex.
# "Madagascar" started in hall number 5.
# Bob is watching "Madagascar".
# Alex is watching "Madagascar".
# "Madagascar" ended.
# Cleaner Anna is cleaning hall number 5.
```

**Важливе зауваження**: Кожен метод, відповідальний за виконання завдання, повинен лише друкувати повідомлення за допомогою
функції `print()`. Немає потреби нічого повертати або використовувати модуль `logging`.

Нарешті, перевірте свій код за допомогою цього [контрольного списку](checklist.md) перед тим, як надсилати своє рішення.
