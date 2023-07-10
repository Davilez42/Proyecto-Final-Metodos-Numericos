from sympy import Symbol,lambdify
from math import fabs
import numpy as np
from Gui import GuiRoot
""" 
Estudiantes
- Oscar Fernando Rivera Pardo - 2067730 
- Jeferson Aguiar Dominguez Diaz - 2067607 
- Jose David Suarez Cardona -2067548 """


class NewtonRaphson(GuiRoot): 
    def __init__(self,function,x0,error=None):
        super().__init__("Method Newton Raphson")
        self.error = error
        self.calculate(function,x0,error)
        self.build_table_values(["N","Xn","Error"])
        self.build_label_summary()
        self.build_function_plt(f1=function,x1=-10,x2=10)
        self.build_figure()
    
    def calculate(self,f,x0,error):
        """
        se utiliza la funcion lambdify para obtener una funcion lambda  de una expresion dada en simbolos
        """
        fx = lambdify(x,f,'numpy') #funcion original   
        fxPrime = lambdify(x, f.diff('x'),'numpy')#funcion derivada 
        limit_iteracion =  100 if error==None else float('inf') #creo limite dependiento del argumento de error
        n = 0 
        xns = [x0]
        errors = [None]
        while n<limit_iteracion:
            """
            En cada iteracion se obtiene el ultimo xn calculado para posteriormente calcular el x1 con la formula 
            """
            xn  =xns[n]#obtengo el ultimo
            xn1 = xn - fx(xn)/fxPrime(xn)#calculo el xn1  con la formula
            xns.append(xn1)#se agrega a lista para tener un seguimiento de los valores en cada iteracion       
            #comprueba error
            """
            para calcular el error se obtiene el ultimo de la lista, 
            en este caso seria el xn-1 y se calcula el error con el x1 actual, si el error cumple 
            la condicion de ser menor o igual al error proporcionado se rompe el bucle, al no proporcionar un error
            solo se van hacer 100 iteraciones          
            """
            ant = xns[n] #obtengo el ultimo
            err = fabs((xn1-ant)/xn1)#calculo el error <la funcion fabs es para calcular valor absoluto>
            errors.append(round(err,6))     
            if round(err,6)==0.0:#si el error es igual a 0 se rompé el cliclo, para no gastar recursos           
                n+=1
                break 
            
            if error is not None and err<=error:#si se cumple el error se rompe el ciclo
                n+=1
                break;
            
            n+=1 #se agrega siempre uno a n ya que n empieza desde 0
        self.rows = np.array(list(zip(xns,errors)))#comprimo las dos listas de valores 

"""
Ejemplos:
en esta parte se utiliza la funcion Symbol() de la libreria numpy la cual se asigna una variable como simbolo
para posteriormente convertir una expresion de python en forma de symbolos
"""
x = Symbol('x')
fx1 =  x**3 + x**2 + 4*x -10
fx2 =  x/4 +1
fx3 =  (x-4)**3
fx4 =  x/5 +1
fx5 =  -x*4+1
fx6 =  0.5-(x/(1-x))#esta funcion Se grafica mal debiudo a la libreria que se usa
fx7 = -x**2 + 10
"""
Funcionamiento:
para probar el metodo se debe usar la sgt syntaxis:
- metodoNewtRaphson(funcion,x0,error) <el error es opcional>
#Ejemplos
 method = NewtonRaphson(fx2,5)
 method = NewtonRaphson(fx1,3,error=10**-4)
 method = NewtonRaphson(fx4,3,error=10**-4)
"""
if __name__ == "__main__":
    method = NewtonRaphson(fx3,0.5,error=10**-4)
    method.mainloop()
