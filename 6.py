from itertools import count, cycle, islice

# 1
my_list = int(input('Введите первичное знасчение: '))
stop_list = int(input('Введите количесвто значений, которые вы хотите вывести: '))

for el in islice(count(my_list), stop_list):
        print(el)


#2
my_list_2 = list(input('Введите строку для повторения: '))
stop_list_2 = int(input('Введите количесвто значений: '))
c = 0
for el in cycle(my_list_2):
    if c > (stop_list_2):
        break
    print(el)
    c += 1