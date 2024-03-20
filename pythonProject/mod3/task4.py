#Строка состоит из 0 и 1.
# Выведите ‘yes’, если количество единиц совпадает с количеством нулей.
# И ‘no’ в противном случае.

user_input = input("Введите двоичное число ")
result = 'yes' if user_input.count('0') == user_input.count('1') else 'no'
print(result)