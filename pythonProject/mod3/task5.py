#Дан список слов.
# Составить из последних букв каждого слова новое.

words = input().split()
result = ''.join(word123[-1] for word123 in words)
print(result)
