from math import log,fabs
from Gui import GuiRoot
from sympy import Symbol,lambdify,sin,cos,sqrt,log


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
        

    def calculate(self,func,an,bn,error):
        range_init = list()
        fx = lambdify(x,func,'numpy')
        if an!=None and bn!=None:
            range_init = [an,bn]
        else:
            range_init = self.findInitValues(fx)
        
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
            fPn = fx(Pn)
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
        
        self.rows =  list(zip(values_an,values_bn,values_Pn,values_Fpn,Values_error))           
        self.contains_poitns_an_bn = list(zip(values_an,values_bn))
        
    
    


    
x = Symbol('x')
fx1 =  x**3 + x**2 + 4*x -10
fx2 =  x/4 +1
fx3 =  log(x,10)#obligatorio dar intervalo [1,0.1]
fx4 =  sin(x)#obligatorio dar intervalo invertido
fx5 =  (x-4)**3
fx6 =  x/5 +1
fx7 =  -x*4+1 #intervalos invertidos [10,-1]
fx8 =  0.5-((x/(1-x))*sqrt(6/2+x))#intervalos invertidos [1,0.1]

if __name__== "__main__":
    method = Biseccion(fx8,an=1,bn=0.1,error=10**-4)
    method.mainloop()
    