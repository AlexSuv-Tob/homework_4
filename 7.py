def fact(num):
    order = 1
    for i in range(1, num + 1):
        order *= i
        yield order

num = int(input("Укажите факториал какого числа Вы хотели бы узнать?: "))
for el in fact(num):
    print(el)