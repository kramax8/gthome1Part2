type_num = int(input('Type number ... '))

def ret_type_num():
    if type_num > 0:
        return 1
    elif type_num < 0:
        return -1
    elif type_num == 0:
        return 0

print(ret_type_num())