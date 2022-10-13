# 5. ** Реализовать функцию, возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого)

import random


def rofl(count: int, unic=False) -> list:
    ls1 = ["автомобиль", "лес", "огонь", "город", "дом"]
    ls2 = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    ls3 = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    if unic:
        result = []

        try:
            for i in range(count):
                result.append(f"{ls1.pop(random.randint(0, len(ls1) - 1))} "
                              f"{ls2.pop(random.randint(0, len(ls2) - 1))} "
                              f"{ls3.pop(random.randint(0, len(ls3) - 1))} ")
        except ValueError:
            print("Мы не можем сделать так много уникальных шуток")

        return result
    else:
        return [f"{random.choice(ls1)} {random.choice(ls2)} {random.choice(ls3)}" for i in range(count)]


print(rofl(10, unic=True))
print(rofl(10))