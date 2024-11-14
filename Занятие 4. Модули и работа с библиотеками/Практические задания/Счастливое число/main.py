from itertools import count
from typing import final


def is_lucky_number(num: int) -> bool:
    ...  # TODO проверить что число шестизначное и положительное
    first = 0
    second = 0
    first_sum= 0
    second_sum = 0
    try:
        list_ = [n for n in str(num)]
        if num > 0 and len(list_) == 6:
            ...
    except ValueError:
        print("Ошибка")
    else:
        first = list_[:3]
        second = list_[3:]
        for j in first:
            first_sum += int(j)

        for k in second:
            second_sum += int(k)
        if first_sum == second_sum:
            return True
        return False





print(is_lucky_number(123321))
print(is_lucky_number(111111))
print(is_lucky_number(123456))
print(is_lucky_number(456243))
