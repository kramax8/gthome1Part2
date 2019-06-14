
type_num = input('Введите 10 чисел через пробел ... ')
type_num_list = list(type_num.split(' '))
result = 0
for i in type_num_list:
    result += int(i)
print(result)
