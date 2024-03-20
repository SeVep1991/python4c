# На вход подается список чисел через пробел.
# Напишите функцию выводящую сообщение для списка чисел:
# 1) Все числа равны
# 2) Все числа разные
# 3) Есть равные и неравные числа
def check_numbers(numbers):
    unique_numbers = set(numbers)

    if len(unique_numbers) == 1:
        print("Все числа равны")
    elif len(unique_numbers) == len(numbers):
        print("Все числа разные")
    else:
        print("Есть равные и неравные числа")

input_numbers = input("Введите список чисел через пробел: ").split()
numbers = [int(num) for num in input_numbers]

check_numbers(numbers)