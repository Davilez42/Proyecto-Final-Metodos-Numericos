from sympy import Symbol,lambdify
from math import fabs
import numpy as np

def metodoNewtRaphson(f,x0,error=None):
    """
    se utiliza la funcion lamdify para obtener una funcion lambda  de una expresion dada en simbolos
    """
    fx = lambdify(x,f,'numpy') #funcion original   
    fxPrime = lambdify(x, f.diff('x'),'numpy')#funcion derivada 

    limit_iteracion =  100 if error==None else float('inf') #creo limite dependiento del argumento de error
    n = 0 
    xns = [x0]
    while n<limit_iteracion:
        """
        En cada iteracion se obtiene el ultimo xn calculado para posteriormente calcular el x1 con la formula 
        """
        xn  =xns[n]#obtengo el ultimo
        xn1 = xn - fx(xn)/fxPrime(xn)#calculo el xn1  con la formula
        xns.append(xn1)#se agrega a lista para tener un seguimiento de los valores en cada iteracion       
        #comprueba error
        if error!=None:
            """
            para calcular el error se obtiene el ultimo de la lista, 
            en este caso seria el xn-1 y se calcula el error con el x1 actual, si el error cumple 
            la condicion de ser menor o igual al error proporcionado se rompe el bucle, al no proporcionar un error
            solo se van hacer 100 iteraciones
            
            """
            ant = xns[n] #obtengo el ultimo
            err = fabs((xn1-ant)/xn1)#calculo el error <la funcion fabs es para calcular valor absoluto>
            if err*100<=error*100:#
                #print(err*100,error*100)
                n+=1
                break;         
        n+=1 #se agrega siempre uno a n ya que n empieza desde 0
        
    print(f"ITERACIONES: {n} \nAproximacion Raiz: {xns.pop()}" )        


x = Symbol('x')
"""
Ejemplos:
en esta parte se utiliza la funcion Symbol() de la libreria numpy la cual se asigna una variable como simbolo
para posteriormente convertir una expresion de python en forma de symbolos
"""
fx1 =  x**3 + x**2 + 4*x -10
fx2 =  x/4 +1
fx3 =  (x-4)**3
fx4 =  x/5 +1
fx5 =  -x*4+1
fx6 =  0.5-(x/(1-x))
fx7 = -x**2 + 10
"""
Funcionamiento:
para probar el metodo se debe usar la sgt syntaxis:
- metodoNewtRaphson(funcion,x0,error) <el error es opcional>
#Ejemplos
metodoNewtRaphson(fx2,5)
metodoNewtRaphson(fx1,3,error=10**-4)
metodoNewtRaphson(fx4,3,error=10**-4)

"""
metodoNewtRaphson(fx2,5)
metodoNewtRaphson(fx3,3,error=10**-4)

#TODO graficar resultados