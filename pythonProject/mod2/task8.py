# Дан список слов. Составить из последних букв каждого слова новое.
user_input = input("Введите слова: ")


last_letters = ""
current_word = ""

for char in user_input:
    if char != " ":
        current_word += char
    else:
        last_letters +=current_word[-1]
        current_word = ""

last_letters += current_word[-1]

print(last_letters)