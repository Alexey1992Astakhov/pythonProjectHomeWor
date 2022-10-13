# 1. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента. Use comprehension.
# in
# 10
# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

import random

def list_gen() -> list:
    return[random.randrange(20) for x in range(int(input("Введите длинну списка: ")))]


def list_new() -> list:
    ls = list_gen()
    print(ls)
    return [ls[x] for x in range(1, len(ls)) if ls[x] > ls[x - 1]]

print(list_new())