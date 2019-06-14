user_str = 'hello world'

new_str = list(user_str.split(' '))
new_str.reverse()
new_str = ' '.join(new_str)

print(new_str)