from math import log,fabs,sin,sqrt
from Gui import GuiRoot
import numpy as np

class Biseccion(GuiRoot):
    def __init__(self,function,an=None,bn=None,error=None):
        super().__init__("Method Biseccion")
        self.calculate(function,an,bn,error)
        self.error = error
        self.geometry("1100x1050")
        self.build_table_values(["N","An","Bn","Pn","f(Pn)","Error"])   
        self.build_label_summary(f'[{self.rows[-1][0]},{self.rows[-1][1]}]')    
        self.build_animation_plt(function,self.contains_poitns_an_bn)
        self.build_figure()
       
     
    def findInitValues(self,function):
        an =0
        bn =0    
        for i in range(-100,100):
            try:
                if (function(i)<0):
                    an=i
            except:
                pass
            try:
                if (function(i)>0):
                    bn=i 
                    break
            except:
                pass  
        return [an,bn]
        

    def calculate(self,funcion,an,bn,error):
        range_init = list()
        
        if an!=None and bn!=None:
            range_init = [an,bn]
        else:
            range_init = self.findInitValues(funcion)
        
        #calculo lso pasos estimados        
        num = fabs(range_init[1]-range_init[0])
        step_estimed = int(fabs(log(num/error,10)/log(2,10))) if error!=None else 1000
        
        values_Pn = list()
        values_Fpn = list()
        Values_error = [None]
        values_an = [range_init[0]]
        values_bn = [range_init[1]]       
        n=0 
   
        while n<step_estimed+10:           
            Pn = (range_init[0] + range_init[1])/2#se obtiene el PN
            fPn = funcion(Pn)
            if fPn<0:
                range_init[0]=Pn
            else:
                range_init[1]=Pn      
                           
            values_Pn.append(Pn)
            values_Fpn.append(fPn)  
            
            values_an.append(range_init[0]) ##se momorizan an y bn #para la
            values_bn.append(range_init[1]) 
            
            #calculo el error
            if n>1:
                ant =values_Pn[-2]           
                err = round(fabs( (Pn - ant) /Pn),6)
                Values_error.append(err)
            
                if error!=None and err<=error:
                    break         
            n+=1    
        
        self.rows =  np.array(zip(values_an,values_bn,values_Pn,values_Fpn,Values_error))           
        self.contains_poitns_an_bn = np.array(zip(values_an,values_bn))
    
    


    

fx1 = lambda x: x**3 + x**2 + 4*x -10
fx2 = lambda x: x/4 +1
fx3 = lambda x: log(x,10)#obligatorio dar intervalo
fx4 = lambda x: sin(x)#obligatorio dar intervalo 
fx5 = lambda x: (x-4)**3
fx6 = lambda x: x/5 +1
fx7 = lambda x: -x*4+1
fx8 = lambda x: 0.5-((x/(1-x))*sqrt(6/2+x))


if __name__== "__main__":
    method = Biseccion(fx8,an=1,bn=0,error=10**-4)
    method.mainloop()
    