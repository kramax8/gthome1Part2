user_age = input('Введите ваш текущий весс... ')

age_moon = 'Ваш текущий весс на луне... ' + str(int(user_age) * 0.165 ) + '\n'

age_moon += 'Ваш через 15 лет на луне... ' + str((int(user_age) + 15) * 0.165 )

print(age_moon)