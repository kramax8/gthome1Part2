user_age = input('Введите ваш возрат... ')

even_list = []
odd_list = []

for i in range(int(user_age) + 1):
    if int(user_age) % 2 == 0 and i > 0 and i % 2 == 0:
        even_list.append(i)
    elif i > 0:
        odd_list.append(i)
        
if int(user_age) % 2 == 0:
    print('четный ' + str(even_list))
else:
    print('не четный ' + str(odd_list))


