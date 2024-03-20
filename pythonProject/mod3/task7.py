#Человек вводит на сайте номер телефона,
# ему позволено для удобства использовать кроме плюса и цифр знаки ‘-’, ‘)’, ‘(’ и пробелы.
# Уберите их из ввода.
phone_number = input()
cleaned_number = ''.join(char for char in phone_number if char.isdigit() or char == '+')
print(cleaned_number)