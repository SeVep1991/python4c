a = int(input())
b = int(input())
c = int(input())
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print(a, b, c) # Упорядочили их по возрастанию
print(b)# число, которое будет стоять между двумя другими после упорядочивания.