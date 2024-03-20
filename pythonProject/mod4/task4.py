#На вход подается строка.
# Напишите функцию для реализации: если из слова можно составить палиндром,
# то составить его и вывести на экран.
def is_palindrome(word):
    return word == word[::-1]

def make_palindrome(input_str):
    words = input_str.split()

    for word in words:
        if is_palindrome(word):
            print(f"Можно составить палиндром из слова '{word}': {word[::-1]}")

input_str = input()
make_palindrome(input_str)