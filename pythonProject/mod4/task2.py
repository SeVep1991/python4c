#Возводить в степень можно гораздо быстрее, чем за n умножений!
# Для этого нужно воспользоваться следующими рекуррентными соотношениями:
#a^n = (a^2)^n/2  при четном n,
#a^n = a × a^n−1 при нечетном n.
#На вход подается два числа через пробел: a, n.
# Напишите функцию для реализации алгоритма быстрого возведения в степень с помощью рекурсивной функции.

def fast_power(base, power):
    if power == 0:
        return 1
    elif power % 2 == 0:
        return fast_power(base * base, power // 2)
    else:
        return base * fast_power(base, power - 1)

a, n = map(int, input("Введите два числа через пробел (a n): ").split())

result = fast_power(a, n)
print(f"{a} в степени {n} = {result}")