#На вход подается два числа через пробел: a, b.
#Напишите функцию для реализации рекурсивного алгоритма Евклида поиска наибольшего общего делителя.

def euclidean_gcd(a, b):
    if b == 0:
        return a
    else:
        return euclidean_gcd(b, a % b)

a, b = map(int, input("Введите два числа через пробел (a, b): ").split())

result = euclidean_gcd(a, b)

print(f"Наибольший общий делитель чисел {a} и {b} равен: {result}")