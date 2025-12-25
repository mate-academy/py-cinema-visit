from typing import Optional, List, Tuple

from movies import list_movies, get_movie_price, get_movie_by_index
from tickets import buy_ticket
from snacks import list_snacks, get_snack_price, buy_snack, get_snack_by_index
from utils import print_line, ask_int

# mapa simples de descontos
DISCOUNTS = {
    "0": ("Nenhum", 0.00),
    "1": ("Estudante", 0.20),
    "2": ("Sênior (65+)", 0.30),
}


def choose_movie() -> Optional[Tuple[str, int]]:
    """Permite escolher filme por número (1..N) ou por nome."""
    print("Filmes em cartaz:")
    print(list_movies())
    choice = input("Escolha o filme (número ou nome): ").strip()
    if not choice:
        return None
    if choice.isdigit():
        selected = get_movie_by_index(int(choice))
        if selected:
            return selected
        print("Índice de filme inválido.")
        return None
    price = get_movie_price(choice)
    if price is None:
        print("Filme inválido.")
        return None
    return choice, price


def choose_discount() -> Tuple[str, float]:
    print_line()
    print("Descontos disponíveis:")
    for k, (name, rate) in DISCOUNTS.items():
        pct = int(rate * 100)
        print(f"{k}. {name} ({pct}% off)")
    opt = input("Escolha o desconto (0/1/2): ").strip() or "0"
    if opt not in DISCOUNTS:
        print("Opção inválida. Usando: Nenhum.")
        opt = "0"
    return DISCOUNTS[opt]


def choose_snacks() -> Tuple[int, List[Tuple[str, int, int, int]]]:
    """
    Loop para comprar vários snacks.
    Retorna (total_snacks, itens) onde itens = [(nome, qty, unit, total_line), ...]
    """
    print_line()
    print("Snacks disponíveis:")
    print(list_snacks())
    items: List[Tuple[str, int, int, int]] = []
    total = 0

    while True:
        s = input("Snack (número/nome) ou Enter para finalizar: ").strip()
        if not s:
            break

        name: Optional[str]
        unit_price: Optional[int]

        if s.isdigit():
            res = get_snack_by_index(int(s))
            if res is None:
                print("Índice de snack inválido.")
                continue
            name, unit_price = res
        else:
            unit_price = get_snack_price(s)
            if unit_price is None:
                print("Snack inválido.")
                continue
            name = s

        qty = ask_int("Quantidade do snack? ")
        if qty is None or qty <= 0:
            print("Quantidade inválida.")
            continue

        line_total = buy_snack(name, qty, unit_price)
        items.append((name, qty, unit_price, line_total))
        total += line_total
        print(f"Adicionado: {name} x{qty} = {line_total} NIS")

    return total, items


def main() -> None:
    print("🎬 Bem-vindo ao Cinema Visit 🎬")
    print_line()

    movie_selected = choose_movie()
    if movie_selected is None:
        return
    movie_name, movie_price = movie_selected

    qty = ask_int("Quantos ingressos? ")
    if qty is None or qty <= 0:
        print("Quantidade inválida.")
        return

    discount_name, discount_rate = choose_discount()

    subtotal_tickets = buy_ticket(movie_name, qty, movie_price)
    discount_value = int(round(subtotal_tickets * discount_rate))
    total_tickets = subtotal_tickets - discount_value

    total_snacks, snack_items = choose_snacks()

    print_line()
    print(f"Filme: {movie_name}")
    print(f"Ingressos: {qty} × {movie_price} = {subtotal_tickets} NIS")
    if discount_rate > 0:
        print(f"Desconto ({discount_name}): -{discount_value} NIS")
    print(f"Subtotal ingressos: {total_tickets} NIS")

    if snack_items:
        print_line()
        print("Snacks:")
        for name, q, unit, line in snack_items:
            print(f"- {name}: {q} × {unit} = {line} NIS")
    print(f"Subtotal snacks: {total_snacks} NIS")

    print_line()
    total = total_tickets + total_snacks
    print(f"💰 Total a pagar: {total} NIS")
    print("Bom filme! 🍿")


if __name__ == "__main__":
    main()
