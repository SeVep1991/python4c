#На вход подается последовательность целых чисел.
# Требуется определить, присутствуют ли в этой последовательности одинаковые числа.
# Результат вернуть в формате Boolean.

numbers = input().split()
result = len(numbers) != len(set(numbers))
print(result)