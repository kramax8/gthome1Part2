user_num = input('Введите число ... ')

list_num = []
i = 1
for i in range(int(user_num)):
    list_num.append(int(i) + 1)

result = 1
for j in range(len(list_num)):
    result = result * list_num[j]
print(result)
