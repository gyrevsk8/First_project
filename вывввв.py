import numpy as np
import matplotlib.pyplot as plt
def circle_plotter(f=4,d=1):
    t=np.linspace(d,100,10000)
    x=[-d,0]
    y=[1,1]
    j=[0,(1/(1/d+1/f))]
    p=[1,0]
    plt.plot(x,y,'r')
    plt.plot(j,p,'r')
    plt.plot([-3,4.5],[0,0],'k')
    plt.plot([0,0],[2,0],'k',lw=3)
    plt.axis('equal')
    plt.show()
circle_plotter(9,3)
