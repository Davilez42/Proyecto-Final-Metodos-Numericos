from sympy import Symbol,lambdify
from math import fabs
from tkinter import *
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk 
import numpy as np

class NewtonRaphson(Tk):
    def __init__(self,function,x0,error=None):
        super(NewtonRaphson,self).__init__()
        self.title("Method Newton Raphson")
        self.geometry("700x850")
        self.frm =  Frame(self)
        self.frm.pack()
        self.error = error
        self.calculate(function,x0,error)
        self.build_table_values()
        self.build_function_plt(function)
    
    def calculate(self,f,x0,error):
        """
        se utiliza la funcion lamdify para obtener una funcion lambda  de una expresion dada en simbolos
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
            errors.append(round(err,6)*100)     
            print(round(err,6)*100)
            if round(err,6)*100==0.0:#si el error es igual a 0 se rompé el cliclo, para no gastar recursos           
                n+=1
                break 
            
            if error is not None and err*100<=error*100:#si se cumple el error se rompe el ciclo
                n+=1
                break;
            
            n+=1 #se agrega siempre uno a n ya que n empieza desde 0
        self.rows = np.array(list(zip(xns,errors)))#comprimo las dos listas de valores 


        
    def build_table_values(self):
        #etiquetas 
        self.label_main = Label(self.frm,text='Values Interations')
        self.label_main.pack()
        self.table_values =  ttk.Treeview(self.frm,columns=(1,2,3),show="headings")
        self.table_values.pack()
        #construyo la tabla de valores 
        self.table_values.heading(1,text="N")
        self.table_values.heading(2,text="Xn")
        self.table_values.heading(3,text="Error")
        for i,(xn,error) in enumerate(self.rows):
            self.table_values.insert("",'end',values=[i,xn,error])
        self.label_summary = Label(self.frm,foreground="#f00",text=f'Aproach root:  {self.rows[-1][0]}  /  Iterations:  {len(self.rows)}  / Error:  {self.error}')
        self.label_summary.pack()
    
    
    
    def build_function_plt(self,func):
        #grafico funcion 
        f= Figure()
        a = f.add_subplot(111)
        a.set_title(f"F(x)={func}")
        xvals = np.arange(-10,10,0.1)
        yvals = lambdify(x,func,'numpy')(xvals) 
        a.plot(xvals,yvals)
        a.plot(self.rows[-1][0],0,'ro')
        #configuracion del grid
        a.axhline(0,color='black')
        a.axvline(0,color='black')
        a.minorticks_on()
        a.grid( True, 'minor', markevery=2, linestyle='--' )
        a.grid( True, 'major', markevery=10 )
        canvas =  FigureCanvasTkAgg(f,self.frm)
        canvas.get_tk_widget().pack()
        nav = NavigationToolbar2Tk(canvas,self.frm)
        canvas._tkcanvas.pack()


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
    method = NewtonRaphson(fx7,4)
    method.mainloop()
