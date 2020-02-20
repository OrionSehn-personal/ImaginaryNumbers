import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
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

def singleclickplot():
    fig, ax = plt.subplots()
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)
    def onclick(event):
        plt.cla()
        plt.xlim(-3, 3)
        plt.ylim(-3, 3)
        plt.scatter([event.xdata], [event.ydata])
        plt.show()

    fig.canvas.mpl_connect('button_press_event', onclick)
    plt.show()    
#singleclickplot()




def complexiteration():# strangely crashes after 20 or so clicks. inconsistent
    fig, ax = plt.subplots()
    plt.xlim(-2, 1)
    plt.ylim(-1, 1)
    plt.grid()
    def onclick(event):
        plt.cla()
        plt.xlim(-2, 1)
        plt.ylim(-1, 1)
        plt.grid()
        c = cnum(event.xdata, event.ydata)
        z = cnum()
        ziterationsx = []
        ziterationsy = []
        for i in range(50):
            ziterationsx.append(z.getA())
            ziterationsy.append(z.getB())
            z = (z*z)+ c
            if abs(z) > 100:
                break
        x = np.array(ziterationsx)
        y = np.array(ziterationsy)
        plt.plot(x, y, linewidth = 1)

        

        #print(ziterations)

        #print(z)



        #plt.scatter([event.xdata], [event.ydata])
        plt.show()

    fig.canvas.mpl_connect('button_press_event', onclick)
    plt.show()    

#complexiteration()


def inMandlebrot(x, y): # returns a rgb touple associated with the behaviour
        c = cnum(x, y) #of the number given to it. 
        z = cnum()
        numiterations = 0
        for i in range(100):
            z = (z*z)+ c
            numiterations += 1 
            if abs(z) >= 2:
                return (255 - numiterations, 255 - numiterations, 255 - numiterations)
        return (0, 0, 0)


def generateMandlebrot(x0 = -2, x1 = 1, y0 = -1, y1 = 1, resolution = (480, 360)):
    
    xvalues = np.linspace(x0, x1, resolution[0])
    yvalues = np.linspace(y0, y1, resolution[1])
    endlist = []
    for y in yvalues:
        ylist = []
        for x in xvalues:
            ylist.append(inMandlebrot(x, y))
        endlist.append(ylist)  
    endarray = np.array(endlist)
    plt.imshow(endarray)
    plt.subplots_adjust(left = 0, right = 1, bottom = 0, top = 1)
    plt.show()
            




generateMandlebrot()
#Misiurewicz point 
#generateMandlebrot(-0.1011 - 0.10, -0.1011 +0.10, 0.9563 - 0.10, 0.9563 +0.10)
#generateMandlebrot(-0.1011 - 0.01, -0.1011 +0.01, 0.9563 - 0.01, 0.9563 +0.01)
