from tkinter import *
from sympy import Symbol,lambdify
from math import fabs
from tkinter import ttk
from matplotlib import pyplot as plt
import matplotlib.animation as animation
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
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        self.canvas.stop_event_loop()
        super().destroy()
        
        
    
    def build_table_values(self,labelsColumns):
        #etiquetas 
        self.label_main = Label(self.frm,text='Values Interations')
        self.label_main.pack()
        self.table_values =  ttk.Treeview(self.frm,show="headings")
        self.table_values.pack()
        #construyo la tabla de valores 
        self.table_values['columns']=labelsColumns
        for i in labelsColumns:
            self.table_values.heading(i,text=i,anchor="w")

        for i,v in enumerate(self.rows):
            vals = [x for x in v]
            vals.insert(0,i)
            self.table_values.insert("",'end',text=i,values=vals)


    def build_label_summary(self,text=None):
        tt_ = f'{self.rows[-1][0]}' if text is None else text
        self.label_summary = Label(self.frm,foreground="#f00",text=f"Root approximation:  {tt_}  Interations:  {len(self.rows)}  Error:  {self.error}")
        self.label_summary.pack()
               
    def build_function_plt(self,f1=None,f2=None,tg=False,x1=0,x2=0):
        #grafico funcion 
        f= Figure((14,4))
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
        self.figure = f
    
    def build_animation_plt(self,f,points):
        x0=points[0][0]
        x1=points[0][1]
        x0,x1 = (x1,x0) if x0>x1 else (x0,x1)
        xpoints = np.arange(x0,x1,0.1) 
        ypounts_evaluates =np.vectorize(f)(xpoints)

        fig, ax = plt.subplots()
        fig.set_size_inches(8.1,7.1)
        plt.title("Buis")
        line,=ax.plot(xpoints,ypounts_evaluates)  
        an, = ax.plot( points[0][0],0,'ro' )    
        lan = ax.annotate('An',(points[0][0],0),color='red')  
    
        
        bn, = ax.plot( points[0][1], 0,'bo' )
        lbn = ax.annotate('Bn',(points[0][1],0),color='blue')
        
        ax.axhline(0,color='black')
        ax.axvline(0,color='black')
               
        ax.minorticks_on()
        ax.grid( True, 'minor', markevery=2, linestyle='--' )
        ax.grid( True, 'major', markevery=10 )

        def update(f):
            if f<len(points):          
                an.set_xdata(points[f][0])
                lan.set_x(points[f][0])               
                bn.set_xdata(points[f][1])
                lbn.set_x(points[f][1])        
            return an,bn,lan,lbn
        self.ani = animation.FuncAnimation(fig,update,interval=700,blit=True,frames=len(points)) 
        self.figure = fig       
        
    def build_figure(self):
        self.canvas =  FigureCanvasTkAgg(self.figure,self.frm)
        self. canvas.get_tk_widget().pack()
        self.nav = NavigationToolbar2Tk(self.canvas,self.frm)
        self.canvas.draw()
        self.canvas._tkcanvas.pack()