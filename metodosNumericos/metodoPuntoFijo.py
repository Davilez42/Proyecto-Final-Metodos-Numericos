##Metodo de puhnto fijo <s>
from math import e,fabs



def metodoPuntoFijo(f,x1=None,x2=None,error=None):

    x0 = x1+x2 /2 if x1 is not None and x2 is not None else 0
    steps =  float('inf')if error is not None else 100
    valuesXn = [x0]
    valuesError = []         
    n=0
    while n<steps:
        xn = f(valuesXn[-1])
        valuesXn.append(xn)
        if error!=None and n>=1:
            err = fabs((xn-valuesXn[-2])/xn)*100
            valuesError.append(err)
            if err<=error*100:
                break
        n+=1
    #verifico 
 
    print(f"SOLUCION:{valuesXn[-1]} Iteraciones:{n+1}")


#funciones ya trasformadas o despejadas                 
fx1 = lambda x:2**x**2 /-5
fx2 = lambda x:e**-x 

#se prueba el metodo
metodoPuntoFijo(fx1,0,-1,10**-4)