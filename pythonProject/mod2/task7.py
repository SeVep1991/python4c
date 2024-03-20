#На вход подается строка s и символ i.
# Необходимо найти количество символов i, расположенных в начале строки.

s = input("Введите строку s: ")
i = input("Введите символ i: ")

count = 0
for char in s:
    if char == i:
        count += 1
    else:
        break

print(count)