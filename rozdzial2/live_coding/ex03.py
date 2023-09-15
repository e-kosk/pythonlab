"""
Zapisz podane funkcje w postaci funkcji anonimowych oraz przypisz je do zmiennych
"""


def increment(a):
    return a + 1


def get_first(elements):
    return elements[0]


def add(a, b):
    return a + b


def avg(elements: list):
    s = sum(elements)
    l = len(elements)
    return s / l


def full_name(dictionary: dict):
    first_name = dictionary.get('first_name')
    last_name = dictionary.get('last_name')
    return f'{first_name} {last_name}'


def combine(*args: str):
    return " ".join(args)
