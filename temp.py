import numpy as np
import matplotlib.pyplot as plt
def grav_deviation():
    d1=6
    l=10
    a=30
    b=30
    x=[0,d1*np.cos(a)]
    y=[0,d1*np.sin(a)]
    plt.plot(x,y)
    d=[d1*np.cos(a),l*np.cos(a+b)]
    f=[d1*np.sin(a),l*np.sin(a+b)]
    plt.plot(d,f)
    x1=[l*np.cos(a+b),l*np.cos(a+b)]
    y1=[l*np.sin(a+b),l*np.sin(a+b)]
    plt.plot(x1,y1,marker='o',ms=7,color='b')
    plt.axis('equal')
    plt.show()

grav_deviation()
