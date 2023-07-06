
from math import e,fabs
from Gui import GuiRoot
from sympy import Symbol,lambdify


class FixedPoint(GuiRoot):
    #Metodo del punto fijo 
    def __init__(self,function_transf,function_norlm,x1=None,x2=None,error=None):
        super().__init__('Method Fixed Point')
        self.error = error
        self.calculate(function_transf,x1,x2,error)
        self.build_table_values(["N","Xn","Error"])
        self.build_label_summary()
        #Nota al graficar la azul es la funcion transformada y la zapote es la normal 
        self.build_function_plt(f1=function_transf,f2=function_norlm,x1=-2,x2=2)
        self.build_figure()

        
    def calculate(self,f,x1,x2,error):
        x0 = x1+x2 /2 if x1 is not None and x2 is not None else 0 #se selecciona el x0 promedio dado un intervalo   
        steps =  float('inf')if error is not None else 80
        valuesXn = [x0]
        valuesError = [None]         
        n=0
        fx = lambdify(x,f,'numpy')
        while n<steps:
            """
            en cada iteracion se calcula el xn dato con la formula y posteriormente si se a proporcionado
            un error se hace el calculo para saber si cumple con dicho error proporcionado    
            """
            xn = fx(valuesXn[-1])
            
            valuesXn.append(xn)
            err = fabs((xn-valuesXn[-2])/xn)#formula del error, se multiplica por 100 para manejar los errores en porcentajes
            valuesError.append(round(err,6))
            if valuesXn[-2]==xn:#condicoon para detener el ciclo en caso de que no se pueda seguir caclulando mas
                n+=1
                break 
            if error!=None and err<=error :               
                n+=1
                break
            n+=1
        self.rows= list(zip(valuesXn,valuesError))



#Ejemplos 
#funciones ya trasformadas o despejadas
x = Symbol('x')
fx1 = 2**x**2 +5*x             
fx1_trans = 2**x**2 /-5

fx2 = (e**-x) -x
fx2_trans = e**-x 


""" Funcionamiento:
para probar el metodo se debe usar la sgt syntaxis:
- FixedPoint(funcionTransformada,funcionSinTransformar,x0,x1,error) <el error es opcional>
#Ejemplos
<Se debe proporcionar un Intervalo donde se sepa que la raiz se encuentre  en [a,b] para mejor la aproximacion>
 method = FixedPoint(fx1_trans,fx1,0,-1,error=10**-4)
 method = FixedPoint(fx2_trans,fx2,0,1,error=10**-4)
"""

if __name__ == "__main__":
   method  = FixedPoint(fx1_trans,fx1,0,1) 
   method.mainloop()

