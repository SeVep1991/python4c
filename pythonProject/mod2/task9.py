#Человек вводит на сайте номер телефона,
# ему позволено для удобства использовать кроме плюса и цифр знаки ‘-’, ‘)’, ‘(’ и пробелы.
# Уберите их из ввода.
user_input = input("Номер: ")

cleaned_number  = ""

v = ["(",")"," ","-"]
for i in user_input :
    if i not in v:
        cleaned_number +=i

print(cleaned_number )