"""
Przekształć podane generatory korzystając z comprehension
"""


def get_names():
    for n in ['Dwight', 'Angela', 'Jim', 'Andy']:
        yield n


def get_nums():
    for num in range(5):
        small = num / 10
        yield small
