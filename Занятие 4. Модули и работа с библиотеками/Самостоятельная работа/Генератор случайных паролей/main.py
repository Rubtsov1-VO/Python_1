import string
from random import sample


def get_random_password() -> str:
    population = string.digits + string.ascii_lowercase +string.ascii_uppercase  # TODO написать функцию генерации случайных паролей
    return sample(population,8)

print(get_random_password())
