user_str = input('Введите строку ... ')

str_list = list(user_str.strip())
even_sym = ''
for i in range(len(str_list)):
    if i % 2 == 0:
        even_sym += str_list[i]

odd_sym = ''
for i in range(len(str_list)):
    if i % 2 != 0:
        odd_sym += str_list[i]

even_rev = []

for i in range(len(str_list)):
    if i % 2 == 0:
        even_rev += str_list[i]
even_rev.reverse()
even_str = ''.join(even_rev)
# print(even_str)

str_list.reverse()
rev_str = ''.join(str_list)

result = str(3) + ': ' + user_str[2] + '\n' 
result += 'Последний... ' + str(len(user_str) - 1) + ': ' + user_str[-1] + '\n' 
result += 'Первые 5 символы... ' + user_str[:5] + '\n'
result += 'Все символы кроме двух послединх... ' + user_str[:(len(user_str) - 2)] + '\n'
result += 'Все четные символы... ' + even_sym + '\n'
result += 'Все нечетные символы... ' + odd_sym + '\n'
result += 'Все символы в развернутом виде... ' + rev_str + '\n'
result += 'Все четные символы в развернутом виде... ' + even_str + '\n'
result += 'Длина строки... ' + str(len(str_list))

print(result)
