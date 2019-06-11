time1 = input('Введите начало времени в формате Ч:М:С ')
time2 = input('Введите конец времени в формате Ч:М:С ')

trans_list_time1 = list(time1.split(':'))

trans_list_time2 = list(time2.split(':'))

trans_list_time1_h = int(trans_list_time1[0]) * 3600
trans_list_time1_m = int(trans_list_time1[1]) * 60
trans_list_time1_s = int(trans_list_time1[2])

trans_list_time1 = trans_list_time1_h + trans_list_time1_m + trans_list_time1_s


trans_list_time2_h = int(trans_list_time2[0]) * 3600
trans_list_time2_m = int(trans_list_time2[1]) * 60
trans_list_time2_s = int(trans_list_time2[2])

trans_list_time2 = trans_list_time2_h + trans_list_time2_m + trans_list_time2_s

result = trans_list_time2 - trans_list_time1

print('Промежуток ' + str(result) + ' секунд')