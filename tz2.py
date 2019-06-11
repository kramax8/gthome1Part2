count_people = int(input('Type how many people? '))
count_apple = int(input('Type how many apple? '))

sum1 = count_apple % count_people

sum2 = (count_apple - sum1) / count_people


print('Каждый человек получит по ' + str(int(sum2)) + ' яблок, ' + 'в корзине ' + str(int(sum1)) + ' яблок.')
    