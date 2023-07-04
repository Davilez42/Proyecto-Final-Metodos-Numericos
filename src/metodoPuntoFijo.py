
from math import e,fabs


#Metodo de puhnto fijo 
def metodoPuntoFijo(f,x1=None,x2=None,error=None):
    x0 = x1+x2 /2 if x1 is not None and x2 is not None else 0 #se selecciona el x0 dado un intervalo
   
    steps =  float('inf')if error is not None else 100
    valuesXn = [x0]
    valuesError = []         
    n=0
    while n<steps:
        """
        en cada iteracion se calcula el xn dato con la formula y posteriormente si se a proporcionado
        un error se hace el calculo para saber si cumple con dicho error proporcionado    
        """
        xn = f(valuesXn[-1])
        valuesXn.append(xn)
        if error!=None and n>=1:
            err = fabs((xn-valuesXn[-2])/xn)*100#formula del error, se multiplica por 100 para manejar los errores en porcentajes
            valuesError.append(err)
            if err<=error*100:
                break
        n+=1

 
    print(f"SOLUCION:{valuesXn[-1]} Iteraciones:{n+1}")

#Ejemplos 
#funciones ya trasformadas o despejadas                 
fx1 = lambda x:2**x**2 /-5
fx2 = lambda x:e**-x 

#se prueba el metodo
metodoPuntoFijo(fx1,0,-1,10**-4)


#TODO graficar resultados