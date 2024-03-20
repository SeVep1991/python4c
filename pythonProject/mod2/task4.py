#Для введенного в десятичном коде натурального числа найти представление в двоичном,
# восьмеричном и шестнадцатеричном кодах. Если введено не натуральное число, вывести диагностику: «Неверный ввод».
# Использовать встроенные возможности языка python запрещено.
user_input = input ("Введите натуральное десятичное число: ")
number = int(user_input)
while number < 0:
    print("Введенное число не натурнольное. Введите еще раз")
    user_input = input("Введите натуральное десятичное число: ")
    number = int(user_input)

binary = ""
octal = ""
hexadecimal = ""

numforbinary = number
numforoctal = number
numforhexadecimal = number

while numforbinary > 0:
    binary = str(numforbinary % 2) + binary
    numforbinary = numforbinary // 2


while numforoctal > 0:
    octal = str(numforoctal % 8) + octal
    numforoctal = numforoctal // 8

while numforhexadecimal > 0:
    remainder = numforhexadecimal % 16
    if remainder < 10:
        hexadecimal = str(remainder) + hexadecimal
    else:
        hexadecimal = chr(ord('A') + remainder - 10) + hexadecimal
    numforhexadecimal = numforhexadecimal // 16


print(f"{binary}, {octal}, {hexadecimal}")