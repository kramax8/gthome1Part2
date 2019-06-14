type_num = input('Введите два числа через запятую "2,9 " ' + " ")
type_num_list = list(type_num.split(','))

type_num_in0 = int(type_num_list[0])

type_num_in1 = int(type_num_list[1])

print_list = []

def print_num(a, b):
    if a <= b:
        for i in range(a, b + 1):
            print_list.append(i)

print_num(type_num_in0, type_num_in1)

print(print_list)
