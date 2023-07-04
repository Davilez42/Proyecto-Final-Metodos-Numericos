from sympy import *
from math import fabs
import numpy as np

def function(f,x0,error=None):
    fx = lambdify(x,f,'numpy') #funcion original   
    fxPrime = lambdify(x, f.diff('x'),'numpy')#funcion derivada 

    limit_iteracion =  100 if error==None else float('inf') #creo limite dependiento del argumento de error
    n = 0 
    xns = [x0]
    while n<limit_iteracion:
        xn  =xns[n]
        xn1 = xn - fx(xn)/fxPrime(xn)
        xns.append(xn1)       
        #comprueba error
        if error!=None:
            ant = xns[n] 
            err = fabs((xn1-ant)/xn1)
            if err*100<=error*100:
                print(err*100,error*100)
                n+=1
                break;         
        n+=1
    print(f"ITERACIONES: {n} \nAproximacion Raiz: {xns.pop()}" )        


x = Symbol('x')
#Ejemplos 
fx1 =  x**3 + x**2 + 4*x -10
fx2 =  x/4 +1
fx5 =  (x-4)**3
fx6 =  x/5 +1
fx7 =  -x*4+1
fx8 =  0.5-(x/(1-x))
fx9 = -x**2 + 10

function(fx2,5)
