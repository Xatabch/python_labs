#Морозов Иван, ИУ7-24

import functions as fc
a = -2#int(input("Введите начало отрезка: "))
b = 5#int(input("Введите конец отрезка: "))
h = 0.5#float(input("Введите шаг: "))
n = 10#int(input("Введите максимальное количество итерраций: "))
eps1 = 0.01#float(input("Введите первую точность: "))
eps2 = 0.01#float(input("Введите вторую точность: "))
error = 0
print("""
         Коды ошибок:
         0 - нет ошибок
         1 - превышено максимальное число итерраций
""")
print('{:>10s} | {:<5s}{:>5s}| {:^10s} | {:^9s} | {:^5s} | {:^5} |'.format('№', 'X(n)', 'X(n+1)', 'X', 'f(X)', 'n', 'err'))
print('         ---------------------------------------------------------')

#Первая часть задания.
#Шаги.
while a < b:
    sled_znach = a
    pred_znach = sled_znach
    sled_znach = pred_znach + h
    a += h
    #print(fc.func(pred_znach),fc.func(sled_znach))
    #Проверка на наличие корней на данном отрезке.
    if ((fc.func(pred_znach) < 0) and (fc.func(sled_znach) > 0)) or ((fc.func(pred_znach) > 0) and (fc.func(sled_znach) < 0)):
        #print("Корень найден")
        x0 = pred_znach
        x1 = sled_znach
        proverca_1 = fc.second_proizv(x0)
        proverca_2 = fc.second_proizv(x1)
        number_of_root = 0
#РАЗОБРАТЬСЯ С ДУБЛИРОВАНИЕМ ЦИКЛОВ!!!!!
        if proverca_1:
            #print("proverca_1")
            #print(proverca_1, proverca_2)
            i = 0
            x2 = fc.newton1(x0)
            while abs(x2-x0) > eps1:
                x2 = x0
                x0 = fc.newton1(x0)
                #print(x0,x2)
                i += 1
                if i >= n:
                    error = 1
                    break
            #print(x0)
            #print(pred_znach, sled_znach)
            #number_of_root += 1
            #print(number_of_root)
            function = fc.func(x0)
            fc.vivod(x0, number_of_root, pred_znach, sled_znach, function, i, error)
            error = 0
        else:
            #print("proverca_2")
            #print(proverca_1, proverca_2)
            i = 0
            x2 = fc.newton1(x1)
            while abs(x2-x1) > eps1:
                x2 = x1
                x1 = fc.newton1(x1)
                #print(x1,x2)
                i += 1
                if i >= n:
                    error = 1
                    break
            #print(x1)
            #number_of_root += 1
            function = fc.func(x1)
            fc.vivod(x1, number_of_root, pred_znach, sled_znach, function, i, error)
            error = 0

#2 Часть задания.
