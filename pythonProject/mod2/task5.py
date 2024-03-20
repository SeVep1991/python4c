# На вход подается доменное имя сайта.
# Необходимо вывести все домены по порядку начиная с домена первого уровня.

user_input = (input("Введите имя сайта: "))

subdomain = ""
main_domains = ""
top_level_domain = ""

dot_count = 0
for char in user_input:
    if char == '.':
        dot_count +=1

    elif dot_count == 1:
        main_domains += char

    elif dot_count == 2:
        top_level_domain += char

    else:
        subdomain += char

print(top_level_domain)
print(main_domains)
print(subdomain)