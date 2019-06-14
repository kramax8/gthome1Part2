g_countries = {1: 'google_kazakstan.txt',
        2: 'google_paris.txt',
        3: 'google_uar.txt',
        4: 'google_kyrgystan.txt',
        5: 'google_san_francisco.txt',
        6: 'google_germany.txt',
        7: 'google_moscow.txt',
        8: 'google_sweden.txt'}


for key in g_countries:
    a = str(key)
    print( a + ' ==> ' + g_countries[key])
user_choose = input('\n' + "Выберите по номеру... ")

user_text = input('напишите ваши жалобы... ')

f = open(g_countries[int(user_choose)], 'w')
f.write(user_text)
f.close()

with open(g_countries[int(user_choose)], 'r') as o_file:
    r_file = o_file.read()


print('\n' + 'Вы выбрали: ' + g_countries[int(user_choose)] + '\n' + 'Написали следующие жалобы... ' + '\n\n' + r_file)