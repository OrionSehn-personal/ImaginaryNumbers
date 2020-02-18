import numpy as np
import matplotlib.pyplot as plt
from complexnumbers import cnum

'''---------------------------------------------------------------------------------
A set of complex number functions, mostly serving as an introductory exploration 
of what precicely a complex number is, how they can be used, and what they look like.



---------------------------------------------------------------------------------'''


#plt.plot(np.random.rand(10))
#plt.show()
def clickdisplay():
    fig, ax = plt.subplots()
    ax.plot(np.random.rand(10))
    def onclick(event):
        print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
              ('double' if event.dblclick else 'single', event.button,
               event.x, event.y, event.xdata, event.ydata))

    fig.canvas.mpl_connect('button_press_event', onclick)
    #print(cid)
    plt.show()
#clickdisplay()
def clickplot():
    fig, ax = plt.subplots()
    ax.margins(3, 2)
    ax.autoscale(False)
    def onclick(event):
        plt.scatter([event.xdata], [event.ydata])
        plt.show()
    fig.canvas.mpl_connect('button_press_event', onclick)
    plt.show()    
#clickplot()


