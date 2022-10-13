# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
# in
# 100
# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100]

def num_krat(num: int) -> list:
    return [x for x in range(20, num + 1) if x % 20 == 0 or x % 21 == 0]

print(num_krat(int(input("Введите число: "))))





