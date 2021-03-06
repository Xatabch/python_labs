import math as m
import pylab
from matplotlib import mlab
import scipy.optimize as sp
import sympy as sym
#import scipy.misc as misc

#Функция
def func(x):
    return (x**3 - 5*x**2 + 6)#(50*x**3 - 10*x + 3)#m.sin(x)#(x**2 - 3)#(x**3 + 4*x - 3)

#Производная от функции
def proizv_func(x):
    return (3*x**2 - 10*x + 6)#m.cos(x)#(2 * x)#(3 * x ** 2 + 4)

#Определение числа от которого начинать уточнение.
def second_proizv(x):
    function = (x**3 - 5*x**2 + 6)#m.sin(x)#(x**2 - 3)#x ** 3 + 4 * x - 3
    second = 6*x - 10#-m.sin(x)#6 * x
    result = function * second
    if result > 0:
        return 1
    else:
        return 0
#Формула метода Ньютона.
def newton1(x):
    if proizv_func(x) != 0:
        x = x - func(x) / proizv_func(x)
    return x

#Уточнение корня
def utochnenie(proverca,x,eps1,n,number_of_root,pred_znach,sled_znach,error,b,h,a):
    i = 0
    x2 = newton1(x)
    while abs(x2-x) > eps1:
        x2 = x
        x = newton1(x)
        i += 1
        if i >= n:
            error = 1
            break
    d = a
    c = b 
    function = func(x)
    viv = vivod(x, number_of_root, pred_znach, sled_znach, function, i, error, d,c)
    return viv

#Вывод результатов.
def vivod(x, number_of_root, pred_znach, sled_znach, function, i, error, d,c):
    if sled_znach > c:
        sled_znach = c
    if pred_znach != sled_znach:
        if x >= d and x <= c:
            if (x >= 0) and (function > 0):
                print('{:>10} | {:<5}{:>5} | {:>10.7f} | {:<5.3e} | {:^5} | {:^5} |'.format(number_of_root, pred_znach, sled_znach, x, function, i, error))
            elif (x <= 0) and (function < 0):
                print('{:>10} | {:<5}{:>5} | {:<5.7f} |{:<0.3e} | {:^5} | {:^5} |'.format(number_of_root, pred_znach, sled_znach, x, function, i, error))
            elif (x <= 0) and (function > 0):
                print('{:>10} | {:<5}{:>5} | {:<5.7f} | {:<0.3e} | {:^5} | {:^5} |'.format(number_of_root, pred_znach, sled_znach, x, function, i, error))
            elif (x >= 0) and (function < 0):
                print('{:>10} | {:<5}{:>5} | {:^11.7f}|{:<0.3e} | {:^5} | {:^5} |'.format(number_of_root, pred_znach, sled_znach, x, function, i, error))
            elif (x == 0) and (function == 0):
                print('{:>10} | {:<5}{:>5} | {:^11.7f}| {:<0.3e} | {:^5} | {:^5} |'.format(number_of_root, pred_znach, sled_znach, x, function, i, error))
        else:
            error = 2
            print('{:>10} | {:<5}{:>5} | {:^11.7s}| {:^9s} | {:^5s} | {:^5} |'.format(number_of_root, pred_znach, sled_znach, '-', '-', '-', error))

def graph(xmin,xmax):
    h = abs(xmin - xmax)/100
    dx = 0.01

    xlist = mlab.frange(xmin, xmax, dx)
    ylist = [func(x) for x in xlist]

    x2 = []
    y2 = []
    x3 = []
    y3 = []
    x4 = [xmin,xmax]
    y4 = [func(xmin),func(xmax)]
    
    x = sym.Symbol('x')
    f = x**3 - 5*x**2 + 6
    f_dif = sym.diff(f, x, 1)
    extr = sym.solve(f_dif, x)
    for k in extr:
        x2.append(float(k))
        y2.append(func(float(k)))
    f_2dif = sym.diff(f_dif, x, 1)
    peregib = sym.solve(f_2dif, x)
    for k in peregib:
        x3.append(float(k))
        y3.append(func(float(k)))

    rootsx = []
    rootscount = 0
    while xmin < xmax:
        if func(xmin) * func(xmin + h) < 0:
            rootsx.append(sp.ridder(func, xmin ,xmin+h))
            rootscount += 1
        xmin += h
        
    pylab.plot(xlist, ylist)
    pylab.grid(True)
    pylab.plot(rootsx,[0] * rootscount,'bo', label = "Roots")
    pylab.plot(x2,y2,'ro', label = "Extrema")
    pylab.plot(x3,y3,'go', label = "Inflection points")
    pylab.plot(x4,y4,'yo', label = "min/max")
    pylab.legend()
    pylab.show()
