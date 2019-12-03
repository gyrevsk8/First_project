import numpy as np
import matplotlib.pyplot as plt
def lens(f=4,d=1,u=1):
    #t=np.linspace(d,100,10000)
    x=[-d,0]
    y=[1,1]
    if u>0:
        j=[0,(1/(1/d+1/f))]
        p=[1,-1]
    else:
        j=[0,((d*f)/(d+f))]
        p=[1,2]
    plt.plot(x,y,'r')
    plt.plot(j,p,'r')
    plt.plot([-3,4.5],[0,0],'k')
    plt.plot([0,0],[-1.025,1.025],'c',lw=2.5)
    plt.axis('equal')
    plt.show()
lens(37,9,1)
lens(37,9,-1)