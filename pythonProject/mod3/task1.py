#Упорядочим их по возрастанию.
#Какое число будет стоять между двумя другими?

user_input = input("ввод: ")
a, b, c = sorted(map(int, user_input.split()))
print(a, b, c)