user_list = [1,2,3,4,6,7,8,9]

new_list = 0

i = user_list[0]

for i in range(len(user_list)):
    if user_list[i] -i <= 1:
        new_list = user_list[i]
    else:
        break
    result = 'Не хватает цифра ==> ' + str(new_list + 1)

print(result)