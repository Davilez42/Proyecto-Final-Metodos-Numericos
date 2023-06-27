from math import log,fabs,sin,sqrt
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import numpy as np

def findInitValues(function):
    an =0
    bn =0    
    for i in range(-100,100):
        try:
            if (function(i)<0):
                an=i
        except:
            print('DOMIO ERROR EN ',i)
            pass
        try:
            if (function(i)>0):
                bn=i 
                break
        except:
            pass  
    return [an,bn]
    

def bisseccionMethod(funcion,an=None,bn=None,error=None):
    range_init = list()
    
    if an!=None and bn!=None:
        range_init = [an,bn]
    else:
        range_init = findInitValues(funcion)
             
    num = fabs(range_init[1]-range_init[0]) 
    print(num)  
    step_estimed = int(fabs(log(num/error,10)/log(2,10))) if error!=None else 1000
    
    values_Pn = list()
    Values_error = list()
    
    n=0
    
    contains_poitns_an_bn = [range_init.copy()]
    
    while n<step_estimed+10:           
        Pn = (range_init[0] + range_init[1])/2#se obtiene el PN

        if funcion(Pn)<0:
            range_init[0]=Pn
        else:
            range_init[1]=Pn                 
        values_Pn.append(Pn)
        
        contains_poitns_an_bn.append((range_init[0],range_init[1]))##se momorizan an y bn
        
        if error!=None and n>0:
            ant =values_Pn[n-1]
            err = round(fabs( (Pn - ant) /Pn),int(fabs(round(log(error,10)))))
            Values_error.append(err)
            if err==error:
                n+=1
                print('SALE POR ERROR PROPORCIONADO')
                break         
        n+=1    
     
    #print(contains_poitns_an_bn)            
    graficar(funcion,contains_poitns_an_bn,step_estimed,n,error)
   
   

def graficar(f,points,ste,n,error):
    x0=points[0][0]
    x1=points[0][1]
    x0,x1 = (x1,x0) if x0>x1 else (x0,x1)
    xpoints = np.arange(x0,x1,0.1) 
    print(xpoints)
    ypounts_evaluates =np.vectorize(f)(xpoints)
    
    fig, ax = plt.subplots()
    plt.title(f"""
    MetodoBiseccion
Pasos Estimados:{ste}/ Pasos tomados:{n} / error:{error} /Rango inicial [an:{points[0][0]} , bn:{points[0][1]}]
        Resultado:{points.pop()}
              """)
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
    ani = animation.FuncAnimation(fig,update,interval=700,blit=True,frames=len(points)) 
    plt.show()    

    

fx1 = lambda x: x**3 + x**2 + 4*x -10
fx2 = lambda x: x/4 +1
fx3 = lambda x: log(x,10)#obligatorio dar intervalo
fx4 = lambda x: sin(x)#obligatorio dar intervalo 
fx5 = lambda x: (x-4)**3
fx6 = lambda x: x/5 +1
fx7 = lambda x:-x*4+1
fx8= lambda x:0.5-((x/(1-x))*sqrt(6/2+x))
bisseccionMethod(fx8,an=0.5,bn=0.1,error=10**-4)


    