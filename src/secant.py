
from math import e,fabs
from Gui import GuiRoot
from sympy import Symbol,lambdify
""" 
Estudiantes
- Oscar Fernando Rivera Pardo - 2067730 
- Jeferson Aguiar Dominguez Diaz - 2067607 
- Jose David Suarez Cardona -2067548 """


class Secant(GuiRoot):
    #Metodo de la secante
    def __init__(self,f,x_1=None,x_2=None,error=None):
        super().__init__('Method Secant')
        self.error = error
        self.calculate(f,x_1,x_2,error)
        self.build_table_values(["N","Xn","F(Xn)","Error"])
        self.build_label_summary()

        self.build_function_plt(f1=f,x1=-10,x2=10)
        self.build_figure()

        
    def calculate(self,f,x0,x1,error):
        steps =  float('inf')if error is not None else 80
        fx = lambdify(x,f,'numpy')
        valuesXn = [x0,x1]
        valuesError = [None]   
        valuesFxn = [fx(x0),fx(x1)]      
        n=0
        
        while n<steps:
            """
            en cada iteracion se calcula el xn dato con la formula y posteriormente si se a proporcionado
            un error se hace el calculo para saber si cumple con dicho error proporcionado    
            """
            #Formula de la secante
            xn = valuesXn[-1]-((valuesXn[-1]-valuesXn[-2])/(valuesFxn[-1]-valuesFxn[-2]) )*valuesFxn[-1]
            valuesFxn.append(fx(xn))
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
        self.rows= list(zip(valuesXn,valuesFxn,valuesError))



#Ejemplos 
#funciones ejemplos
x = Symbol('x')
fx1 =  x**3 + x**2 + 4*x -10 # 1 2 
fx2 =  x/4 +1 # -5 -3
fx3 =  (x-4)**3# 3 5
fx4 =  x/5 +1#-7 -4
fx5 =  -x*4+1#0 1
fx7 = -x**2 + 10 #2 4
fx9 = x**2 -8 #intervalos 2 3
fx8 = x - 10  #intervalos 9 11    
""" Funcionamiento:
para probar el metodo se debe usar la sgt syntaxis:
- Secant(funcion,x0,x1,error) <el error es opcional>
#Ejemplos
"""

if __name__ == "__main__":
   method  = Secant(fx7,2,4) 
   method.mainloop()

