user_str = "Hello world! I read new file in new file"   

first_ind = user_str.find("f")  
last_ind = user_str.rfind('f')

result = 'Index of a first f... ' + str(first_ind) + '\n' + 'Index of a last f... ' + str(last_ind)

print(result)
