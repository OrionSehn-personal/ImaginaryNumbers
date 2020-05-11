import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from complexnumbers import cnum
import time

'''---------------------------------------------------------------------------------
A set of complex number functions, mostly serving as an introductory exploration 
of what precicely a complex number is, how they can be used, and what they look like.
---------------------------------------------------------------------------------'''

'''---------------------------------------------------------------------------------
A function to output the coordinates of a point clicked on the screen, pulled
from the documentaion of matplotlib returns none
---------------------------------------------------------------------------------'''
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

'''---------------------------------------------------------------------------------
function to display the point clicked on the canvas
---------------------------------------------------------------------------------'''
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

'''---------------------------------------------------------------------------------
function to display the point clicked on the canvas, will clear canvas between each
click event
---------------------------------------------------------------------------------'''

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

'''---------------------------------------------------------------------------------
function which shows exactly how a complex number iterates through z = z^2 + c
will show how the complex number behaves under iteration when being considered
for being in the Mandelbrot set or not. 
---------------------------------------------------------------------------------'''

def complexiteration():
    hidemandle = False
    
    img = plt.imread("Mandlebrot3000,2000cropped.png")
    fig, ax = plt.subplots()
    axes2 = plt.axes()
    plt.xlim(-2, 1)
    plt.ylim(-1, 1)
    axes2.imshow(img, extent =[-2, 1, -1, 1])
    #plt.grid()

    def runiteration(event):
        plt.clf()
        axes2 = plt.axes()
        axes2.imshow(img, extent =[-2, 1, -1, 1])
        plt.xlim(-2, 1)
        plt.ylim(-1, 1)
        if (event.xdata == None) or (event.ydata == None):
            return
        c = cnum(event.xdata, event.ydata)
        z = cnum()
        ziterationsx = []
        ziterationsy = []
        for i in range(80):
            ziterationsx.append(z.getA())
            ziterationsy.append(z.getB())
            z = (z*z)+ c
            if abs(z) > 50:
                break
        x = np.array(ziterationsx)
        y = np.array(ziterationsy)
        plt.plot(x, y, linewidth = 0.5, color = 'orange')        
        event.canvas.draw()
    
    fig.canvas.mpl_connect('motion_notify_event', runiteration)
    plt.show() 

       
complexiteration()

'''---------------------------------------------------------------------------------
helper function for generateMandelbrot(), which takes two numbers, an x and a y, 
interprets them as a complex number x + yi and iterates it, to determine if it 
is in fact in the Mandelbrot set. returns an rgb touple of the colour, black if
it is in the set, and white - gray, depending on how many iterations it takes for
the number to leave the stable region. 
---------------------------------------------------------------------------------'''

def inMandelbrot(x, y): # returns a rgb touple associated with the behaviour
        c = cnum(x, y) #of the number given to it. 
        z = cnum()
        numiterations = 0
        for i in range(100):
            z = (z*z)+ c
            numiterations += 1 
            if abs(z) >= 2:
                return (255 - numiterations, 255 - numiterations, 255 - numiterations)
        return (0, 0, 0)

'''---------------------------------------------------------------------------------
funciton which will produce a mandlebrot set:
takes a starting point x0, y0, and an end point, x1, y1
and a touple representing the x and y resolution of the mandlebrot set. 

because you can take different points, and different resolutions, you can view the
entirty of the mandelbrot set, or you can zoom in on a region, by selecting 
the values of the window size to be a certain value.
---------------------------------------------------------------------------------'''

def generateMandelbrot(x0 = -2, x1 = 1, y0 = -1, y1 = 1, resolution = (480, 360)):
    
    xvalues = np.linspace(x0, x1, resolution[0])
    yvalues = np.linspace(y0, y1, resolution[1])
    endlist = []
    for y in yvalues:
        ylist = []
        for x in xvalues:
            ylist.append(inMandelbrot(x, y))
        endlist.append(ylist)  
    endarray = np.array(endlist)
    plt.imshow(endarray)
    plt.subplots_adjust(left = 0, right = 1, bottom = 0, top = 1)
    plt.show()
                




#generateMandelbrot(resolution = (3000,2000))
#Misiurewicz point 
#generateMandelbrot(-0.1011 - 0.10, -0.1011 +0.10, 0.9563 - 0.10, 0.9563 +0.10, resolution = (300,200))
#generateMandelbrot(-0.1011 - 0.0001, -0.1011 +0.0001, 0.9563 - 0.0001, 0.9563 +0.0001, resolution = (300,200))

