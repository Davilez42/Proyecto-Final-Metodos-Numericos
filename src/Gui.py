from tkinter import *
from sympy import Symbol,lambdify
from math import fabs
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk 
import numpy as np
class GuiRoot(Tk):
    def __init__(self,title):
        super(GuiRoot,self).__init__()
        self.title(title)
        self.geometry("700x850")
        self.frm =  Frame(self)
        self.frm.pack()
        self.rows = []
        self.x= Symbol('x')
        
        
    def build_table_values(self,labelsColumns):
        #etiquetas 
        self.label_main = Label(self.frm,text='Values Interations')
        self.label_main.pack()
        self.table_values =  ttk.Treeview(self.frm,show="headings")
        self.table_values.pack()
        #construyo la tabla de valores 
        self.table_values['columns']=labelsColumns
        for i in labelsColumns:
            self.table_values.heading(i,text=i)

        for i,(xn,error) in enumerate(self.rows):
            self.table_values.insert("",'end',values=[i,xn,error])
        self.label_summary = Label(self.frm,foreground="#f00",text=f'Aproach root:  {self.rows[-1][0]}  /  Iterations:  {len(self.rows)}  / Error:  {self.error}')
        self.label_summary.pack()
           
    def build_function_plt(self,f1=None,f2=None,tg=False,x1=0,x2=0):
        #grafico funcion 
        f= Figure()
        a = f.add_subplot(111)
        a.set_title(f"F(x)={f1}")
        xvals = np.arange(x1,x2,0.1)
        yvals = lambdify(self.x,f1,'numpy')(xvals) if tg else f1(xvals)
        a.plot(xvals,yvals)
        a.plot(self.rows[-1][0],0,'ro')
        #configuracion del grid
        if f2 is not None:
            yf2vals = f2(xvals)
            a.plot(xvals,yf2vals)
        a.axhline(0,color='black')
        a.axvline(0,color='black')
        a.minorticks_on()
        a.grid( True, 'minor', markevery=2, linestyle='--' )
        a.grid( True, 'major', markevery=10 )
        canvas =  FigureCanvasTkAgg(f,self.frm)
        canvas.get_tk_widget().pack()
        nav = NavigationToolbar2Tk(canvas,self.frm)
        canvas._tkcanvas.pack()