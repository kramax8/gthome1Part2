
type_num = input('Введите 10 чисел через пробел ... ')
type_num_list = list(type_num.split(' '))
# result = 0
# for i in type_num_list:
#     result += int(i)
# print(result)

# n = input("Введите целое число: ")
 
while len(type_num_list) != 3:
    try:
        result = 0
        for i in type_num_list:
            result += int(i)
            
            if len(type_num_list) == 3:
                print(result)
                break
    except ValueError:
        print("Неправильно ввели!")
        type_num = input('Введите 10 чисел через пробел ... ')
    


