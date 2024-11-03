# TODO написать функцию remove
from typing import Any


def remove(list_: list, rem: Any) -> list:
    if rem in list_:
        list_.reverse()
        list_.remove(rem)
        list_.reverse()
    elif rem not in list_:
        raise ValueError

    return list_

print(remove([0, 1, 2, 0, 1, 2], 0))  # [0, 1, 2, 1, 2]
print(remove([0, 1, 2], 0))  # [1, 2]
print(remove([0, 1, 2, 3, 4], 4))  # [0, 1, 2, 3]
